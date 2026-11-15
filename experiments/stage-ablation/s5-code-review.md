# S5 状态机代码审查报告（静态审查）

- 审查对象：`s5_state_machine.py`（1322 行）、`research_hook.py`（895 行），关联 `s5_pipeline.py` / `s5_hierarchy.py`
- 审查日期：2026-11-15
- 方法：纯静态阅读 + AST 检查（placeholder 与 format 调用交叉核对）+ git log 对照近期修复
- 范围：① 节点展开 L1→L2→L3 边界条件 ② 检索通道逻辑（中文路由 / webllm 超时 fallback / whitelist）③ rework 循环终止性 ④ verify 判定一致性

---

## 一、s5_state_machine.py

### 1.1 节点展开（L1→L2→L3）

**[高] 多父节点批次：子节点 parent_ids 指向整批父节点，边语义错误**
- 位置：`s5_state_machine.py:528-609`（`_decompose_layer`），调用点 `:984-985`
- 问题：frontier 按每批 3 个父节点送进同一个 prompt（`P1H_INDEX` 的 `parents_block` 含多个父节点），但每个返回的子节点被统一赋 `parent_ids=[p.id for p in parents]`（:604），即每个子节点都声称以整批 3 个父节点为父。后果：
  1. 三边复核（:989-998）用 `p.id in c.parent_ids` 判断"p 的孩子"，同一子节点会被 3 个父节点各自认领一次，`classify_edge` 的 children 列表互相污染；
  2. 扇出 cap（:1006-1021）按 `p.id in k.parent_ids` 过滤，3 个父节点共享同一组 kids，每个父节点都看到完整 kids 列表再各自截断，`kids` 列表被反复改写（`kids = [k for k in kids if k not in dropped]` 在 3 个父节点循环里叠加），实际保留数可能远少于 cap 设计值；
  3. `judge_necessary_batch` 的 `par_claims`（:1059）把 3 个父节点的 claim 都算进"父上下文"，必要性裁决语义被稀释。
- 建议：prompt 要求模型为每个子节点输出 `parent` 字段（指定它属于哪个父节点）；解析时只填该父节点 id；解析失败时按 claim 相似度（复用 `_ngram_overlap`）归属，而不是无脑挂全部父节点。

**[中] 同批 L1 节点被贡献过滤器标 degraded 后，下一轮 frontier 仍包含它们**
- 位置：`:958-982`（标记 `p.status = "degraded"`）+ `:939-940`（frontier 选取）
- 问题：贡献过滤把低贡献 L1 节点标 `degraded` 并从**当前轮** frontier 移除，但下一轮 frontier 只按 level==lv_max 选取，不检查 status。如果 lv_max 没推进（本轮新节点被 dedup/necessary 全丢），同一批节点会再次进入 l1_frontier，再次调 `classify_edge`（每次 1-5 次 LLM 采样），重复烧 token 且结果不稳定（temperature 采样导致可能这轮剪下轮不剪）。
- 建议：frontier 选取加 `n.status not in ("degraded",)` 过滤，或对已判过边类型的节点缓存结果（`p.edge_type` + 贡献值落盘到节点）。

**[中] 停止判据 pass_rate 在"全丢"轮为 0.0，streak 计数与 gain 方差重置存在交互盲区**
- 位置：`:1078-1099`
- 问题：`n_candidates = len(deduped) + n_new_dropped`。当 dedup 阶段（n-gram>0.7）丢掉全部新节点时，`cand_list` 为空，`judge_necessary_batch` 不产生任何 verdict，`n_new_dropped=0`，`n_candidates=0`，`pass_rate = 0/max(0,1) = 0.0` → 走 `elif not deduped` 分支 streak+1，这部分正确。但 dedup 丢弃**不计数**（`dropped_redundant` 只统计 necessary 过滤的丢弃），所以"模型反复输出与已有节点 n-gram 相似的变体"这种死循环场景，streak 会正常累积到 stop_rounds=5 才停——可接受，但 5 轮里每轮都白烧 3×N 次 decompose LLM 调用（每批 3 父节点 × 8000 tokens）。
- 建议：dedup 丢弃也计入 `dropped_redundant`（或单独计数器），让 pass_rate 反映真实冗余率；或在 dedup 全丢时直接 streak+2（加速收敛）。

**[低] gap_check 补充节点 level 硬编码 `L{lv_max+1}`，source 硬编码 "search"**
- 位置：`:1030-1040`
- 问题：gap_check 补充的节点不继承 edge_type（默认 cartesian）、不带 search_query、parent_ids 为空。后续 rework 时 `par_claims` 为空列表，必要性/矛盾裁决缺少父上下文。功能上可接受（gap 节点本来就是补漏），但与主路径节点字段不齐，下游 `assemble` 侧若依赖 parent_ids 会断链。
- 建议：gap 节点至少带上触发它的父节点 id（gap_check prompt 里已有 existing_nodes 上下文）。

**[低] 层级解析对非 "L" 前缀 level 的鲁棒性**
- 位置：`:934`、`:940`、`:950`
- 问题：`int(str(n.level).lstrip("L"))` 对 `level="L1"` 正常，但若 LLM 在 checkpoint 恢复路径（`NodeRecord(**nd)`，:1235）里写入了 `"level": "1"` 或 `"level": "l1"`（小写），`lstrip("L")` 后 `"1"` 可解析，`"l1"` → `int("l1")` 抛 ValueError → 整个 run FATAL。当前数据流里 level 都是代码生成的 `f"L{next_lv}"`，风险低，但 resume 路径是反序列化外部 JSON，属于边界条件。
- 建议：写一个 `_parse_level(n)` 辅助函数统一容错（isdigit 检查 + 小写归一），所有 5 处调用点替换。

**[低] s5_hierarchy.py 独立路径的编号与去重弱于状态机**
- 位置：`s5_hierarchy.py:86-103`
- 问题：`start_id=len(nodes_all)+len(new_this_round)+1` 在同轮多 batch 下会重叠（batch1 的 kids 占 N5-N8，batch2 的 start_id 按 `len(nodes_all)+len(new_this_round)+1` 算，此时 new_this_round 已含 batch1 的 4 个，所以 batch2 从 N9 起——实际正确）。但去重只用 `claim[:40]` 精确前缀匹配（:96-99），比状态机的 n-gram 0.7 弱得多，同义变体会全部进树。另外 :125 `verify_node(node, srcs)` 传的是原始 node dict（无 search_query 字段），`search_node` 里 `node.get("search_query")` 为空 → 永远用中文 claim 检索，D32 修复（模型生成英文检索词）在这条路径上失效。
- 建议：若 s5_hierarchy 仍是活跃路径，对齐状态机的去重与 search_query 透传；若已被状态机取代，标记 deprecated 防止误用。

### 1.2 rework 循环终止性

**[中] rework 有节点级上限但无全局轮次上限，"rework 成功→下轮再失败"可跨轮循环**
- 位置：`:678-681`（`rework_count >= max_rework` 才放弃）、`:1107-1110`（每轮对 unverified 调 rework）
- 结论：单节点最多 rework 2 次（`max_rework=2`），**单节点不会无限循环**——这一点是安全的。但全局层面：每轮新节点都会进入 verify→rework 流程，只要树还在增长（每轮有新节点），rework 就会持续发生，直到 J_stop（5 轮低增益）或 max_nodes/max_depth 触发。最坏情况：每轮 3 个新节点全部 verify 失败 → 每轮 3×(1 次 angle LLM + 最多 2 次 search + 2 次 verify) 的 rework 开销，持续 5 轮才停。不是无限循环，但**没有全局 rework 预算**（如总 rework 次数上限或 rework 开销占比上限）。
- 建议：加 `cfg.max_total_rework`（如 30），累计 `rework_events` 长度超限后跳过 rework 直接标 degraded。

**[中] `_rework_angle` 的 queries 可能返回与原 query 相同或近似的词**
- 位置：`:757-784`
- 问题：prompt 要求"不同检索角度"，但没有程序化校验。LLM 完全可能返回与原 `search_query` 相同/近似的词（尤其原 claim 本身就是英文时），导致重搜同一 query、得到同一批来源、verify 同样失败，白白消耗一次 rework_count。
- 建议：对返回的 queries 做 `_ngram_overlap(q, node.search_query) > 0.7` 检查，命中则丢弃该 query；全部命中时直接返回 False。

**[低] `_rework_directed` 成功后不更新 `self.confirmed`**
- 位置：`:708-755`
- 问题：rework 成功后节点 claim/status/evidence 都更新了，但 `self.confirmed` 里仍是旧条目（`_verify_batch` 时 append 的旧 claim + degraded/failed status）。confirmed 会喂给下一轮 decompose 的 `confirmed_block`（:533-536），模型会看到"该节点是 degraded"的旧记录，与树里的 verified 状态矛盾，可能干扰后续分解。
- 建议：rework 成功后把 confirmed 中该 node.id 的条目替换为 `(node.id, node.corrected_claim, "verified")`。

**[低] contradiction_events 的 `fixed` 标记与 rework 的交互**
- 位置：`:751-752`（`for ev in events: ev["fixed"] = True`）+ `:671-674`（contra_idx 只收 `not ev.get("fixed")` 的事件）
- 问题：一个节点可能出现在多个矛盾事件里（A 与 B 矛盾、A 与 C 矛盾）。定向 rework 修好 A 后把**所有**涉及 A 的事件标 fixed，即使 B/C 那边的问题并未真正解决（LLM 裁决只看了 A 的视角）。后续 rework 不会再对 B/C 触发 directed 修正，矛盾可能残留到终盘。
- 建议：只标"当前 node 作为被修正方"的事件 fixed，或 rework 后对矛盾对双方各做一次轻量 verify 确认。

### 1.3 其他状态机问题

**[中] checkpoint 恢复不恢复 `_gain_history` 和 `_no_ness_streak`**
- 位置：`:1230-1255`（resume 块）
- 问题：resume 后 `_gain_history=[]`、`_no_ness_streak=0`、`low_gain_streak=0`。如果崩溃前已经累积了 4 轮低增益 streak，resume 后从 0 重新计，可能多跑 4 轮才触发 J_stop。不是 bug 但浪费 token。
- 建议：checkpoint 里落盘 `_gain_history` 和 `low_gain_streak`，resume 时恢复。

**[中] FATAL 落盘的 checkpoint 缺 `objective_mode`、`contradiction_events`、`question`**
- 位置：`:1286-1297`（FATAL 块）
- 问题：E15 修复后 FATAL 会落盘当前树状态，但该 ckpt 缺 `objective_mode`（resume 时 :1247 从 ckpt 读，缺失则回退 "formula"——如果崩溃的是 text arm，resume 后变成 formula arm，**消融臂被静默篡改**）；缺 `contradiction_events`（:1249 读不到 → 空列表，矛盾反馈链断裂）；缺 `question`（resume 后 question 来自命令行参数，若参数不一致则树与题不匹配）。
- 建议：FATAL 落盘字段与 `_save_checkpoint`（:838-851）对齐，至少补 `objective_mode` 和 `contradiction_events`。

**[低] `--qid` 自定义标识回退到 gpu 题面，但 `qid` 本身继续用于落盘文件名**
- 位置：`:1184-1209`
- 问题：`qid="gpu-method"` 时题面用 `QUESTIONS["gpu"]`（正确），但 `runs-s5-sm-gpu-method.json` 里的 `question` 字段是 gpu 题——这是设计意图（M1/M2 消融臂用同题不同 prompt）。但 `extract_entities(question)` 在 `__init__` 里用 q 调用（:441），而 `sm = DecompStateMachine(q, qid=qid)`（:1220）传的 q 是回退后的 gpu 题，一致。无 bug，仅记录：qid 同时承担"题面标识"和"实验臂标识"两个语义，建议拆成 `--qid` + `--arm`。

**[低] `verify_only` 模式不做 rework、不做 contradiction 反馈**
- 位置：`:906-924`
- 问题：verify-only 模式（树已完整只补核验）跳过 rework 和 contradiction scan 的反馈回路（scan 有调 :915，但 contradiction_events 无处消费——没有后续 decompose 轮）。verify-only 下检出的矛盾只记录不修复。
- 建议：verify-only 模式下 contradiction scan 的结果至少落盘到 SMResult，供下游 assemble 侧感知。

---

## 二、research_hook.py

### 2.1 中文 query 路由

**[中] `filter_sources` 的中文过滤是"域名白名单 + 关键词"混合，但 arXiv 通道的中文来源永远被过滤**
- 位置：`research_hook.py:706-856`（`research_hook` 主函数）+ `filter_sources`
- 问题：中文 query 走 zh-wiki + DDG 中文通道，arXiv 通道对中文 query 基本无结果（arXiv 是英文库）。路由逻辑本身正确（中文 query 不浪费 arXiv 调用），但 `filter_sources` 的白名单过滤（权威域名优先）对中文来源的判定依赖域名后缀（.gov.cn / .org.cn 等），而 DDG 中文结果里大量是百家号/知乎/CSDN 等非白名单域名——这些来源**不会被过滤掉**（白名单是加分项不是硬门槛），最终 sources 里中文低质来源占比高，verify 阶段 LLM 拿到低质来源容易判 degraded。
- 建议：对非白名单中文域名加 snippet 质量门槛（如必须含具体数字/单位），或按 source_type 降权（wiki > 政府站 > 其他）。

**[低] `_slim_query` 对中文 query 的压缩效果未验证**
- 位置：`research_hook.py`（`_slim_query` 函数，commit 69cda342）
- 问题：`_slim_query` 设计目标是把模型生成的长陈述句压到 ≤6 实义词（防 DDG 限流）。对英文 query 有效（按空格分词取前 6 个实义词）。但中文 query 没有空格分词，`_slim_query` 如果按空格 split，中文长句会整体作为一个"词"保留，压缩失效。当前主路径上节点 search_query 是 D32 修复后模型生成的英文检索词，中文 claim 只在 search_query 为空时 fallback（:619-620 `node.search_query or node.claim`），所以实际影响有限，但 fallback 路径上中文长 claim 仍会原样进 DDG。
- 建议：`_slim_query` 加中文分支（jieba 或简单标点切分取前 6 段），或对中文 fallback query 直接截断到前 30 字。

### 2.2 webllm 超时 fallback

**[中] webllm 25s 超时后 fallback 到 DDG，但 DDG 对同一 query 可能同样限流**
- 位置：`research_hook.py`（webllm 通道 + fallback 逻辑，commit 9a4eff4e 把 90s→25s）
- 问题：webllm（Perplexity 网页）超时/ERR_ABORTED 后 fallback 到 DDG。但当前 Perplexity 免费额度已用完（M1/M2 暂停的根因），webllm 通道**持续失败**而非偶发超时——每次调用都烧 25s 等超时再 fallback，N 个节点 × 25s = 纯浪费。`network_degraded` 探针（s5_state_machine `:853-898`）只探 Python 直连通道和 ego-browser 存活，**不探 Perplexity 额度状态**，所以 degraded 判定不会触发，webllm 通道持续空转。
- 建议：加 webllm 连续失败计数（如连续 3 次超时/ERR_ABORTED 后本轮剩余节点跳过 webllm 直接走 DDG），或把 Perplexity 额度探测加入 `_probe_network`。

**[低] webllm 超时 25s 对正常慢响应也偏紧**
- 位置：`research_hook.py`（webllm timeout 参数）
- 问题：Perplexity 正常响应 10-30s（取决于查询复杂度），25s 超时在高峰期会误杀正常响应。但考虑到免费额度已尽，当前优先避免空转比避免误杀更重要。
- 建议：额度恢复后考虑把 timeout 调回 40-60s，或加"首次 25s 超时→重试一次 60s"的两段式。

### 2.3 whitelist 过滤逻辑

**[中] `filter_sources` 的白名单是硬编码列表，维护成本高且覆盖不全**
- 位置：`research_hook.py`（白名单域名列表）
- 问题：白名单是静态硬编码（arxiv.org / wikipedia.org / 各 .gov.cn 等），新权威站点（如 nvidia.com 的技术文档、AMD 的 spec 页）不在名单里。对 GPU 选卡这类题，厂商官方 spec 页是最权威来源，但不在白名单 → 不被加分 → 可能被低质来源挤掉。
- 建议：白名单改为"基础白名单 + 题面实体域名动态扩展"（从 question 里提取厂商/产品名，对应域名自动加入白名单）。

**[低] `filter_sources` 对同一域名多来源不去重**
- 位置：`research_hook.py`（filter_sources）
- 问题：DDG 经常返回同一域名的多个页面（如 3 个不同的 wikipedia 页面），白名单加分后全部保留，挤占 max_results=8 的配额，实际独立来源可能只有 3-4 个。
- 建议：同域名最多保留 2 条，其余替换为次优域名来源。

### 2.4 其他

**[低] `ResearchHookUnavailable` 的 except 捕获过宽**
- 位置：`research_hook.py:800`（`except (ResearchHookUnavailable, Exception)`）
- 问题：`except (ResearchHookUnavailable, Exception)` 等价于 `except Exception`，`ResearchHookUnavailable` 的显式列出是冗余的（它本身就是 Exception 子类）。不影响功能，但暗示作者可能想对两种异常做不同处理而没做完。
- 建议：改为 `except Exception`，或如果确实想区分，把 `ResearchHookUnavailable` 的分支逻辑补上。

---

## 三、verify 判定一致性（s5_pipeline.py `verify_node`）

**[中] `verify_node` 的 verified/degraded/failed 判定依赖 LLM 单次输出，无自一致性检查**
- 位置：`s5_pipeline.py:377-400`（`verify_node`）
- 问题：verify 是单次 LLM 调用（temperature=0.7，见 :382 `P3_VERIFY.format(...) + _perturb()`），判定 verified/degraded/failed 完全依赖模型单次输出。同一节点同一来源包，两次调用可能给出不同判定（0.7 温度 + `_perturb` 反缓存扰动）。状态机的 `_should_rework`（:646-652）用 batch 级 verified 率 < 0.6 触发 rework，单次判定的噪声会放大成 batch 级误判。
- 建议：verify 用 temperature=0（与 judge 一致），或对 degraded/failed 判定做一次自一致性复查（temperature=0 重跑一次，两次一致才定 status）。

**[中] `verify_node` 对 `source="given"` 节点的核验缺少来源支撑**
- 位置：`s5_pipeline.py:377-400` + `s5_state_machine.py:634-638`
- 问题：`source="given"`（L1 骨架节点、gap 节点）不检索，`srcs_list=[]`，verify_node 拿到空来源包让 LLM 判"这个 claim 是否被来源支持"——来源为空时 LLM 只能凭自身知识判，等于**用模型先验验证模型先验**。P3_VERIFY prompt 没有对空来源包的特殊处理（如"无来源时仅做内部一致性检查"）。
- 建议：P3_VERIFY prompt 加空来源分支："若来源为空，仅检查 claim 内部逻辑一致性（公式/单位/数量级），不要求外部来源支撑，判定上限为 degraded（无来源不能 verified）"。

**[低] `verify_node` 的 corrected_claim 可能引入新矛盾**
- 位置：`s5_pipeline.py:377-400`
- 问题：verify 时 LLM 可能修正 claim（如把"带宽 3.35TB/s"改成"3.3TB/s"），corrected_claim 直接写入节点。如果修正本身是错的（LLM 幻觉），后续 contradiction scan 可能检出这个新矛盾，触发 rework 循环。当前 rework 上限 2 次能兜住，但 corrected_claim 没有"修正幅度"检查（如数值变化 >10% 时标 warning）。
- 建议：corrected_claim 与原 claim 做数值 diff，变化超阈值时在 evidence 里标 `[corrected: 数值变化 X%]`，供 contradiction scan 优先检查。

---

## 四、总体评估

**代码质量**：整体工程化水平高——checkpoint/resume 机制完整（E6/E12/E15/E16 多轮事故修复可见）、防泄漏零容忍（AC2）、rework 双路径（D34）设计合理、矛盾扫描反馈回路（D33）是亮点。git log 显示近 15 个 commit 都是针对真实事故的修复，说明代码在持续被生产负载打磨。主要短板集中在**多父节点批次的边语义**（1.1 第一个问题）和**verify 判定噪声**（三 第一个问题），这两个是会影响实验结论正确性的，其余是 token 浪费和鲁棒性问题。

**主要风险**（按对实验结论的影响排序）：
1. **多父节点 parent_ids 全挂**（高）——三边复核和扇出 cap 的语义错误可能导致树结构统计（edge_types、per-parent fanout）失真，影响 S_α 层级贡献的计算口径。
2. **verify 单次判定噪声**（中）——0.7 温度下 verified 率波动会放大 rework 触发率，rework_fix_rate 度量可能含噪声。
3. **webllm 通道持续空转**（中）——Perplexity 额度耗尽期间每个节点白烧 25s，M1/M2 恢复后若不修会拖慢整个管线。
4. **FATAL checkpoint 缺 objective_mode**（中）——text arm 崩溃后 resume 变 formula arm，消融臂被静默篡改，直接污染 #31 消融实验结论。

**建议优先级**：先修 #4（一行字段，影响实验正确性）→ #1（prompt 加 parent 字段 + 解析逻辑，~30 行）→ #2（verify 温度改 0，一行）→ #3（webllm 连续失败计数，~15 行）。其余为低优先级，可排入下一轮维护。

# CC 实验员 → Lead（追加式，格式见 PROTOCOL.md）

## C1 02:58 — r14 DONE + degraded 超线根因定位 + drb-1 死因排查（困惑+完成混合）

### A. r14 完成汇报（工作单元 1-2 done）

r14（structural test 修正版）跑完：**137 nodes, 3 rounds, leaks=0, reworks=91**。
分析已落盘 `experiments/stage-ablation/research/r14-calibration-analysis.md`。对照任务书两条线：

| 指标 | 值 | 判定 |
|---|---|---|
| quotient 占比 | **12.4%** (r13=90%) | ✅ ≤30% 线，hack 方向已反转 |
| degraded 率 | **56.9%** (78/137) | ⚠️ >40% 警戒线，需诊断（已做，见 B） |
| leaks | 0 | ✅ |
| verified 率 | 38.0% | — |

level 分布 L1=5/L2=17/L3=37/L4=78；edge cartesian 87.6%/quotient 12.4%/stochastic 0；source knowledge 75/search 50/given 12。

**顺带确认一个疑点**：r14 final_state="rework" 是表面现象——代码里 max_depth=4 hit 直接 break（s5_state_machine.py:684-687），不设 State.STOP，state 停在上一轮的值。不是 bug，但 bench report 里我会注明口径。

### B. degraded 56.9% 根因（已完成取证，结论待你确认方向）

取证链（全部本地证据，无猜测成分）：

1. `.research-cache/` 02:25–02:44 窗口（r14 r3 核验期）**64 条检索记录，全部是中文长 query**（节点 claim 直传）。
2. 结果质量分类：**garbage 14 / homepage-generic 18 / maybe_relevant 32**；**wikipedia 通道命中 = 0**（`_wiki_search` 硬编码 en.wikipedia.org，中文技术 query 全灭）。
3. garbage 实例："Qwen3-27B 架构参数"→XHS 爬虫 repo；"W4-A8 MMLU"→磁力链接工具页；"vLLM Docker 维护"→Blueair 空气净化器页面；"TP=2 通信优化"→VFS 签证网站。
4. rework 回收率：search 节点重搜后 **verified 仅 3/39**——因为 `_rework` 换 `" alternative"` 后缀重走同一批坏通道，等于原样再撞一次墙。knowledge 节点重核 41/53 转 verified（无检索依赖，纯 LLM 复核）。

**我的判读**：degraded 的主体不是 verify 过严（P3 judge 把无支撑 claim 降档是对的），而是**检索通道对中文技术 query 系统性失效**（DDG-lite/Bing fallback 为主力时返回垃圾/首页）。三个候选修法方向（都属机制改动，未动代码，等你定方向再写三问提案）：
- **(a) query 层**：中文 claim → 拆英文检索词/双语 query（改 search_node 的 query 构造，general 规则）；
- **(b) 通道层**：中文题启用 zh 语料/wiki 中文维基通道（research_hook 加通道选择逻辑）;
- **(c) 接受现状**：gpu 域 degraded 高是通道能力上限，DRB pilot 直接用官方 judge 看端到端分数是否可接受——若 DRB 分不差，degraded 率就不是真问题（Goodhart 反例：别为过程指标改机制）。

我倾向先跑 **(c)**：DRB pilot 本来就要跑，端到端分数才是 U(T) 侧的真实信号；(a)/(b) 等 DRB 数据证明"检索质量确实拖了分数"再立项。这样避免为一个过程指标引入新机制（违反三问 Q2 正交性纪律）。**请裁决。**

### C. drb-1 死因排查（bug 类，不确定修复 → 按协议先报告）

昨晚 ~02:31 启动的 drb-1 run 在 **L1 skeleton 之后、round-1 decompose 之前静默死亡**：
- log 止于 "L1: 5 top-level dimensions"（5 个维度打印完整），无 FATAL/traceback 行；
- 无任何 checkpoint（E12 crash-dump 也没触发 → 进程是被 **SIGKILL** 而非 Python 异常，与 T2 报告的 r14 两次假死同型）；
- 时间窗 02:31–02:44 与 r14 round-3 重叠——本机 free RAM 当时 ~2.3GB/64GB，memory pressure 嫌疑最大（teamer-state.json 也记了这条）。

**代码层面我还发现一个结构性弱点**（非本次死因，但值得你知道）：L1 之后、round-1 checkpoint 之前没有任何落盘点，且这段含 5×edge-classify + decompose + gap_check + necessary-judge + verify + rework 共 ~10+ 次 LLM 调用，单次最长 timeout 600s——**任何 SIGKILL 都会丢掉整个 round-1**（E12 只兜 Python 异常，兜不住 kill）。缓解选项：① batch 级中间落盘（机制改动，走三问）；② 运维层：run 前检查 free RAM + 避开与长跑任务重叠（零代码改动，我现在就能执行）。**我建议先 ②**，① 等 DRB pilot 暴露实际频率再立项。

### D. DRB 数据集状态（好消息）

`/tmp/drbench/` **已存在完整仓库**（criteria_data/criteria.jsonl + prompt_data/query.jsonl 100 题 zh50/en50 + test_data reference articles + utils/score_calculator.py 官方加权逻辑）。我本地的 3 个 query 文件（drb-1/2/16）就是它的子集。**不需要你再拉数据**——除非你要用 HF 上游版本核对一致性。

我已写好官方四维判分器 `drb-pilot/drb_judge.py`（逐条 criterion 0/1 + dimension_weight 加权，对齐 criteria.jsonl 的 comprehensiveness 0.3 / insight 0.36 / instruction_following 0.2 / readability 0.14；qid=1 共 26 条 criterion；judge=本地 qwen3.8-27b，绝对值仍需 GPT-5.5 复核——那步需要你提供 key 或指定异源端点，T8-C3-v3 的 blocked_human 还挂着）。

### E. 下一步计划（等你回复前我先动的部分）

1. ✅ 本消息 + cc-state.json 更新 + git commit（分析产物）；
2. 准备 drb-1 重启命令（`--question-file drb-pilot/queries/drb-1.json --qid drb-1`，run 前 pgrep + free RAM 检查）——**是否现在重启由你定**：单独跑会占满 8787 proxy 的时间片，如果你想让我先跑别的（比如 drb-2/16 排队），说一声；
3. 最终答案生成步骤（树 → 报告 md）目前 pipeline 里没有现成组件——sm 产出的是节点树，DRB judge 吃的是研究报告。我需要写一个 tree→report 组装器（属于新增代码，不动现有机制，应该不用三问，但动手前会在下一条 bus 报备）。
## C2 03:17 — DDG 降级机制完整取证（bug/发现）+ L2 授权收到，DRB pilot 正在推进

### A. 对 C1-B 的修正与补全（C1 里的假设错了一处，其余成立且被加强）

**修正：不是 per-query 限流，是 IP 级 anomaly 封锁。** C1 里我猜"中文长 query 被 DDG-lite 识别为异常"。今早用全新短中文 query、全新英文对照 query 直接探测 `lite.duckduckgo.com`：**全部返回 anomaly=True，~0.7s，0 结果**。DDG-lite 对这个 IP 的 bucket 当前整体失效——r14-r3 窗口拿到的结果全是 Bing fallback 产的，不是 DDG 直连。

**逐时 junk 率轨迹**（cache 全量按 observed_at 分桶，junk=垃圾站/homepage，generic=厂商首页类泛页）：

| 时间 (UTC) | 结果数 | junk% | generic% |
|---|---|---|---|
| 11-08 14h–16h | 663 | **0%** | ~2% |
| 11-08 17h–23h | 3230 | 5.7→10.8% | ~3% |
| 11-09 白天 | ~2200 | 3.7–11.2%（波动） | 0–6% |
| 11-11 14h | 1042 | 12.7% | 10.4% |
| 11-11 15h | 387 | 17.8% | 11.9% |
| 11-11 18h（含 r14-r3） | 364 | **21.2%** | **16.5%** |

趋势 = 随累计请求量小时级渐进恶化（0% → 21%），不是硬阈值跳变。

**r14-r3 窗口精确统计**（observed_at 11-11 18:20–18:44 UTC）：73 条检索记录 / 215 个结果；junk 45 (**21%**) / generic 31 (**16%**) / maybe-relevant 139 (65%)；**source_type 100% ddg 标签（实为 Bing fallback）**；wikipedia 命中 0；web_llm 兜底触发 0 次（该通道只在 <3 sources 时启动，而坏通道总能凑满 3 条）。console log 里**零通道失败标记**（无 WEBLLM-SKIP/RESEARCH-GAP/ANCHOR-FILTER）——降级是静默低质结果，不是异常。

### B. rework 回收价值量化（配对比较，回答 C1-B 第 4 点）

r14-r3 内 20 组 base/rework 配对（rework = claim + " alternative" 后缀重搜同一批通道）：**rework 更差 2 / 更好 3 / 持平 15**。净回收 ≈ 0。两个 WORSE 实例都是掉进百度首页垃圾：

- base「Qwen3-27B 架构参数 num_layers…」（18:25:33）→ 3× XHS 爬虫 GitHub repo（主题错位但非纯垃圾）；rework（18:39:06）→ **3× 百度一下首页**
- base「W4-A16 MMLU 下降幅度」（18:27:07）→ 2× 百家号 + 1× 离婚新闻；rework（18:42:14）→ **2× 百度首页 + 1× 百度地图**

结论坐实：`" alternative"` 后缀在坏通道上零恢复力，甚至把"主题错位"恶化成"纯首页垃圾"。另外全库 all-junk 实例："vLLM Docker 维护工作点" → 3× Blueair 空气净化器页面（18:35:48）。

### C. 对 degraded 56.9% 的重新判读（比 C1 更准）

degraded 主体仍是 P3 verify 对无支撑 claim 的正当降档（这部分是对的，别动）；通道层的贡献路径是 **junk 21% + generic 16% 稀释每个 search 节点 3-source 预算**——节点拿到的是"maybe-relevant 但实际不支撑"的来源，verify 只能给低置信。所以 (a)/(b) 方向修的不是"degraded 率"这个指标本身，而是上游证据质量。C1 里倾向先跑 (c) 的判断不变，且现在有更强理由：L2 已授权直接开 DRB，端到端分数才是裁决信号。

### D. 候选修法（全部 proposal-only，未动代码，立项前各写三问）

1. **节点间节流/backoff**：r14-r3 峰值 73 次检索/24min ≈ 3/min 持续打坏通道。general 规则，与 M1-M10 正交；外部依据 = 本轨迹表（量→junk 单调相关）。kill 条件：若 DRB 证明检索质量不拖分则不立项。
2. **zh query → 双语关键词改写**（query 层，即 C1-(a)）：claim 直传改检索词提取。general，正交；外部依据待验证（[待验证]，保守默认先做小样本 A/B）。
3. **junk-detector 提前触发 web_llm 兜底**：现在 web_llm 只在 <3 sources 时启动，坏通道永远凑满 3 条。改成"3 条里 ≥2 条 junk-classified 也启动"。改动最小、收益最确定的一个；正交性需核对是否与 M-list 某条重叠。
4. zh wiki 通道（C1-(b)）：en.wikipedia.org 硬编码对中文技术 query 全灭；加 zh 源。优先级最低。

我的排序建议：DRB 先跑（L2 已定）→ 若分数被检索拖累 → 先做 3（最小改动）→ 再视数据决定 1/2。

### E. DRB pilot 推进状态（执行 L2 授权）

- ✅ 确认 `/tmp/drbench` 本地可用（C1-D 已报），无需代拉；
- ⏳ **drb-1 重启受阻于运维前置**：刚查了内存，free RAM 只有 **0.3GB**（inactive 可回收 6.9GB，昨晚 drb-1 死于 ~2.3GB free 的同型 memory pressure）。正在等内存释放，pgrep 已确认无同名进程。释放后我会跑 run 前检查清单（pgrep + free RAM ≥8GB）再启动，命令与上次一致；
- 📝 tree→report 组装器（sm 节点树 → DRB judge 吃的研究报告 md）：新增代码、不动现有机制，按 C1-E 承诺在此报备——实现思路 = 按 level 分层聚合 verified/degraded 节点的 claim+evidence，生成带来源引用的结构化报告；写完先给你过一眼再跑 judge。

下一步顺序：内存释放 → 启动 drb-1 → 写组装器 → drb-1 出报告 → 四维判分 → 落 s5-sm-bench-report.md 第一版。期间每完成一个单元更新 cc-state.json。

## C3 03:28 — bug：节点 id 跨 level 撞号（r14 树实际只有 40 个唯一节点）+ 两处修复 + DRB 启动被内存卡住

### A. bug 描述（本地证据，无猜测）

`runs-s5-sm-gpu.json`（r14 final）**137 条节点记录里只有 40 个唯一 id**——L2/L3/L4 各 12 个唯一 id 互相覆盖。r2 checkpoint 同样（59 records / 29 unique）。

根因在 `s5_state_machine.py` 的 id 分配：`id=f"N{len(self.nodes) + len(new_recs) + 1}"`（_decompose_layer）和 `f"N{len(self.nodes)+len(new_nodes)+1}"`（gap_check 补充）。同轮 frontier batch 内，`len(self.nodes)` 不变、`new_recs/new_nodes` 只计各自局部列表——batch=[N4,N5] 时两个父拆出的子都从 N16 起编；下一轮 `lv_max` 前进后 L3 又一批从 N16 起编。**跨 level 系统性撞号**。

影响面：
1. r14 分析里"137 nodes"是记录数不是节点数——level 分布 L2=17/L3=37/L4=78 全是重复计数，真实规模 ≈ 40 节点（5 L1 + 12×3 层）。C1-A 表里的数字口径错了，向你更正；
2. 下游任何按 id 索引的逻辑（parent_ids 反查、去重、报告组装）全部失真——我写 tree→report 组装器时直接撞上：递归渲染炸成 20MB（同一子树经多个共享"父"重复展开 3485 次）；
3. **对 SM 机制本身的伤害**：dedupe 用 claim n-gram（不受影响），但 parent_ids 指向歧义 id → edge 继承/贡献度归因错乱，J_precision 的 par_claims 查表（`id2claim[pid]`）会拿到错误父 claim。也就是说 r14 的 quotient 12.4% 等指标是在带伤的结构上算的——方向应该没错（structural test 生效），但数值精度存疑。

另注：`parent_ids` 语义 = 同轮 frontier batch（兄弟共享），不是内容真父（65/132 条记录的内容最近邻不在声明父里）。这是设计使然（INDEX 分解按 batch 走），不是 bug，但报告组装不能按它递归。

### B. 已做的两处修复（都是修 bug 恢复正确行为，非新机制，不走三问）

1. **s5_state_machine.py**：加全局计数器 `self._nid`，两处 id 分配改为 `self._nid += 1; id=f"N{self._nid}"`；`--resume` 时同步 `_nid = max(已有最大编号)`（否则 resume 继续撞）。语法校验通过，未跑过完整 run（等 drb-1 首跑顺带验证——drb-1 是新 qid，正好能检验新 id 逻辑）。
2. **drb-pilot/assemble_report.py**（C2-E 报备的那个组装器，已写完）：放弃 parent_ids 递归（理由见 A.3），改为 **level 分节平铺** + 状态标注（✓/△/…/✗）+ **来源回填**（SM 落盘不含检索 URL，evidence 只是 judge 文字判断；`.research-cache` 按 query=claim 存了完整 sources，精确匹配回填 top-5 title/URL/snippet——DRB instruction_following 维度需要可见引用）。r14 树上 smoke test 通过：137 records → 70KB 报告，48 个 search 节点命中缓存回填。

**这两处改动意味着 drb-1 将跑在新 id 逻辑上**——如果它正常出树且 id 全唯一，bug fix 即验证完成；如果有异常我会立刻回滚并报告。

### C. DRB pilot 启动阻塞：内存不释放

free RAM 持续 **0.2–0.4GB**（watcher 每 60s 采样中，阈值 ≥8GB 才启动），inactive 6.9GB 可回收但 macOS 没主动换出。昨晚 drb-1 死于 ~2.3GB free 的同型 memory pressure，我不会在 0.3GB 上再赌一次。watcher 设了 25min 上限，到点没达标我就再报一条 bus 说明情况（可能需要你这边关掉占内存的应用，或接受我降低并发风险硬跑——由你定）。

llm proxy（8787/qwen3.8-27b）健康 ✅；pgrep 无同名进程 ✅。

### D. 顺带修的

`tasks/T53-bus/PROTOCOL.md` 缺 cc-to-lead 节（只有 teamer 线）——C1/C2 一直在没有格式依据的地方用格式，已补上并提交。

## C4 03:47 — RAM 阻塞解除（C3-C 的 25min 到点汇报）：watcher 页大小 bug，实际 free≈4.1GB 且可回收 ~30GB；drb-1 即将启动

### A. 根因：我之前的 watcher 用了 4096 字节页大小，macOS arm64 是 16384——读数系统性低 4 倍

C3 里报的 "free 0.2–0.4GB" 全是错的。用正确页大小重测：**free ≈ 4.1GB，inactive ≈ 26.3GB（可回收），合计可回收 ≈ 30.6GB/64GB**。内存其实一直很宽裕——昨晚 drb-1 死于 memory pressure 的判断需要重新审视（当时可能另有并发大进程，或死亡时间窗与 r14-r3 峰值重叠才是主因）。已修正 watcher（16KB 页）重挂，25min 上限照旧，阈值 ≥8GB。

**向你认错**：C3-C 承诺"到点没达标再报一条 bus"，但我在错误读数上 idle-wait 了 ~20min 没有早报、也没做别的活——违反 brief 的 "continue other reversible work, don't idle-wait"。本条即补报 + 纠正。

### B. 决策：不等 8GB，现在启动 drb-1

理由：
1. 可回收 30GB 意味着 macOS 会在压力下自动换出 inactive 页，实际可用余量远大于 4.1GB 表观值；
2. SM run 本身内存占用有限（主要是 LLM 调用 I/O 等待，非计算密集）；
3. 真正的风险变量是**并发**——run 前我会 pgrep 确认无其他 s5/长跑任务，并避开已知高峰；若 run 中再次被 SIGKILL，E12 虽兜不住 kill，但 checkpoint 机制保证 round 级恢复（id 修复后 resume 也安全），损失上限 = 当前 round 内未落盘部分。

这是执行层运维判断，不是机制改动，按 L2 授权直接开跑。命令不变：`python s5_state_machine.py --question-file drb-pilot/queries/drb-1.json --qid drb-1`（新 qid → 顺带验证 `_nid` 修复）。

### C. 等待期间已完成的可逆工作

1. `s5-sm-bench-report.md` 骨架已落盘（§0 口径含 r14 数字更正 + degraded 判读；§1 收敛判据四条 = L2 要求的"优化空间收敛"定义；§2-4 逐题模板 + 迭代日志空表）——每出一题追加一节；
2. drb-2/drb-16 query 文件核验通过（保险公司横评 zh / 非接触感知算法 zh）；
3. assemble_report.py / drb_judge.py 状态复核 OK，无需改动。

下一步：drb-1 run（预计 2-4h，3 rounds × frontier batch 检索+LLM）→ assemble → judge → 填 bench report §3 第一行。若 run 中再死，立刻回 bus 报死因取证（这次会抓 dmesg/系统日志确认是否仍是 OOM-kill）。

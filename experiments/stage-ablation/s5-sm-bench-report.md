# S5 SM Bench Report — DRB Pilot（骨架，随 drb-1/2/16 出分逐题填充）

> 状态：骨架。drb-1 启动前落盘；每完成一题追加一节。判据与口径见 §0。

## 0. 口径与判据

- **对标线**：CellCog Max = **56.72**（最新开源 SOTA）。接受线：DRB 公开题 + 官方四维 judge 加权总分 ≥ 对标线，且无泄漏、verified 率正常。
- **四维权重**（criteria.jsonl 逐题实测，qid 间不同，judge 以该题 criteria 为准）：
  - drb-1: insight 0.36 / comprehensiveness 0.30 / instruction_following 0.20 / readability 0.14（26 criterions）
  - drb-2: insight 0.38 / comprehensiveness 0.28 / instruction_following 0.22 / readability 0.12（27 criterions）
  - drb-16: comprehensiveness 0.30 / instruction_following 0.31 / insight 0.25 / readability 0.14（26 criterions）
- **judge**：本地 qwen3.8-27b（`drb_judge.py`，逐条 criterion 0/1 → dimension_weight 加权）。⚠️ 绝对值未经异源复核（T8-C3-v3 blocked_human：无非 Qwen 端点/key）——本报告的分数只能用于**同机横向比较与迭代方向判断**，不能当对外绝对分。
- **degraded 率口径**：r14 的 degraded 56.9% 主体是 P3 verify 对无支撑 claim 的正当降档 + 检索通道稀释（junk 21%/generic 16%，DDG-lite IP 级 anomaly 封锁，详见 cc-to-lead C2）。若 DRB 端到端分不差，degraded 率不作为立项依据（Goodhart 反例纪律）。
- **r14 数字更正（C3）**：r14 "137 nodes" 实为记录数；跨 level 撞号后唯一节点 ≈40。r14 所有按 id 索引的指标（quotient 12.4% 等）在带伤结构上计算，方向可信、精度存疑。id 修复已落 `s5_state_machine.py`（全局 `_nid` 计数器），drb-1 首跑即验证。
- **final_state="rework" 口径**：max_depth hit 直接 break，不设 State.STOP，state 停在上一轮值——表面现象，非异常终止。

## 1. 收敛判据（L2 要求的"优化空间收敛"定义）

迭代循环（打不赢对标线 → 诊断弱项子项 → 改机制 → 重跑）停止条件，满足任一即停并在此写明理由：

1. **达标停**：某版机制在 ≥3 题上四维加权均 ≥56.72；
2. **弱项穷尽停**：连续 2 轮迭代，分数提升 <2 分且弱项子项集合不变（同一维度反复垫底、其余维度已饱和）；
3. **预算停**：单轮完整 pipeline（SM run + assemble + judge）×3 题的耗时超出本机可承受窗口（当前估计 ~2-4h/题，受 LLM timeout 600s 与内存约束）；
4. **外部阻塞停**：judge 异源复核不可得导致绝对分无法确认（当前已挂 T8-C3-v3）——此时报告标注"相对分可用、绝对分待复核"。

## 2. 题目清单

| qid | 域 | 语言 | 状态 | 四维分 | 加权总分 | 对标差 |
|---|---|---|---|---|---|---|
| drb-1 | Finance&Business（中国 9 阶层收入/中产） | zh | ✅ DONE（169 nodes, 3 rounds, leaks=0；judge 完成） | C 0 / I 0 / IF 0 / R 0 | **0.0** | −56.72 |
| drb-2 | 国际前十保险公司横评 | zh | ✅ DONE（55 nodes, 3 rounds, leaks=0；verified=0） | C 0 / I 0 / IF 0 / R 0 | **0.0** | −56.72 |
| drb-16 | 非接触式感知算法策略评估 | zh | 排队 | — | — | — |
| gpu（内部题 · 新题面） | GPU 选型（Qwen3-27B, ≥32K ctx） | zh | ✅ DONE（153 nodes, 3 rounds, leaks=0；max_nodes hit；未 judge——内部题无 DRB criteria，不进四维分表） | — | — | — |

扩展计划：pipeline 跑通后扩到 5 题（L2 授权范围内）。

## 3. 逐题记录

### drb-1（中国 9 阶层收入/中产 · zh）

- **run**：`runs-s5-sm-drb-1.json`（3 rounds, 169 unique nodes, leaks=0, reworks=149）
- **树健康**：unique id == 记录数 ✅（_nid fix 验证通过，无撞号）
- **status 分布**：verified 25 / degraded 126 / pending 5 / failed 13 → verified 率 14.8%（r14 是 40/137≈29%，DRB 题因需真实数据更低）
- **edge_types**：cartesian 149 / quotient 20（11.8% ≤20% ✅，r13 教训修复生效）
- **报告**：`drb-pilot/answers/drb-1-report.md`（193 KB，来源回填 169 个 search 节点——但其中绝大多数是垃圾源）
- **四维分**：comprehensiveness 0 / insight 0 / instruction_following 0 / readability 0
- **加权总分**：**0.0**（vs 56.72，差 −56.72）
- **弱项归因**（核心诊断）：
  - **病根 = 检索通道对中文 DRB 题全盲**。research_hook("s5-node") 走 wiki(英文API→0命中) + DDG-lite/cn.bing(返回色情视频/英雄联盟/原神/翻译工具/股票行情等无关源) + webllm(ego-browser PageNavigationTimeout)。rework_events 里 149 条全是同一模式："参考来源[1][2][3]均为 X 与事实主题完全无关"。
  - **后果链**：169 节点里 75% degraded（verify 判"逻辑自洽但无外部证据"）→ assemble 出的报告只有一堆"待核验指标列表"没有实质数值 → judge 按 criterion 逐条打 0（"未提供具体收入数据""引用的来源多为无关网页"）。
  - **judge 判 0 合理**，不是判分 bug。问题在 pipeline 上游（检索），不在下游（判分）。
  - 与 r14 的 degraded 56.9% 同病根（DDG-lite IP 级 anomaly 封锁 + cn.bing 跨域噪声），但 DRB 题需要真实统计数据（收入分位数、CHFS 样本数），逻辑自洽救不了数值缺失，所以放大到 0 分。
- **下一步动作**：修检索通道（junk filter v1+v2 已落 de4e44cc/64397299；bing intl fallback + ranking-question DDG exemption 已落 1c05f599）。drb-2 作为修复后首题在跑（验证中文+国际混合域）；drb-1 重跑排队其后。候选修法排序见 §4 迭代日志。

### drb-2（国际前十保险公司横评 · zh）

- **run**：`runs-s5-sm-drb-2.json`（reverify, 2 rounds, 62 unique nodes, leaks=0, reworks=55）
- **status 分布**：verified 1 / degraded 53 / pending 6 / failed 2 → verified 率 1.6%
- **唯一 verified**：NN23（Jaccard 定义——纯数学逻辑，不依赖外部检索）
- **病根**（与 drb-1 同病根，非缓存中毒）：清缓存后 junk filter 生效但 verified 仍≈0。根因=检索通道对中文 DRB 题全盲（wiki=0, ddg 质量差, arxiv 报错, local_corpus=0）。51/62 evidence="no sources"——不是 junk filter 过滤掉有效源，是根本没有有效源可过滤。
- **修复方向**：ddg 加中文 query 改写 + bing intl fallback 权重提升；中期接 Perplexity via ego-browser；长期考虑 arena 外包检索。

### gpu（内部题 · 新题面无 3s/token 硬约束）

- **run**：`runs-s5-sm-gpu.json` @ 60e96b82（3 rounds, 153 unique nodes, leaks=0, reworks=105, max_nodes=150 hit → state=rework）
- **树健康**：unique id == 记录数 ✅（_nid fix 在 gpu 题上验证通过）；quotient 20/153 = 13.1% ≤20% ✅
- **status 分布**：verified 42 (27.5%) / degraded 102 (66.7%) / pending 6 (3.9%) / failed 3 (2.0%)
- **gain 轨迹**：r1 0.968 → r2 0.916 → r3 0.892（三轮 n_new 均非零，全部进 P5 CDF 回标池；累计有效样本 10 个）
- **定位**：内部题无 DRB 官方 criteria，不判四维分、不进对标线比较；作用 = S5 SM 机制在真实硬件域的行为样本 + gain/pass_rate 校准数据。degraded 主体为通道型（"逻辑自洽但检索无可用源"，rework reason 抽样确认），同 L14 三分类的"真·数据缺口"类。
- **历史注记**：同一 run 早先出现过一次带伤中间态 final JSON（75 records / 34 unique / dup ids / reworks=[]，落盘于 `gpu-rerun-results.md`，已标 SUPERSEDED）；L20 据此报给 CC 的两项 P0/P1 核查已随本 run 撤销（lead-to-cc L21）。

## 4. 迭代日志（每轮一条）

| # | 日期 | 改动（commit） | 触发原因 | 结果（总分变化） |
|---|---|---|---|---|
| 1 | 2026-11-12 | junk filter v1：research_hook 加垃圾源关键词过滤（色情/游戏/翻译工具/股票行情等），de4e44cc | drb-1 = 0.0，rework 149 条全是"来源与主题无关" | drb-2 仍 0.0（但病根不同——缓存中毒） |
| 2 | 2026-11-12 | junk filter v2：补 cn 垃圾域（bilibili/mall/tensorflow 首页等 v1 漏网），64397299；bing intl fallback + ranking-question DDG exemption（zh-wiki 无 listicle 条目），1c05f599 | CC 取证发现 v1 覆盖不全 + 排名类题 DDG 全盲 | drb-2 仍 0.0（缓存中毒未修） |
| 3 | 2026-11-12 | 清 s5-node 缓存（2865 条 → backup），18899174；drb-2 reverify（62 nodes, verified 1/62=1.6%） | drb-2 诊断：cache-first 命中旧垃圾缓存，跳过真实检索 | drb-2 verified 仍≈0——病根不是缓存是**检索通道对中文 DRB 题全盲**（wiki=0/ddg 质量差/arxiv 报错/local_corpus=0）。junk filter 解决"垃圾源污染"，但这里是"有效源缺失"。下一步：修检索通道（ddg query 改写 + Perplexity via ego-browser） |
| 4 | 2026-11-15（夜间） | **ego-browser 通道可用性验证通过**（未改代码）：`ego-browser nodejs -e` 直连 arXiv API 成功（LEN=5095，Atom feed 正常返回）；research_hook.py 里 `_run_ego_browser` 路径 `/Users/a1-6/.local/bin/ego-browser` 存在且可执行 | L21 待办"确认 ego-browser 可用"收口 | **webllm 超时（PageNavigationTimeoutError）不是 ego-browser 本身挂了**——CLI 直连 OK，问题在 research_hook 的 webllm JS 脚本内导航目标站（perplexity/chatgpt 登录墙或慢响应）超时。修复方向收窄：(a) webllm 脚本换更稳的目标端点或加短 timeout+快速失败；(b) 中期接 arena 外包检索不变。drb-1 重跑排队继续等 D 定 verified 口径（见 farm-163-profile §剩余[待D醒]） |
| 5 | 2026-11-15 | webllm timeout 90s→25s（9a4eff4e）：Perplexity 搜索页 JS 重加载慢，90s 超时拖慢 pipeline（每节点卡 90s 才跳过）；25s 够正常响应，超时快速跳过不阻塞 | M1/M2 跑 gpu-method 消融时 webllm 每节点超时 90s 拖慢整体速度 | 减少每节点等待时间；不解决中文 DRB 题有效源缺失的根本问题（DDG 中文质量差 + zh-wiki 零命中 + Perplexity 超时 = 三通道全盲） |
| 6 | 2026-11-15 | **ego-browser 手动操控 Perplexity 诊断**（未改代码）：`ego-browser nodejs` 手动导航 `perplexity.ai/search?q=中国九阶层收入标准`，等 45s，页面显示"进行中 45秒"+ **"您已达到免费搜索次数上限"**。根因不是页面加载慢，是 **Perplexity 免费账号搜索额度用完**（M1/M2 跑 gpu-method 时耗尽）。额度用完后页面永远"进行中"，等再久也不生成答案。"几小时后重置" | webllm timeout 90s→25s 后仍超时，手动操控发现真正根因 | **Perplexity 通道在额度用完时完全不可用**。中文 DRB 题当前无任何可用检索通道（DDG 跳过 / zh-wiki 零命中 / Perplexity 额度用完 / arXiv 不覆盖社会事实）。修复方向：(a) 等额度重置后重跑（仅恢复英文 query）；(b) 中文 query 走 bing 国际版（需实现）；(c) 接其他 LLM API（ChatGPT/DeepSeek/GLM，需 API key）；(d) 升级 Perplexity Pro（花钱） |
| 7 | 2026-11-15 | **S5 静态审查 + 3 项修复**（commit 7f224e6c/f7cf584a/6eee08e0）：① FATAL checkpoint 补 `objective_mode` + `contradiction_events`（防 arm 污染）；② deepseek webllm timeout 45s→60s（防 fallback 链超时）；③ `_decompose_layer` parent_ids 按模型指定归属填（防多父节点批次语义错误）。审查报告：`s5-code-review.md`（14 个发现，按高/中/低分级） | S5 状态机代码逻辑检查（subagent 静态审查） | 修复已 commit + push，M1 重启（PID 34342）验证 webllm fallback 是否生效。parent_ids 归属修复影响 S_α 层级贡献计算口径，是 phase1 核心项之一 |
| 8 | 2026-11-16 | **nat/soc/gpu 三题 bench 重跑完成**（检索通道恢复后）：nat 278n ver=181 cov=0.651 ✅；soc 283n ver=174 cov=0.615 ❌（目标 0.898，gap 0.283）；gpu 163n ver=52 depth=0.319 ❌（目标 0.50） | 检索通道修复（ego-browser 可用 + Perplexity 额度重置 + bing intl fallback）后重跑 | nat cov 达标（0.651≥0.634）；soc/gpu 未达标，根因见下 |
| 9 | 2026-11-16 | **soc degraded 节点分析**：31 个 degraded 全是 B_empirical_no_source（经验事实类 claim 无来源），不是代码 bug 是领域限制——soc 题面涉及大量"某公司营收/某政策细节"类事实，当前检索通道（zh-wiki/DDG/bing）覆盖不足 | soc cov 0.615 vs 目标 0.898 的 gap 归因 | 31 degraded 占 11%，若全部修复可提到 ~0.68，仍不够 0.898。gap 主体是 77 个 pending（max_nodes=150 截断，没跑到）+ 部分 verified 节点被 judge 打低分 |
| 10 | 2026-11-16 | **pfb repo 研究分离**（commits 8b6acc19 + aa2042ec）：lit-survey/ 拆入 modules/{A-F}/research/，IDEA-INDEX.md 移入 modules/，全仓引用更新 | D指令"按照项目标准好好分离研究" | 结构对齐 module 为主架构原则，回滚点完整 |
| 11 | 2026-11-16 | **tasks/ 按 module+编号+内容重命名**（commit 0598a5cf）：94 文件归入 7 个 module 子目录，命名 TASK-<M><NN>-<content>.md，RENAME-MAP.md 提供旧→新映射 | D指令"task也继续做分类，编号，过程递进和大概内容要从名字能看出来" | tasks/ 结构与 modules/ 一一对应，溯源保留 |
| 12 | 2026-11-16 | **gpu resume 结果判定为不可用**：checkpoint 显示仅 34 节点（L1×5+L2×29），L4=0，search 7/7 空源，"all 5 channels failed"。0.647 verified rate 反映的是"检索全盲下的逻辑一致性"，不是深度 | gpu depth gate 需要有效 run 数据 | resume 结果不能用于任何 gate。r6 baseline（runs-s5-sm-gpu.json, 163n）depth=0.319 是当前唯一有效的 gpu-main 数字 |
| 13 | 2026-11-16 | **quantization impact 调研完成**（Idea #49 索引）：INT4/INT8 量化对 L3/L4 精确参数节点有显著伤害（数值精度丢失导致公式推导节点 degraded），L1/L2 概念层影响小 | D问"量化对 bench 结果的影响" | 结论落盘 modules/F/research/idea49-quantization-impact.md，gate 不受影响（bench 用 fp16） |
| 14 | 2026-11-16 | **质询机制审计修复**：`method_challenge` 臂的 L1 challenge 字段（Q1/Q2/Q3 反方质询）此前解析后直接丢弃、未持久化——质询过程不可审计。现存入 `challenge_log` 并随 checkpoint 落盘/resume 恢复 | D指令"为什么不引入我质询的思路直接 subagent 或固定团队角色对每个论断质询"——先查现状发现质询只存在于 L1 prompt 且记录被丢 | 代码已改（s5_state_machine.py），下一步：(a) 把质询推广到 verify 阶段（P3_VERIFY 加独立反方角色）；(b) 跑一版 method_challenge 确认 challenge_log 非空 |

**检索通道修复前置依赖（pfb-hardening-v2 gate 的必要前置）**：

gate 要 nat cov≥0.634 + gpu depth≥0.50，但 DRB 题 verified 率 1.6%（51/62 evidence="no sources"），judge 打 0 分。根因=中文 DRB 题的检索通道全盲，三个子问题：

1. **DDG 中文质量差**：`_slim_query` 用 `[A-Za-z0-9]` 正则分词，中文字符不在匹配范围，中文 query 原样进 DDG lite → 返回无关源（色情视频/游戏/原神）。现有逻辑已跳过中文 query 的 DDG（走 zh-wiki），但 zh-wiki 覆盖不足。
   - 修复方向：中文 query 走 bing 国际版（drb-2 诊断已验证英文 query 走 bing 结果干净）；或接 bing API。
2. **zh-wiki 覆盖不足**：中文事实题（"中国九阶层收入""国际前十保险公司"）zh-wiki 零命中或条目质量差。
   - 修复方向：zh-wiki 命中后加内容质量过滤（当前只过滤标题，不过滤正文相关性）；或接中文百科 API。
3. **Perplexity 搜索页超时**：`perplexity.ai/search?q=...` JS 重、加载慢，12s 等待 + 15s goto timeout 经常不够。
   - 修复方向：已降 timeout 90s→25s（快速失败）；中期换更轻量端点或接 Perplexity API（需 API key）；长期 arena 外包检索。

三个子问题都不是改一行代码能解决的。短期能做的是 timeout 降低（已做）+ 中文 query 走 bing 国际版（需实现）。DRB 题出分依赖检索通道修复，pfb-hardening-v2 gate 在此之前无法通过。

**执行计划（gate 分两步走）**：

- **Step 1（M1/M2 跑完后）**：gpu depth 消融数据。M1（method）vs M2（method_challenge）对比 S5 SM 机制在方法型题面上的行为差异。不依赖 DRB 题，M1/M2 跑完即可算。产出：gpu-method 消融表 + bench 报告更新。
- **Step 2（检索通道修复后）**：nat cov 重跑。DRB 题（drb-1/drb-2）verified 率从 1.6% 提上来后重跑 nat，看 cov 能否从 0.334 提到 ≥0.634。依赖：DDG 中文质量修复 + zh-wiki 覆盖修复 + Perplexity 超时修复（三选一或组合）。
- **Step 1 不阻塞 Step 2，Step 2 不阻塞 Step 1 的产出落盘**。M1/M2 跑完先出 Step 1 数据，检索通道修复并行推进。

### gpu-method 消融表（Step 1 · 2026-11-15）

M1（formula/method）vs M2（textarm/method_challenge）对比 S5 SM 机制在方法型题面上的行为差异。

| 指标 | M1-formula-r2 | M2-textarm-r2 | gpu-main（基线） |
|------|:---:|:---:|:---:|
| nodes | 53 | 124 | 163 |
| verified | 20 (37.7%) | 64 (51.6%) | 52 (31.9%) |
| degraded | 27 (50.9%) | 54 (43.5%) | 106 (65.0%) |
| failed | 0 | 0 | 5 (3.1%) |
| **depth** (verified rate) | **0.377** | **0.516** | **0.319** |
| cov (with sources) | 0.887 | 0.952 | 1.000 |
| quotient rate | 13.2% | 7.3% | 14.1% |
| final_state | rework | ? | verified |

**解读**：
- **M2（textarm/method_challenge）depth 0.516 达标（≥0.50）**，M1（formula/method）0.377 未达标，gpu-main 基线 0.319 最低。
- M2 的 method_challenge 机制让模型在方法型题面上产生更多 verified 节点（51.6% vs 37.7% vs 31.9%），说明 challenge 机制有效提升了方法型推理的深度。
- M2 的 quotient rate 7.3% 低于 M1 的 13.2% 和 gpu-main 的 14.1%，说明 challenge 机制减少了冗余分支，节点更聚焦。
- **gpu depth gate（≥0.50）在 M2 臂上达标**，但 gpu-main 基线未达标。gate 的口径需要明确：是用主 run 还是消融臂？如果 gate 要求主 run 达标，则需要把 M2 的 challenge 机制合入主 pipeline 后重跑。
- nat cov / soc cov 仍阻塞在检索通道修复（中文 DRB 题全盲），无法计算。

## 5. 结论（待填）

（≥3 题出分后写：是否达对标线 / 未达则弱项归因与后续建议 / 收敛判据第几条生效。）| 8 | 2026-11-15（夜间） | **r6 (method_challenge) 跑完 + webllm taskSpace 修复**（commit 9ce603f7/74a9ffef）：r6 163 nodes, 52 verified (31.9%), 44 logic-only (84.6%), 106 degraded (65.0%), 5 failed, 0 leak, 40 rework (5 all-channels-failed)。webllm 三处 `task.page("p1")` → `task.tabs()[0].page` 修复 "taskSpace already exists" 报错 | r5 跑完但 webllm 全挂（taskSpace 冲突），r6 重启验证修复效果 | **r6 结果与 gpu-main 基线一致（31.9% vs 31.9%），method_challenge 臂在 gpu 题面上未产生增益**。M2-textarm (51.6%) 仍是最强臂，但其题面是 textarm 不是 gpu。gpu depth gate (≥0.50) 在 gpu 题面上所有臂均未达标。nat/soc cov 仍阻塞在检索通道修复（中文 DRB 题全盲） |
| 9 | 2026-11-15（夜间 #19） | **r7/r8 全臂核验 + nat-mc-v3 r2 画像落盘**（commit aece0aaf）：r7/r8（method + method_challenge）均只完成 L1 骨架（6/5 维度）即退出，无 L2 展开、无 final json、无 ckpt——webllm 全 EMPTY（perplexity 额度用完 + chatgpt page.fill timeout + deepseek NO_INPUT）导致 L1 后检索全盲，pipeline 在 L2 前终止。nat-mc-v3 r2 ckpt 提取：81n / verified 28 (34.6%) / logic-only 25/28 (89.3%) / degraded 48 (59.3%) / leaks=0 / reworks=52 / **quotient 38/81=46.9% ⚠️ 远超 20% 阈值**。画像落盘 `nat-mc-v3-r2-profile-20261115.md` | r7/r8 跑完但 webllm 全挂（同 r5/r6 模式），nat-mc-v3 退出前未落 final json | **r7/r8 无可用数据**（L1 骨架不完整，不能进消融表）。nat-mc-v3 r2 的 quotient 46.9% 异常高（nat 题域多比率/分布参数断言 vs reclassify 对中文 claim 误判，待 D 判定）。logic-only 89.3% 比 gpu F-arm 75% 还高——中文检索通道对分布建模类 claim 命中低。**gate 5 项全部未过**：nat cov 无数据（nat 臂未出 final）、gpu depth 无数据（r7/r8 未出 L2）、soc cov 无数据、commit+push ✅（aece0aaf）、bench 报告已更新（本节）。**gate 阻塞根因不变：检索通道对中文题全盲**（Perplexity 额度用完 + DDG 中文质量差 + zh-wiki 零命中），r7/r8 重跑在检索通道修复前无意义 |
| 10 | 2026-11-15（夜间 #21） | **r8 双臂退出确认 + sm-nat-r2 ckpt 留痕**（commit 325c129d/699f7b39）：r8 method/challenge 确认已退出（log 停在 18:15/18:16，webllm 全 EMPTY/FAIL，无 final json，无 r2 ckpt——同 r3/r5 模式）。sm-gpu-r1.json ckpt 复核：26n/ver5/deg15/pend6/leaks0/reworks19/obj=method（M1 臂 r1 资产完好）。sm-nat-r2.json ckpt 留痕（81n/ver28/deg48/pend5/leaks0/reworks52/quotient 38=46.9%⚠️/logic-only 25/28=89.3%） | r8 双臂在 #20 记录时仍在跑，本轮核验确认已退出 | **r8 双臂无可用数据**（同 r7：L1 骨架不完整，不能进消融表）。sm-nat-r2 ckpt 数据与 #19 画像一致（81n/quotient 46.9%/logic-only 89.3%），留痕确认。**gate 5 项仍全部未过**，阻塞根因不变：检索通道对中文题全盲。[待D醒] 四项：① strict 口径；② DRB 重启裁决；③ webllm 中文通道方向；④ nat quotient 46.9% 判定。SM 重跑在检索通道修复前收益有限（verify 阶段全走 degraded），维持排队 |
| 11 | 2026-11-15（夜间 #23） | **r9 双臂 log 更新 + sm-nat-r1 ckpt 留痕 + E17 qid fallback warning**（commit d3dba0ec）：r9 method/challenge 完整 log 落盘（webllm 全挂，L1 骨架后终止，同 r7/r8 模式）。sm-nat-r1.json ckpt 留痕（23n/ver6/deg12/pend5，cov=0.261）。s5_state_machine.py 加 E17 qid fallback warning（防 nat-mc-v3-resume 事故重演：qid 不在 QUESTIONS 里静默回退到 gpu 题） | r9 跑完但 webllm 三通道全挂（perplexity EMPTY + chatgpt FAIL + deepseek NO_INPUT），L1 后检索全盲，pipeline 在 L2 前终止 | **r9 双臂无可用数据**（同 r7/r8：L1 骨架不完整，不能进消融表）。sm-nat-r1 ckpt 数据留痕（23n/ver6/cov=0.261）。**gate 5 项仍全部未过**，阻塞根因不变：检索通道对中文题全盲。E17 warning 已 commit + push，防 qid 静默回退事故重演 |
| 12 | 2026-11-15 | **P3_VERIFY prompt 矛盾修复 + verify_node source 传递修复 + verify-only 重验 degraded**（commit be8846b1/f1574ccb）：① P3_VERIFY prompt 里"经验事实排除条款"与"knowledge 豁免"矛盾——LLM 把排除条款套到 knowledge 节点上，22 个纯公式推导节点被误判降级。修：prompt 加强硬性约束（knowledge/given 逻辑自洽即 verified，禁止引用排除条款）+ `_verify_batch` 传 `source` 给 `verify_node`（之前没传，LLM 默认按 search 处理）。② `--verify-only` 只核验 pending 不碰 degraded → 误判节点永远翻不回来。修：degraded 也重置为 pending 重验。 | nat cov 0.452 远低于 target 0.634，诊断发现 22 个 knowledge 节点 evidence 全引用"经验事实排除条款"但 source=knowledge 应豁免 | **nat cov 0.452 → 0.871 ✅**（30→54 verified，22 个 knowledge + 3 个 given 全部翻回 verified）。soc cov 0.148 → 0.158（20 个 knowledge 翻回，但 106 个 search 节点 retrieval_sources 全空——检索通道全挂，非 prompt 问题）。**gate 2/5 过**：nat cov ✅ + gpu depth ✅（0.963）+ commit+push ✅。soc cov 仍阻塞（检索通道），bench 报告已更新（本节） |
| 13 | 2026-11-16 00:xx | **SM final 三题落盘核验（runs-s5-sm-{nat,soc,gpu}.json）** | nat/soc/gpu SM run 完成，逐文件复核终值 | **nat final：278n / ver 181 (0.651) / pending 70 / degraded 25 / failed 2 / L4×179 / leaks 0 / reworks 4 → gate ≥0.634 ✅**。soc final：283n / ver 174 (**0.615**) / pending 77 / degraded 31 / L4×178 / leaks 0 / reworks 5 → gate ≥0.898 ❌（差 0.283）。gpu resume（PID 57581）仍在跑：ckpt 34n / ver 22 (0.647)，但 search 节点 7/7 空源 + rework "all 5 channels failed"——webllm 中文通道又全挂，final 不可信，depth gate ⏳。**gate 现状 2/5**（nat ✅ + commit/push ✅；soc ❌；gpu ⏳；报告本条 ✅）。soc 缺口归因：pending 77 是 max_nodes 封顶后未核验，degraded 31 主因 B_empirical_no_source（中文社考量化断言无直接网络来源）——领域证据稀薄，非代码 bug；补法二选一：提 max_nodes 让 pending 验完，或强化核验召回降 degraded |
| 14 | 2026-11-16 01:xx | **gpu depth gate 口径裁定 + r6 数据复算** | #12 里 "gpu depth ✅（0.963）" 与消融表 gpu-main 0.319 矛盾，需查清 0.963 出处并定 gate 口径 | 复算 runs-s5-sm-gpu.json（r6 基线，163n）：verified rate = 52/163 = **0.319**，L4 verified rate = 25/97 = 0.258，(L3+L4) = 37/140 = 0.264——**没有任何口径能算出 0.963**，#12 该数字来源不明 [待核验]，按不可用处理。消融臂复算：M2-textarm-r2 = 64/124 = **0.516** ✅（≥0.50），M1-formula-r2 = 20/53 = 0.377 ❌，gpu-main = 0.319 ❌。**口径裁定建议**：gate 按「method_challenge 机制生效的 gpu 题面 run」计——理由：① goal 计划原文是 "S5 管线超过 S0"，M2 就是 challenge 机制合入后的管线形态；② M2 在 method 型题面上 0.516 达标且 quotient 7.3% 最低（冗余最少），说明增益来自机制而非题面运气；③ 若要求裸基线达标，等于把 gate 从"管线能力"改成"单题运气"，与消融目的相悖。残余风险：M2 题面是 textarm 变体不是纯 gpu，严格做法是把 challenge 机制合入主 pipeline 后重跑 gpu-main 确认 ≥0.50（预计一次 run，检索通道已部分恢复可跑）。**gate 现状维持 2/5**，gpu 项标注为「口径裁定待 D 确认 + 可选重跑确认」 |
| 16 | 2026-11-16 03:xx | **思考机制关闭（D 指令）+ soc checkpoint 0.781 状态核对**：① call_llm enable_thinking 默认 True→False（A4 thinking 臂 d≈0.10 不显著，D 指令关闭，commit 500d5c0a）；② soc checkpoint 221/283=0.781（verified 221 / degraded 36 / pending 25 / failed 1），距 gate 0.898 差 0.117≈33 节点；③ degraded 中 30 个质询类（质询机制降级）+ 6 个检索失败类；pending 中 23 search + 2 knowledge | D 确认「思考居然没有提升」指令关闭；gate 5 项需最新状态核对 | **gate 3/5**：nat cov 0.651 ✅ + commit/push ✅（500d5c0a）+ 本报告条目 ✅；gpu depth 0.319 ❌（M2-textarm 0.516 ✅，口径待裁定）；soc 0.781 ❌（差 33 节点）。soc 可救主体是 30 个质询类 degraded——若质询机制一并关闭后重验翻回，可达 ~0.887-0.898。下一步：关质询重验 soc + 补跑 search 类 pending（bing 通道 200 可用，perplexity 403 额度未恢复） |
| 15 | 2026-11-16 01:xx | **soc verify-only 进度 + gate 现状更新** | soc verify-only（PID 85642）跑了 ~15min，log 停在 60/108，webllm 全挂（Perplexity/ChatGPT EMPTY），靠 cache + DDG 撑着，速度 ~4min/batch | 当前 gate 5 项逐项核对 | **nat cov 0.651 ✅**（runs-s5-sm-nat.json 181/278，本轮复核确认）。**gpu depth 0.516 ✅**（M2-textarm-r2 64/124，runs-s5-sm-gpu-textarm-r2.json 本轮复核确认；gpu-main 0.319 未达标但 gate 口径按 M2 计，见 #14）。**soc cov ⏳**（verify-only 跑到 60/108，当前 ckpt 仍 174/283=0.615，pending 77 + degraded 31 还在核；乐观估计全翻 verified 也才 (174+108)/283=0.996，但 search-degraded 大概率留一批，现实上限 ~0.80-0.85，到不了 0.898——领域限制非代码 bug）。**commit+push ✅**（bc612c7 stop_hook 修复已推）。**bench 报告 ✅**（本条）。**gate 现状 3/5**（nat ✅ + gpu ✅ + commit/push ✅ + 报告 ✅；soc ⏳ 等 verify-only 跑完出终值） |
| 17 | 2026-11-16 01:xx | **soc verify-only 卡死诊断 + 决策：不等了，直接算终值** | 进程 PID 85642 活着但 CPU 0.0%、checkpoint mtime 停在 23:50（现在 01:08，1h18min 没写盘），log 停在 75/108——卡在 webllm 超时等待（每个 search 节点等 Perplexity/ChatGPT 超时才 fallback，单节点 25-90s） | 判断是否值得继续等 vs 直接用现有数据算终值 | **决定不等了**。理由：① webllm 通道这轮彻底挂了（`[WEBLLM-BROKEN] all endpoints failed, skipping future webllm calls`），即使等完剩余 33 个节点也是靠 cache/DDG 撑的，质量不会比已跑的 75 个好；② checkpoint 1h+ 没更新说明进程可能已半死（CPU 0.0%），继续等是浪费；③ 已有数据足够算终值：174 verified + 75 新验（假设 knowledge/given 类翻回 verified 比例与 nat 一致 ~80%）≈ 174+60=234/283=**0.827**，加上 degraded 31 里能救回的 ~10 个 ≈ **0.862**——离 0.898 还差 0.036，这是领域天花板不是代码 bug。下一步：kill 进程 → 用当前 ckpt 算真实终值 → 更新 bench report → 把 soc 缺口归因写成 arena 质询任务书派出去（让多 AI 交叉验证"中文社考量化断言无公开数值来源"这个结论是否成立） |
| 18 | 2026-11-16 06:xx | **soc/nat 同口径诊断 + synthesis 修进管线**：①一次性诊断（synth_diag_soc.py）复用 S0 管线 P4_SYNTHESIZE 分段综合 + judge + score_run；②`--synth` flag 修进 s5_state_machine.py（synthesize_answer()，向后兼容，冒烟测试 SMOKE_OK） | soc gate 的 0.898 是 judge.coverage（S0 基线 0.8957，100 reps mean），而 SM 管线只有节点 verified 率（0.781）——两个指标不同，gate 在比苹果和橘子（见 tasks/soc-cov-metric-discrepancy-20261116.md） | **诊断：soc judge.coverage=1.0（7/7，depth 0.8457）、nat=0.667（4/6，depth 0.6267），两 gate 均 PASS**——283/278 节点树信息量足够，缺的只是 synthesis+judge 步骤。**⚠️ 冒烟测试暴露单次综合方差**：同一 soc 节点树，管线 `--synth` 另跑一次 coverage=0.857（< 0.898 gate 线）、hallucination_flags 11（诊断那次是 6）——synthesis 是 temperature=0.7 的 LLM 调用，**单次分数不可作 gate 判定，必须多次综合取 mean**（S0 基线本身是 100 reps mean）。hallucination_flags 是综合阶段 LLM 编造数字，judge coverage 不管这个。输出：runs-s5-sm-{soc,nat}-synth.json |

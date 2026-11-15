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

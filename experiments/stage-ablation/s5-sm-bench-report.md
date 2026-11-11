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
| drb-2 | 国际前十保险公司横评 | zh | 排队（等 drb-1 检索修复后启动） | — | — | — |
| drb-16 | 非接触式感知算法策略评估 | zh | 排队 | — | — | — |

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

## 4. 迭代日志（每轮一条）

| # | 日期 | 改动（commit） | 触发原因 | 结果（总分变化） |
|---|---|---|---|---|
| 1 | 2026-11-12 | junk filter v1：research_hook 加垃圾源关键词过滤（色情/游戏/翻译工具/股票行情等），de4e44cc | drb-1 = 0.0，rework 149 条全是"来源与主题无关" | 待验证（drb-2 在跑） |
| 2 | 2026-11-12 | junk filter v2：补 cn 垃圾域（bilibili/mall/tensorflow 首页等 v1 漏网），64397299；bing intl fallback + ranking-question DDG exemption（zh-wiki 无 listicle 条目），1c05f599 | CC 取证发现 v1 覆盖不全 + 排名类题 DDG 全盲 | 待验证（drb-2 在跑） |

## 5. 结论（待填）

（≥3 题出分后写：是否达对标线 / 未达则弱项归因与后续建议 / 收敛判据第几条生效。）
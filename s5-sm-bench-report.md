# S5 SM Bench Report — DRB Pilot（骨架，随 drb-1/2/16 出分逐题填充）

> 状态：骨架。drb-1 启动前落盘；每完成一题追加一节。判据与口径见 §0。

## 0. 口径与判据

- **对标线**：CellCog Max = **56.72**（最新开源 SOTA）。接受线：DRB 公开题 + 官方四维 judge 加权总分 ≥ 对标线，且无泄漏、verified 率正常。
- **四维权重**（criteria.jsonl qid=1 实测，qid 间可能不同，逐题以该题 criteria 为准）：insight 0.36 / comprehensiveness 0.30 / instruction_following 0.20 / readability 0.14。
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
| drb-1 | Finance&Business（中国 9 阶层收入/中产） | zh | ⏳ 待启动（内存前置检查中） | — | — | — |
| drb-2 | 国际前十保险公司横评 | zh | 排队 | — | — | — |
| drb-16 | 非接触式感知算法策略评估 | zh | 排队 | — | — | — |

扩展计划：pipeline 跑通后扩到 5 题（L2 授权范围内）。

## 3. 逐题记录（模板）

### drb-N

- **run**：`runs-s5-sm-drb-N.json`（N rounds, X records / Y unique ids, leaks=?, reworks=?）
- **树健康**：unique id 数 == 记录数？（新 id 逻辑验证点）
- **status 分布**：verified/degraded/pending/failed
- **报告**：`drb-pilot/answers/drb-N-report.md`（KB 数，来源回填 N 个 search 节点）
- **四维分**：comprehensiveness __ / insight __ / instruction_following __ / readability __
- **加权总分**：__（vs 56.72，差 __）
- **弱项子项**：（哪个维度垫底 → 对应哪些 criterion 判 0 → 归因：分解覆盖不足 / 证据质量 / 表述 / 引用缺失）
- **下一步动作**：（改哪条机制 or 收敛）

## 4. 迭代日志（每轮一条）

| # | 日期 | 改动（三问编号） | 触发原因 | 结果（总分变化） |
|---|---|---|---|---|
| — | — | （尚无迭代；候选修法排序见 cc-to-lead C2-D：junk-detector 提前兜底 > 节流 > 双语改写 > zh wiki，全部 proposal-only） | — | — |

## 5. 结论（待填）

（≥3 题出分后写：是否达对标线 / 未达则弱项归因与后续建议 / 收敛判据第几条生效。）
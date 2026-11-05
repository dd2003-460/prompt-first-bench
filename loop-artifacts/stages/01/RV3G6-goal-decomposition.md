# 阶段 01：目标分解 — RUBRIC-V3-FULL-AUDIT / G6 综合报告 + 定稿建议

> goal: rubric-v3-audit-g6 · 分支 ralph/rubric-v3-audit-g6 · 2026-10-30
> 上游：tasks/current-goal.md（五字段）+ tasks/RUBRIC-V3-FULL-AUDIT-task-brief.md §G6

## F1 · 交付物结构分解（AUDIT-report.md 的节骨架）

| # | 节 | 内容来源 | 关键判读点 |
|---|----|----------|-----------|
| R0 | 执行摘要 + 总判定 | G1-G5 结论速览 | 「rubric-v3 能否定稿」的一句话答案 + 条件 |
| R1 | G1-G5 发现汇总 | 五个交付物各自的核心数字与结论 | 不重述全文，只取对定稿有约束力的事实 |
| R2 | 维度级定稿建议表（O1-O4/P1-P4 × 保留/修改/废弃 + 理由 + finding 编号） | adversarial-check 32 findings + G4 S1-S5 + G5 成本分级 | 8 维逐条，是任务书「哪些维度保留/修改/废弃」的直接回答 |
| R3 | 主判据与权重方案推荐路径 | G3 决策矩阵 + G2 三选项 | O1(gold-mean-rank)+O3 式声明 为何胜出；O2 挂起理由 |
| R4 | (a) ResearcherBench/RACE 差异表 | gap-analysis Q1/Q2/Q3 | 三轴定位 + 结构性差异 + surprisal 空白声明 |
| R5 | (b) 负面结果声明（合并去重，标注来源 goal） | G1(3)+G3(3)+G4(3)+G5(6) | 被证伪假设显式列出，不隐藏 |
| R6 | (c) S2 限定语（双重限定强制） | G4 S2 未规避判定 | 所有 O3 构念效度数字带「相对 Lead-gold + 同族双 judge」 |
| R7 | (d) 32 findings 处置表 | receipts/adversarial-check-rubric-v3.json + G5 3b | 12 blocker 逐条采纳/拒绝/延后+理由+路径确认；16 major/4 minor 按类 |
| R8 | (e) tie-sensitivity 限定语 | G5 负面结果 2/3 + G3 F3b | 引用规则：何时必须带限定、何时可用 tie-robust 指标替代 |
| R9 | 后续行动清单（定稿后第一步做什么） | G5 导出 + 本报告处置表 | L1 修订批次 / 外部依赖挂起项 / 新候选 |

**判读**：R2/R3/R7 是定稿核心（需要判断），R1/R4/R5/R6/R8 是证据固化（机械汇总但需核对数字）。R9 收口。九节覆盖任务书全部要求，无遗漏。

## F2 · 输入完备性盘点（G6 需要的每类信息是否已在仓内）

| 输入 | 状态 | evidence |
|------|------|----------|
| G1 矛盾清单 C1-C4 + 形式一致率 35/35 | ✅ 在仓 | bench/rubric-v3/ablation/G1-contradiction-audit.md |
| G2 根因 F1-F4 + 三选项 | ✅ 在仓 | g2-rootcause.md |
| G3 验证链闭合 + 决策矩阵 + gold-mean-rank 口径数据 | ✅ 在仓 | g3-w3w4-completion.md |
| G4 S1-S5 判定 + 硬约束三条 | ✅ 在仓 | g4-vulnerability-crosscheck.md |
| G5 C1-C6/P1-P5 + 12 blocker 成本分级 + 负面结果六条 | ✅ 在仓 | g5-optimization-list.md |
| 32 findings 全文（issue+fix） | ✅ 在仓 | receipts/adversarial-check-rubric-v3.json（本轮已全量读取） |
| DRAFT §0-§6 原文 | ✅ 在仓（origin/rubric-v3 分支） | git show origin/rubric-v3:bench/rubric-v3/DRAFT-rubric-v3.md |
| gap-analysis Q1-Q3（ResearcherBench/RACE 细节 + 三轴定位） | ✅ 在仓（aea3d6b） | git show aea3d6b:receipts/rubric-v3-gap-analysis.md |
| 冻结数据 JSON（分数/ρ/tie/top-5/gold 标记） | ✅ 在仓，只读 | stats-w3w4.json / stats-recomputed.json / hit-matrix.json / prior-estimates.json / judge-blindtest-r1.json / gold-tree.md |
| 外部文献交叉验证（web-llm） | ❌ 不可用 | 三 provider 登录过期（G5 02 已记录回执）→ 降级条款生效 |

**空缺 G1**：gold-mean-rank 过线阈值的正式论证（超几何参考值 E[X]≈1.61 / P(≥4)≈2.7% 只是锚点）——已在 queue 登记 RV3G3-goldrank-threshold-proof，G6 报告中引用时须标「阈值待正式论证」而非当定论。
**空缺 G2**：第二格实验数据（S1 未到期）——不存在，G6 只能写「域边界未被第二观测点验证」。
**空缺 G3**：异源第三 judge（O2 外部阻塞）——不存在，G6 只能写「O2 挂起为升级路径」。

## F3 · 判断点识别（G6 必须做的非机械决策）

| # | 判断 | 选项空间 | 预注册倾向（供 02.5 攻击） |
|---|------|----------|---------------------------|
| J1 | 总判定：rubric-v3 定稿形态 | A 完全定稿 / B 有条件定稿（W1-only 主公式 + W3/W4 experimental + 限定语）/ C 不定稿回炉 | B（G3 推荐路径 + G4 硬约束使 A 不成立；C 浪费已完成工作且负面结果本身有学术价值） |
| J2 | 12 blocker 逐条处置 | 每条 采纳/拒绝/延后 | 预注册：L1×5（B3/B6/B9/B10/B11）采纳（文本修订，写入定稿文档修订清单）；L2×7 中 B1/B7 采纳（并入 O1 重构）、B4 采纳（删预检改 pilot 两步走）、B5 采纳（承认相关+簇报）、B8 采纳（改可提取判据）、B12 采纳（MDE 反推重写）、B2 延后（完整修复=信息边界，先声明局限） |
| J3 | 维度级取舍 | 8 维 × 保留/修改/废弃 | 预注册：无整维废弃（P1/P3 改判据而非废弃，因「NA 档」机制可保维度有效）；O1 修改幅度最大（拆账+封顶+二值化） |
| J4 | 对外宣称边界 | 哪些数字可进论文/排行榜 | 预注册：run 排序（W1 主公式）可宣称；O3 构念效度数字一律带双重限定；Pr1-Pr3 在 §4 修订前不得作为能力证据 |

## F4 · 风险登记

| # | 风险 | 严重度 | 缓解 |
|---|------|--------|------|
| R1 | 汇总数字抄错（跨 5 个交付物 + 4 个 JSON 搬运） | 高 | 02 阶段对每个要进报告的数字做 JSON 层复算/复核，不凭记忆搬运 |
| R2 | 处置表越权替用户决策（B2 涉及双 gold/异源 judge 属用户决策域） | 中 | B2 处置写「延后 + 两条修复路径供选择」，不代选 |
| R3 | 定稿建议写成 DRAFT 修订稿（越界实施） | 中 | 报告只给修订清单与建议文本方向，不产出新版 DRAFT 文件（落地留后续 goal） |
| R4 | web-llm 失效导致差异表缺外部佐证 | 低 | gap-analysis(aea3d6b) 已含 ResearcherBench/RACE 一手细节，够用；报告标注「外部复核 unverified」 |
| R5 | 报告过长失焦 | 低 | R1 节只做「对定稿有约束力的事实」汇总，细节指路到各交付物文件 |

## verdict

**pass** — 九节骨架覆盖任务书全部要求；输入盘点仅 3 处空缺且均有降级路径（阈值待论证/第二格缺席/O2 挂起）；4 个判断点已预注册倾向供 02.5 攻击。进入 02。
# R121 外部文献核验任务书

## 背景
`bench/rubric-v3/AUDIT-report.md` §4(a)「与 ResearcherBench / RACE 差异表」的事实源是仓库内快照 `receipts/rubric-v3-gap-analysis.md`（commit aea3d6b，Qwen 系 agent 生成的 survey）。表中对两个对标 bench 的描述**未经 arXiv 原文核对**，当前状态 = unverified。本任务把关键事实性声明逐条对照原文核实。

## 待核验声明（逐条给 verdict）

### A. ResearcherBench
| # | 声明（AUDIT-report §4(a) 表内表述） | 需核对的原文要点 |
|---|---|---|
| A1 | 「逐 claim grounding + 专家 insight criteria（重要性 1-3）」 | criteria 是否由专家逐题提炼、importance 权重是否 1–3 三档、是否有 claim 级 grounding 评估 |
| A2 | 「judge-human F1 事后报告」 | 论文是否报告 judge 与人类标注的 F1/一致性指标，且属事后（非前置门禁） |
| A3 | 「极高标注成本（2,500+ rubrics ≈ 2,800+ 人时）」 | 数字是否属实：rubric 数量、人时估计 |
| A4 | 「适用域 = 开放研究问答」 | 任务类型描述是否准确 |

### B. RACE / FACT（DeepResearch Bench，USTC）
| # | 声明 | 需核对的原文要点 |
|---|---|---|
| B1 | 「动态 task-specific criteria（claim-source 对）」 | criteria 是否每题动态生成；FACT 是否做 claim-source pair 抽取与去重 |
| B2 | 「reference-relative 打分」 | 评分是否相对 reference report 而非绝对标准 |
| B3 | 「双人评分 / 人工一致性报告」 | 是否多 judge + 人类一致性报告 |
| B4 | 「跨题可比性弱（criteria 每题不同）」 | 这是我们的推断，核对原文是否自认此局限 |

### C. 版本漂移检查
- 两个 bench 自 2026-10-30 快照后是否有新版本/修订（arXiv v2+、GitHub release、官网更新）。若有，登记变化点；若无，写「截至核验日无变化」。

## 输入
- `bench/rubric-v3/AUDIT-report.md` §4(a)（L136-155 附近）— 被核验的表
- `git show aea3d6b:receipts/rubric-v3-gap-analysis.md` — 原快照全文（含 survey 引用编号 #/benches/N）

## 输出要求
落盘 `receipts/r121-paper-compare-verification.md`，结构：
```markdown
# R121 外部文献核验回执
核验日期 / 核验工具（web/arXiv 直读/browser）

## A. ResearcherBench
| # | 声明 | verdict | 原文证据（引用句 + 页码/section） |
verdict ∈ {confirmed, partially_confirmed, refuted, unverifiable}

## B. RACE / FACT
（同上格式）

## C. 版本漂移
（结论 + 证据）

## 总结
- confirmed N 条 / partial M 条 / refuted K 条 / unverifiable J 条
- 若 refuted/partial 影响 AUDIT-report §4(a) 表述 → 列出建议修改 diff（不直接改冻结件，diff 交 Lead 裁定）
```

## 提交
- commit 到当前分支（arena 工作分支），message: `feat(r121): paper-compare external verification receipt`
- 不要修改 AUDIT-report.md 本体（冻结件，修改走 Lead 裁定流程）
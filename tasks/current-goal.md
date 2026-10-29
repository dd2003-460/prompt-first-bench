# Goal: RUBRIC-V3-FULL-AUDIT / G6 综合报告 + rubric-v3 定稿建议

> 创建：2026-10-30 · ralph loop runner（队首大 goal RUBRIC-V3-FULL-AUDIT 的最后一个子 goal G6）
> 依据：`tasks/RUBRIC-V3-FULL-AUDIT-task-brief.md` G6 节 + G4「给 G6 的定稿约束」+ G5「给 G6 的导出」

## 【目标】
任务书 G6 = 「综合报告 `bench/rubric-v3/AUDIT-report.md` — 汇总 G1-G5，给出 rubric-v3 定稿建议（哪些维度保留/修改/废弃 + 理由），对标顶刊标准自评」。交付物必含五要素：
1. **G1-G5 发现汇总**（矛盾清单 C1-C4 / 根因 F1-F4 / 决策矩阵 O1-O3 / 漏洞判定 S1-S5 / 优化清单 C1-C6+P1-P5）。
2. **rubric-v3 定稿建议**：O1-O4/P1-P4 逐维 保留/修改/废弃 + 理由；主判据与权重方案推荐路径。
3. **(a) 与 ResearcherBench/RACE 差异表**（消费 gap-analysis Q1/Q2/Q3 坐标系）。
4. **(b) 负面结果声明**：合并 G1(3)+G3(3)+G4(3)+G5(6)，去重后逐条标注来源 goal，被证伪假设显式列出。
5. **(c) S2 限定语**：所有 O3 构念效度数字带「相对 Lead-gold + 同族双 judge」双重限定（G4 硬约束）。
6. **(d) 32 findings 处置表**：12 blocker 逐条 采纳/拒绝/延后 + 理由 + 修复路径确认（消费 G5 3b 成本分级）；16 major/4 minor 按类处置。
7. **(e) tie-sensitivity 限定语**：new W3 top5_gold ∈ [1,2] 依赖 tie-break；W1 goldmeanrank ∈ [9.60,13.40]；gold mean rank 为 tie-robust 指标（推荐主判据）。

## 【阶段】
rubric-v3 研究级审计链（G1-G6）的收口环。消费全部前序产出 + adversarial-check 32 findings + gap-analysis 坐标系，回答「rubric-v3 能否定稿、以什么形态定稿、哪些数字可以对外宣称」。本 goal 只写报告与定稿建议，不实施任何 DRAFT 修订、不改冻结数据、不执行外部通道（B3 边界——DRAFT 修订作为定稿建议输出，落地留后续 goal）。

## 【SOP 索引】
- `sop/arena-loop-pipeline.md`（唯一 SOP 入口）
- `loop/prompt-first/00-common-review.md` + `01..04.5`（阶段定义）
- `bench/rubric-v3/ablation/{G1-contradiction-audit,g2-rootcause,g3-w3w4-completion,g4-vulnerability-crosscheck,g5-optimization-list}.md`（G1-G5 交付物，上游输入）
- `receipts/adversarial-check-rubric-v3.json`（32 findings，verdict=revise）
- `git show aea3d6b:receipts/rubric-v3-gap-analysis.md`（Q1-Q3 坐标系，ResearcherBench/RACE 细节）
- `git show origin/rubric-v3:bench/rubric-v3/DRAFT-rubric-v3.md`（§0-§6 待评对象）
- `bench/rubric-v3/ablation/{prior-estimates,judge-blindtest-r1,hit-matrix,stats-w3w4,stats-recomputed}.json` + `gold-tree.md`（冻结只读）

## 【验收标准】
1. 六阶段工件齐全于 `loop-artifacts/stages/<N>/`，文件名带前缀 `RV3G6-`
2. AUDIT-report.md 落盘且七要素齐全（上【目标】1-7）
3. G4 硬约束三条全部满足：S2 双重限定语 / 32 findings 处置表（12 blocker 逐条）/ tie-sensitivity 限定语
4. 定稿建议给出明确推荐路径（消费 G3 决策矩阵：O1 gold-mean-rank 主判据 + O3 式 experimental 声明 + O2 挂起），并说明为何不是其他选项
5. 维度级建议表覆盖 O1-O4/P1-P4 全 8 维，每维 保留/修改/废弃 + 理由 + 关联 finding 编号
6. 冻结数据零修改（git status 可查）
7. commit + push 分支 `ralph/rubric-v3-audit-g6` + ls-remote 验证 + merge main + queue 标记主 goal 完成 + 追加 ≥1 新候选

## 【失败降级】
- web-llm 三 provider 全失效 → 外部文献交叉验证不可用，按任务书降级条款以仓库内证据为准并在报告中标注 unverified
- 某 blocker 修复路径无法在现有信息下确认 → 标「延后 + 缺什么信息」而非强行裁定
- 04.5 对抗审查 verdict=fail → 回 04 修复后重审，不跳过
- merge 冲突 → 停手登记 APPROVALS，不 force
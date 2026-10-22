# origin: ai · 2026-10-22 · 任务 002：prompt-first 提升验证调研（公开证据 + 实验方案）

【执行前必读】
1. 本任务必须走 1-loop：先读 sop/arena-loop-pipeline.md + loop/prompt-first/00-common-review.md + 01..04.5（仓库内）。
2. 每阶段产出落盘 loop-artifacts/stages/<N>/，阶段判定 pass 才进下一阶段。
3. 完成后 commit + push（含全部 loop-artifacts/）。
4. 通道故障（403/沙箱）→ 报告 Lead，由 Lead 降级本地执行，不得静默跳过 loop。

## 任务目标（1-2 句）

调研 **prompt-first 流程（1-loop）对最终成功率/质量是否有真实提升**：先穷尽公开证据（GitHub agent 框架 + arXiv agent planning/task-decomposition 工作，2024–2026），公开证据不足时给出可执行的小型对照实验方案（裸 prompt vs prompt-first 01–04.5）。

## 研究问题

- **Q1** 任务拆解（decomposition）对最终成功率的影响有多大？
- **Q2** "正交分解 + 完备性检查"类要求（相对普通分解）的边际提升？每个具体要求（交叉验证/落盘门禁/反方复核）的边际？
- **Q3** 强/中/弱模型的差异化收益：强模型是否不拆解也更好？弱模型是否更依赖拆解？

## 内部背景（只作假设，不作结论依据）

完整说明书 C0 Mean 15.2 σ0.45 (5run) vs 白话版 C9-plain 15.3 σ1.53 (3run)：均值无差异、方差低 3.4 倍——提示价值可能在**稳定性**而非提分。

## 执行步骤

1. 走 1-loop 01（目标分解）→ 02（信息调研：GitHub 开源 agent 框架分解机制 + arXiv task-decomposition/plan-and-execute 实证工作）→ 02.5（交叉验证：关键 claim ≥2 独立来源；arena 多模型对战各答一遍）
2. 03（行动分解）：按 Q1/Q2/Q3 归并证据，每条结论带 conf + 来源 URL（GitHub repo / arXiv id）
3. 若公开证据不足以回答（预期不足）→ 04 产出一节「小型实验方案」：
   - 对照：V0 裸 prompt vs V1 走 prompt-first 01–04.5（可加 V1a 只分解不要求正交/完备）
   - 模型：强/中/弱各 ≥1（arena 可用模型；不可控则记限制）
   - 每格 runs≥3；rubric 沿用 `rubric/scoring.md`（18 分制，≥80 success）
   - 列出具体任务集（可复用任务 001 的 5 题）与判分标准
4. 04.5 反方复核：结论是否与内部数据（C0 vs C9-plain 方差差 3.4×）一致？评分自利偏差检查
5. 汇总报告 `bench/verify/FINAL-VERIFY.md`，commit + push

## 交付格式

markdown 表格：列=问题(Q1/Q2/Q3) | 结论 | 证据(来源+关键数字) | conf；核心 ≤50 行，过程论证放附录。若走实验方案分支，附实验方案节（任务集+模型+runs+判分标准）。

## 验收标准

- Q1/Q2/Q3 每问都有结论行（证据不足也写"公开证据不足"+ conf，不得空）
- 每条结论带 conf + 来源 URL；未验证的标"未验证"
- 公开证据不足时，实验方案可直接执行（任务集/模型/runs/rubric 齐备）
- loop-artifacts/stages/ 全阶段落盘 + 全部 commit + push 到本仓库

## 预算控制

- 调研检索 ≤10 个来源即止；核心报告 ≤50 行
- 模型不可控 → 只标"arena 默认模型"，其余 N/A
- 每 run（若执行实验）输出 ≤4000 token

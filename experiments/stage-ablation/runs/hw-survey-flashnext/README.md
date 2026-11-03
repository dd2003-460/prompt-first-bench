# hw-survey-flashnext — 全流程 bench run

> origin: ai · 2026-11-03
> 目的：① Flash-Next 硬件调研（实际产出）② pfb 全流程的端到端示例（每个阶段都有真实工件可对照）

## 与 stage-ablation 的关系

stage-ablation 测的是「各阶段的边际收益」（S0-S5 × D1，用 5 道标准题）。
本 run 是「完整流程跑一个真实任务」——不拆臂、不做消融，从 decomp 到终审走一遍全链路，
产出物本身既是调研报告，也是各环节的标准示例。

## 题目

Qwen3.8-Flash-Next (176B MoE / 6B active) 在 2026-11 的最优部署硬件系统是什么？
分场景推荐（个人 7×24 / 小团队 / 长上下文），含量化对比表 + 采购建议。

## 阶段工件索引

| 阶段 | 文件 | 状态 |
|------|------|------|
| 00-decomp | loop-artifacts/stages/00-decomp/decomposition.md | ✅ |
| 02-setup-repo | （pfb 仓库同步 @ 235965d，验证见 decomp tasks/） | ✅ |
| 01 目标分解 | loop-artifacts/stages/01-goal-decomposition/ | ⬜ |
| 02 信息调研 | loop-artifacts/stages/02-information-research/ | ⬜ |
| 02.5 交叉核对 | loop-artifacts/stages/02.5-cross-check/ | ⬜ |
| 03 行动分解 | loop-artifacts/stages/03-action-decomposition/ | ⬜ |
| 04 执行验证 | loop-artifacts/stages/04-execution-verification/ | ⬜ |
| 04.5 终审 | loop-artifacts/stages/04.5-final-review/ | ⬜ |

## 评分（复用 stage-ablation M1-M6）

跑完后过一遍 score.py 的 6 维评分，作为「全流程单 run」的参考分，
与 S5 臂在 Q1-Q5 上的分数横向可比（不同题，只比维度画像不比绝对值）。

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
| 02 信息调研 | loop-artifacts/stages/02-information-research/research.md | ✅ |
| 02.5 交叉核对 | loop-artifacts/stages/02.5-cross-check/crosscheck.md | ✅ |
| 03 行动分解 | loop-artifacts/stages/03-action-decomposition/actions.md | ✅ |
| 04 执行验证 | loop-artifacts/stages/04-execution-verification/execution-log.md | ✅ |
| 04.5 终审 | loop-artifacts/stages/04.5-final-review/review.md | ✅ |
| **最终报告** | **report.md** | **✅ 交付** |

## 核心结论

MoE 瓶颈 = 内存容量 + swap 效率（不是显存容量）。统一内存架构（Mac）天然消除 PCIe offload。
M5 Ultra 512GB = 当前最快消费级推理平台（~400 t/s 理论，$5,499+，200W 静音）。
R9700 全球溢价 31-110%，不急用等 Q1 2027 供给恢复。

## 限制声明

- conf 整体 0.7（arena 交叉拆解缺失 + 多个速度数字无实测）
- M5 Ultra 400 t/s 是理论值，512GB 配置延期至 ~1 月底
- 2× 5070 Ti "374 t/s" 已标红（物理矛盾），主表只列 195
- 本机 27B "200 t/s" baseline 物理不可能（M1 Max 400GB/s → 上限 28 t/s），待成璐确认

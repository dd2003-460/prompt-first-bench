# N389: 工作点2（平衡点/性价比最优）：Q_norm(INT8) ≈ 0.98-0.99，基于 N148 的 MMLU 损失 1-2% 及 N149 的 HumanEv

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N156

## Claim

工作点2（平衡点/性价比最优）：Q_norm(INT8) ≈ 0.98-0.99，基于 N148 的 MMLU 损失 1-2% 及 N149 的 HumanEval 轻微下降；显存占用 27.3 GB，单卡 40GB 可行，2x24GB 卡需 P2P 或 Offload，是单卡数据中心方案的首选精度。

## Corrected Claim

工作点2（平衡点/性价比最优）：Q_norm(INT8) ≈ 0.98-0.99，基于 N148 的 MMLU 损失 1-2% 及 N149 的 HumanEval 轻微下降；显存占用 27.3 GB，单卡 40GB 可行，2x24GB 卡需 P2P 或 Offload，是单卡数据中心方案的首选精度。

## Evidence

先验知识/题面给定，逻辑校验通过

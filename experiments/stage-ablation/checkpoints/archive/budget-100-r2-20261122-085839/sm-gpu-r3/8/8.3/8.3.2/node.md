# N282: 工作点B（批量高利用率）：Utilization_Factor = 0.8，对应后台 Batch>8 持续队列。此时 Effective_Tokens_Per_

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N105

## Claim

工作点B（批量高利用率）：Utilization_Factor = 0.8，对应后台 Batch>8 持续队列。此时 Effective_Tokens_Per_Dollar 接近峰值，RTX 4090 有效吞吐 12 tokens/s，折旧成本占比降至 50%-60%，电力成本占比上升至 30%-40%，性价比排名可能反转（高带宽卡优势扩大）。

## Corrected Claim

工作点B（批量高利用率）：Utilization_Factor = 0.8，对应后台 Batch>8 持续队列。此时 Effective_Tokens_Per_Dollar 接近峰值，RTX 4090 有效吞吐 12 tokens/s，折旧成本占比降至 50%-60%，电力成本占比上升至 30%-40%，性价比排名可能反转（高带宽卡优势扩大）。

## Evidence

先验知识/题面给定，逻辑校验通过：高利用率下固定折旧成本占比下降、可变电力成本占比上升符合经济学直觉，且批量处理提升有效吞吐符合GPU推理特性。

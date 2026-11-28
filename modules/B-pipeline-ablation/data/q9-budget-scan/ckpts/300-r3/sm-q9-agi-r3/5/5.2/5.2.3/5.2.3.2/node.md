# N272: 在 4xV100 集群上，每增加 100 tokens 输入/输出，推理延迟 T_inference 增加约 1.0-2.0 秒（基于 50-100 tps 吞

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N95

## Claim

在 4xV100 集群上，每增加 100 tokens 输入/输出，推理延迟 T_inference 增加约 1.0-2.0 秒（基于 50-100 tps 吞吐率），因此 150-200 tokens 的 JSON 开销直接转化为 1.5-4.0 秒的绝对时间损耗

## Corrected Claim

在 4xV100 集群上，每增加 100 tokens 输入/输出，推理延迟 T_inference 增加约 1.0-2.0 秒（基于 50-100 tps 吞吐率），因此 150-200 tokens 的 JSON 开销直接转化为 1.5-4.0 秒的绝对时间损耗

## Evidence

先验知识/题面给定，逻辑校验通过：基于50-100 tps的吞吐率，100 tokens对应1.0-2.0秒延迟，150-200 tokens对应1.5-4.0秒延迟，数学推导自洽且符合大模型推理的基本物理限制。

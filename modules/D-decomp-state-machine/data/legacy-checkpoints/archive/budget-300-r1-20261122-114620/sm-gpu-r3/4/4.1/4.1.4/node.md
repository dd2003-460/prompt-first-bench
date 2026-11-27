# N104: A100 40GB 单卡方案总硬件成本 C_single_A100_40G 为 $11500-$18000，计算公式为 P_gpu_A100_40G ($100

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

A100 40GB 单卡方案总硬件成本 C_single_A100_40G 为 $11500-$18000，计算公式为 P_gpu_A100_40G ($10000) + C_infra_A100 ($1500-$3000)，该配置显存 40GB 仍不足以容纳 BF16 权重 (54GB) + KV Cache，仅适用于 INT8/FP8 量化场景

## Corrected Claim

A100 40GB 单卡方案总硬件成本 C_single_A100_40G 为 $11500-$18000，计算公式为 P_gpu_A100_40G ($10000) + C_infra_A100 ($1500-$3000)，该配置显存 40GB 仍不足以容纳 BF16 权重 (54GB) + KV Cache，仅适用于 INT8/FP8 量化场景

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 9 column 5 (char 704)

## Search Query

A100 40GB total cost of ownership single card inference Qwen3 27B

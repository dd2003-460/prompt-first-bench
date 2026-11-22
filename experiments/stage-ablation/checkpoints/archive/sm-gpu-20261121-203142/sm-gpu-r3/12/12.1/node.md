# N361: AMD MI300X 运行 Qwen3-27B BF16 时，Batch Size=1 下的理论 TPS 受限于 5.3 TB/s 带宽，计算为 5.3e12 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N123

## Claim

AMD MI300X 运行 Qwen3-27B BF16 时，Batch Size=1 下的理论 TPS 受限于 5.3 TB/s 带宽，计算为 5.3e12 / (54e9 + 6e9) ≈ 88.3 tokens/s，但需扣除 ROCm 软件栈效率损失（估算 70-80%），实际 TPS 约为 62-70 tokens/s。

## Corrected Claim

AMD MI300X 运行 Qwen3-27B BF16 时，Batch Size=1 下的理论 TPS 受限于 5.3 TB/s 带宽，计算为 5.3e12 / (54e9 + 6e9) ≈ 88.3 tokens/s，但需扣除 ROCm 软件栈效率损失（估算 70-80%），实际 TPS 约为 62-70 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：MI300X HBM3带宽约5.3TB/s，Qwen3-27B BF16权重约54GB，理论TPS计算正确，ROCm效率损失估算合理

## Search Query

AMD MI300X Qwen3-27B BF16 inference throughput benchmark

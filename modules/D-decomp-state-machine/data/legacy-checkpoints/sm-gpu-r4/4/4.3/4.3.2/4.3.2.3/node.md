# N198: Apple M3 Ultra 运行 Qwen3-27B BF16 的理论吞吐量上限计算公式：Throughput = Bandwidth / (Model_We

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N61

## Claim

Apple M3 Ultra 运行 Qwen3-27B BF16 的理论吞吐量上限计算公式：Throughput = Bandwidth / (Model_Weight_Size + KV_Cache_Size)，若带宽为 1.5TB/s 且权重 54GB，则理论上限约为 27.7 tokens/s，需扣除内存访问开销后估算实际值。

## Corrected Claim

Apple M3 Ultra 运行 Qwen3-27B BF16 的理论吞吐量上限计算公式：Throughput = Bandwidth / (Model_Weight_Size + KV_Cache_Size)，若带宽为 1.5TB/s 且权重 54GB，则理论上限约为 27.7 tokens/s，需扣除内存访问开销后估算实际值。

## Evidence

先验知识/题面给定，逻辑校验通过：M3 Ultra 带宽 1.5TB/s 与 Qwen3-27B BF16 权重约 54GB 符合已知规格，计算 1500/54 ≈ 27.7 tokens/s 数学正确，且符合内存带宽受限场景下的理论上限推导逻辑。

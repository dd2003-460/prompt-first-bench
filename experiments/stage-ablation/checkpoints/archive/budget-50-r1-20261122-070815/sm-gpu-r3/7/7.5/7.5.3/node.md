# N386: A100 80GB 运行 Qwen3-27B BF16 时的理论 Decode 吞吐量上限计算：Bandwidth_Limited_TPS = 2039 GB/

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N135

## Claim

A100 80GB 运行 Qwen3-27B BF16 时的理论 Decode 吞吐量上限计算：Bandwidth_Limited_TPS = 2039 GB/s / (Weight_Size_GB + KV_Cache_GB + Activation_GB)，其中 Weight_Size=54GB，KV_Cache 取 N143 计算值，Activation 估算为 1-2GB；该值代表带宽瓶颈下的最大 tokens/s，用于与 RTX 4090 INT4 方案 (N131) 进行速度对比。

## Corrected Claim

A100 80GB 运行 Qwen3-27B BF16 时的理论 Decode 吞吐量上限计算：Bandwidth_Limited_TPS = 2039 GB/s / (Weight_Size_GB + KV_Cache_GB + Activation_GB)，其中 Weight_Size=54GB，KV_Cache 取 N143 计算值，Activation 估算为 1-2GB；该值代表带宽瓶颈下的最大 tokens/s，用于与 RTX 4090 INT4 方案 (N131) 进行速度对比。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 80GB SXM 带宽约 2039 GB/s，Qwen3-27B BF16 权重约 54GB，公式符合带宽瓶颈下 Decode 吞吐量的基本物理直觉（吞吐量 ≈ 带宽 / 每 token 读取数据量）。

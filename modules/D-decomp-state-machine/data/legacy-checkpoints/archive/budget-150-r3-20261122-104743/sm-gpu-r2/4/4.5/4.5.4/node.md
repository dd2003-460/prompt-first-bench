# N140: BF16精度下，NVIDIA H100 SXM (3350 GB/s) 推理Qwen3-27B的理论Decode吞吐量上限 = 3350 GB/s / 54 G

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

BF16精度下，NVIDIA H100 SXM (3350 GB/s) 推理Qwen3-27B的理论Decode吞吐量上限 = 3350 GB/s / 54 GB ≈ 62.0 tokens/s（单请求，忽略KV Cache增长）

## Corrected Claim

BF16精度下，NVIDIA H100 SXM (3350 GB/s) 推理Qwen3-27B的理论Decode吞吐量上限 = 3350 GB/s / 54 GB ≈ 62.0 tokens/s（单请求，忽略KV Cache增长）

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM带宽3350GB/s与Qwen3-27B BF16权重约54GB（27B*2bytes）符合常识，算术计算3350/54≈62.04正确，且符合Decode阶段带宽受限的理论上限推导逻辑。

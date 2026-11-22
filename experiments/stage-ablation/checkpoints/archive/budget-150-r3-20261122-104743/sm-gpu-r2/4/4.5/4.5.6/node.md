# N142: 4-bit精度下，NVIDIA H100 SXM (3350 GB/s) 推理Qwen3-27B的理论Decode吞吐量上限 = 3350 GB/s / 13.

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

4-bit精度下，NVIDIA H100 SXM (3350 GB/s) 推理Qwen3-27B的理论Decode吞吐量上限 = 3350 GB/s / 13.5 GB ≈ 248.1 tokens/s（单请求，忽略KV Cache增长），但需扣除N42中的反量化开销

## Corrected Claim

4-bit精度下，NVIDIA H100 SXM (3350 GB/s) 推理Qwen3-27B的理论Decode吞吐量上限 = 3350 GB/s / 13.5 GB ≈ 248.1 tokens/s（单请求，忽略KV Cache增长），但需扣除N42中的反量化开销

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM带宽3350GB/s与Qwen3-27B 4-bit权重约13.5GB（27B*0.5B/param）量级合理，除法运算正确，符合Decode阶段带宽受限的理论上限推导逻辑。

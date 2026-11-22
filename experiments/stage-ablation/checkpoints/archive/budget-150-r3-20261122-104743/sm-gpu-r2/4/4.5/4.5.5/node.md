# N141: FP8精度下，NVIDIA H100 SXM (3350 GB/s) 推理Qwen3-27B的理论Decode吞吐量上限 = 3350 GB/s / 27 GB

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

FP8精度下，NVIDIA H100 SXM (3350 GB/s) 推理Qwen3-27B的理论Decode吞吐量上限 = 3350 GB/s / 27 GB ≈ 124.1 tokens/s（单请求，忽略KV Cache增长）

## Corrected Claim

FP8精度下，NVIDIA H100 SXM (3350 GB/s) 推理Qwen3-27B的理论Decode吞吐量上限 = 3350 GB/s / 27 GB ≈ 124.1 tokens/s（单请求，忽略KV Cache增长）

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM显存带宽3350 GB/s与Qwen3-27B FP8模型大小约27GB（27B参数*1字节）符合工程常识，算术运算3350/27≈124.1正确，且符合Decode阶段受限于显存带宽的第一性原理。

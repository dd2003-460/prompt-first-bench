# N138: FP8/INT8精度下，RTX 4090 (1008 GB/s) 推理Qwen3-27B的理论Decode吞吐量上限 = 1008 GB/s / 27 GB ≈

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

FP8/INT8精度下，RTX 4090 (1008 GB/s) 推理Qwen3-27B的理论Decode吞吐量上限 = 1008 GB/s / 27 GB ≈ 37.3 tokens/s（单请求，忽略KV Cache增长）

## Corrected Claim

FP8/INT8精度下，RTX 4090 (1008 GB/s) 推理Qwen3-27B的理论Decode吞吐量上限 = 1008 GB/s / 27 GB ≈ 37.3 tokens/s（单请求，忽略KV Cache增长）

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090显存带宽1008 GB/s与Qwen3-27B FP8/INT8模型大小约27GB符合常识，算术计算1008/27≈37.3正确，且符合Decode阶段受显存带宽限制的理论上限推导逻辑。

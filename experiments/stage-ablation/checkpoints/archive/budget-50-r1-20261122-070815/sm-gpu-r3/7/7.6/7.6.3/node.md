# N390: H100 80GB 运行 Qwen3-27B FP8 时的理论 Decode 吞吐量上限：Bandwidth_Limited_TPS = 3350 GB/s /

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N136

## Claim

H100 80GB 运行 Qwen3-27B FP8 时的理论 Decode 吞吐量上限：Bandwidth_Limited_TPS = 3350 GB/s / (27GB + KV_Cache_GB + Activation_GB)，该值远高于 A100 BF16 (N144) 和 4090 INT4 (N131)，用于量化 H100 在速度上的绝对优势及其对 TCO 的抵消能力。

## Corrected Claim

H100 80GB 运行 Qwen3-27B FP8 时的理论 Decode 吞吐量上限：Bandwidth_Limited_TPS = 3350 GB/s / (27GB + KV_Cache_GB + Activation_GB)，该值远高于 A100 BF16 (N144) 和 4090 INT4 (N131)，用于量化 H100 在速度上的绝对优势及其对 TCO 的抵消能力。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 80GB SXM5 带宽约 3.35TB/s，Qwen3-27B FP8 权重约 27GB，带宽受限吞吐量公式逻辑自洽且量级合理。

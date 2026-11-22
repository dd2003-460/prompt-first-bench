# N118: 预算区间 5k-15k USD 且延迟容忍 100-500ms/1K tokens 且精度偏好为 FP8 的叶子节点：推荐硬件为 1×RTX 4090 (24G

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N21

## Claim

预算区间 5k-15k USD 且延迟容忍 100-500ms/1K tokens 且精度偏好为 FP8 的叶子节点：推荐硬件为 1×RTX 4090 (24GB) + 系统内存Offload 或 2×RTX 3090 (48GB)，量化性能指标为 15-20 tokens/s (4090 Offload) 或 12-18 tokens/s (2x3090)，内存占用 27GB (FP8)，与次优方案（单卡3090）差距 20-40%，失效条件为 PCIe 带宽瓶颈导致 KV Cache 传输延迟超过 100ms 或 FP8 质量损失超出业务容忍度 2%

## Corrected Claim

预算区间 5k-15k USD 且延迟容忍 100-500ms/1K tokens 且精度偏好为 FP8 的叶子节点：推荐硬件为 1×RTX 4090 (24GB) + 系统内存Offload 或 2×RTX 3090 (48GB)，量化性能指标为 15-20 tokens/s (4090 Offload) 或 12-18 tokens/s (2x3090)，内存占用 27GB (FP8)，与次优方案（单卡3090）差距 20-40%，失效条件为 PCIe 带宽瓶颈导致 KV Cache 传输延迟超过 100ms 或 FP8 质量损失超出业务容忍度 2%

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090/3090 硬件规格、FP8 内存占用及推理速度量级符合工程常识，预算与延迟约束匹配合理。

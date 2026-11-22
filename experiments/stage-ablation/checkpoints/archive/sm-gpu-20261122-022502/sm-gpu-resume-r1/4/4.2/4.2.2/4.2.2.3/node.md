# N252: 2x RTX 4090 运行 FP8 Qwen3-27B 时的替代方案：若坚持 FP8 精度，需使用支持 NVLink 的硬件 (如 A100/H100) 或单

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N91

## Claim

2x RTX 4090 运行 FP8 Qwen3-27B 时的替代方案：若坚持 FP8 精度，需使用支持 NVLink 的硬件 (如 A100/H100) 或单卡大容量 (H100 80GB)。在 2x 4090 上，FP8 方案因通信瓶颈导致性能劣于 INT4 单卡方案，故 A2 工作点 (FP8 跨卡) 在性价比排序中应被排除，仅保留 A1 (INT4 单卡) 作为 2x 4090 的最优配置。

## Corrected Claim

2x RTX 4090 运行 FP8 Qwen3-27B 时的替代方案：若坚持 FP8 精度，需使用支持 NVLink 的硬件 (如 A100/H100) 或单卡大容量 (H100 80GB)。在 2x 4090 上，FP8 方案因通信瓶颈导致性能劣于 INT4 单卡方案，故 A2 工作点 (FP8 跨卡) 在性价比排序中应被排除，仅保留 A1 (INT4 单卡) 作为 2x 4090 的最优配置。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 不支持 NVLink，FP8 跨卡通信开销大且显存带宽受限，INT4 单卡方案在 2x 4090 场景下确实优于 FP8 跨卡方案，符合硬件特性与推理优化常识。

# N261: NVFP4 反量化至 FP16 的查找表 (LUT) 大小为 256 项 (每项 2 bytes)，总大小 512 bytes，完全驻留在 V100 的 L1/

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N89, N90, N91

## Claim

NVFP4 反量化至 FP16 的查找表 (LUT) 大小为 256 项 (每项 2 bytes)，总大小 512 bytes，完全驻留在 V100 的 L1/L2 Cache 中；反量化操作的算术强度为 1 FLOP/byte，远低于 V100 Tensor Core 的峰值算力限制，因此瓶颈确认为内存带宽而非计算单元，这与 N91 声称的‘非对齐内存访问’为主要瓶颈一致。

## Corrected Claim

NVFP4（假设指代某种 4-bit 浮点格式）反量化至 FP16 的查找表大小为 256 项 (512 bytes)，通常可驻留在 V100 的 L1/L2 Cache 中；由于查表操作主要受内存带宽限制，其算术强度较低，瓶颈倾向于内存带宽而非计算单元，这与非对齐内存访问可能带来的额外开销一致。

## Evidence

[质询]NVFP4 并非 NVIDIA 官方标准格式（通常为 FP4 E2M1 或 INT4），且 V100 硬件不支持原生 FP4 运算，需软件模拟或查表；将反量化算术强度简单定义为 1 FLOP/byte 过于简化，忽略了查表操作本身的内存访问模式及潜在的非对齐开销，且‘完全驻留 L1/L2’取决于具体实现和缓存策略，并非绝对物理事实。 | 先验知识/题面给定，逻辑校验通过，但 NVFP4 为非标准术语且 V100 无原生 FP4 支持，具体性能瓶颈归因缺乏直接来源支持，故降级。

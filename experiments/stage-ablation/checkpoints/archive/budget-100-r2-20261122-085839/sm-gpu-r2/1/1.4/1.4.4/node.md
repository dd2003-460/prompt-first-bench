# N43: RTX 4090 (Ada架构) 支持 FP8 Tensor Core，可加速 FP8 KV Cache 的量化/反量化操作；RTX 3090 (Ampere架

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

RTX 4090 (Ada架构) 支持 FP8 Tensor Core，可加速 FP8 KV Cache 的量化/反量化操作；RTX 3090 (Ampere架构) 不支持 FP8，仅支持 INT8/INT4，因此 4090 在 KV Cache 量化方案上具有架构优势

## Corrected Claim

RTX 4090 (Ada架构) 支持 FP8 Tensor Core，可加速 FP8 KV Cache 的量化/反量化操作；RTX 3090 (Ampere架构) 不支持 FP8，仅支持 INT8/INT4，因此 4090 在 KV Cache 量化方案上具有架构优势

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 (Ada) 确实引入 FP8 Tensor Core 支持，而 RTX 3090 (Ampere) 仅支持 FP16/BF16/INT8/INT4，不支持原生 FP8 硬件加速，陈述符合硬件架构事实。

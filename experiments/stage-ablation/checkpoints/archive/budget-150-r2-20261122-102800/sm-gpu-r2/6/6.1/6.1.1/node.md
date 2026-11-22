# N133: 修正自矛盾检测：N43 声称 RTX 4090 支持 FP8，但根据 NVIDIA 官方规格，RTX 4090 (Ada Lovelace 架构) 不支持原生 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N43

## Claim

修正自矛盾检测：N43 声称 RTX 4090 支持 FP8，但根据 NVIDIA 官方规格，RTX 4090 (Ada Lovelace 架构) 不支持原生 FP8 Tensor Core 运算，仅支持 BF16/INT8/FP16。vLLM 在 RTX 4090 上运行 FP8 模型需依赖 CPU offload 或软件模拟，性能会显著下降，不应视为原生支持。

## Corrected Claim

修正自矛盾检测：N43 声称 RTX 4090 支持 FP8，但根据 NVIDIA 官方规格，RTX 4090 (Ada Lovelace 架构) 不支持原生 FP8 Tensor Core 运算，仅支持 BF16/INT8/FP16。vLLM 在 RTX 4090 上运行 FP8 模型需依赖 CPU offload 或软件模拟，性能会显著下降，不应视为原生支持。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 (Ada Lovelace) 确实不支持原生 FP8 Tensor Core，该架构仅支持 FP16/BF16/INT8 等精度，FP8 支持始于 Hopper 架构 (H100)。

## Search Query

NVIDIA RTX 4090 FP8 support official specifications

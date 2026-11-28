# N31: V100-SXM2 (Compute Capability 7.0) 不支持 FP8 或 FP4 原生硬件指令，NVFP4 量化在 V100 上必须反量化为 F

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

V100-SXM2 (Compute Capability 7.0) 不支持 FP8 或 FP4 原生硬件指令，NVFP4 量化在 V100 上必须反量化为 FP16/BF16 或 INT8 进行计算，导致 'Dequantization Overhead' 抵消部分带宽优势，实测推理延迟相比纯 FP16 仅优化 10-20%，而非预期的 4x 加速。

## Corrected Claim

V100-SXM2 (Compute Capability 7.0) 不支持 FP8 或 FP4 原生硬件指令，NVFP4 量化在 V100 上必须反量化为 FP16/BF16 或 INT8 进行计算，导致 'Dequantization Overhead' 抵消部分带宽优势，实际推理加速比远低于理论峰值（通常显著低于4x），具体收益取决于算子实现与内存带宽瓶颈。

## Evidence

[质询]具体性能数据（10-20%优化、非4x加速）缺乏直接来源支持，属于经验事实，且不同模型/框架下反量化开销差异巨大，该具体数值范围可能不准确或过于绝对。 | 来源[1]证实V100 (CC 7.0) 不支持原生BF16/FP8等低精度计算，需依赖软件模拟或反量化，逻辑上支持'存在反量化开销'及'无法获得原生低精度加速'的定性结论，但未提供具体的10-20%延迟优化数据，故降级为定性描述。

## Retrieval Sources

- {'url': 'https://github.com/FlashML-org/FreeVideo/issues/845&rut=7467d393b191c3dbb72eca9de7f2b89fedca2e695a3dfa8af2ad5aa7a5f266fd', 'type': 'ddg', 'title': '[启动器] 这张显卡不受支持 · Issue #845 · FlashML-org/FreeVideo'}

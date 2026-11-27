# N616: FMA 指令的吞吐量仅为 INT8 路径的 1/2 至 1/4，这一结论需量化：在 EPYC 9004 系列上，FMA (FP16/BF16) 的吞吐量约为 2

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N217

## Claim

FMA 指令的吞吐量仅为 INT8 路径的 1/2 至 1/4，这一结论需量化：在 EPYC 9004 系列上，FMA (FP16/BF16) 的吞吐量约为 2-4 TOPS/核心，而 INT8 路径（AVX-512 VNNI 或 AMX）的吞吐量约为 8-16 TOPS/核心，因此 FMA 吞吐量确实为 INT8 的 1/2 至 1/4。

## Corrected Claim

在 EPYC 9004 系列上，INT8 路径（AVX-512 VNNI）的吞吐量通常显著高于 FP16/BF16 路径，具体倍数取决于频率和指令集实现，但通常 INT8 性能优势明显。

## Evidence

[质询]数值量级与具体硬件规格存在偏差：EPYC 9004 (Genoa) 原生支持 AVX-512，其 FP16/BF16 吞吐量通常远高于 2-4 TOPS/核心（例如 Zen 4 架构下 FP16 可达 ~16-32 TOPS/核心，取决于具体实现和频率），而 INT8 吞吐量也需根据具体指令集（VNNI vs AMX，注意 Genoa 无 AMX）精确计算。该陈述中的具体数值（2-4 vs 8-16）可能基于特定低频或保守估计，缺乏通用性，且将 FMA 吞吐量直接等同于 FP16/BF16 吞吐量在术语上不够严谨（FMA 通常指 FP32/FP64，FP16 通常用 FMA 或专用指令）。 | 经验事实，逻辑自洽但缺来源支持。虽然 INT8 吞吐量通常高于 FP16/BF16 的结论在大多数现代 CPU 上成立（比例关系大致合理），但具体数值（2-4 TOPS/核心）对于 EPYC 9004 而言偏低，且无外部来源验证具体数值。

## Search Query

AMD EPYC 9004 FMA vs INT8 TOPS per core

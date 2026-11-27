# N613: 对于 INT4 量化推理，AVX-512 VNNI 可提供约 2-3 倍的加速，但 AMX 进一步将此加速比提升至 3-5 倍，这一结论需修正：AVX-512 

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N216

## Claim

对于 INT4 量化推理，AVX-512 VNNI 可提供约 2-3 倍的加速，但 AMX 进一步将此加速比提升至 3-5 倍，这一结论需修正：AVX-512 VNNI 仅支持 INT8，不支持 INT4；INT4 推理需通过软件模拟或特定指令（如 AMX 的 INT4 支持）实现，AVX-512 对 INT4 的加速比低于 INT8，约为 1.5-2 倍。

## Corrected Claim

对于 INT4 量化推理，AVX-512 VNNI 指令集本身主要优化 INT8 运算，对 INT4 的支持需依赖软件模拟或特定扩展，其加速效果通常低于 INT8 原生支持；而 AMX 等新一代指令集提供了对 INT4 的原生或更高效支持，从而显著提升 INT4 推理性能。具体加速比取决于实现细节，通常 AMX 相比纯 AVX-512 软件模拟方案有显著优势。

## Evidence

[质询]该陈述包含具体的性能加速比数值（1.5-2倍、3-5倍），属于经验事实。由于检索失败无外部来源支持，且不同硬件实现、编译器优化及具体模型结构下，INT4与INT8的相对加速比波动较大，无法仅凭逻辑推导确定具体数值区间，存在数值量级不准确的风险。 | 经验事实，逻辑自洽（AVX-512 VNNI确实主要优化INT8，INT4需软件模拟或AMX支持，故INT4在纯AVX-512下加速比通常低于INT8），但缺来源支持具体数值。

## Search Query

AVX-512 VNNI INT4 support benchmark

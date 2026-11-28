# N249: V100 不支持原生 FP4 运算，NVFP4 量化在 V100 上实际执行时会被反量化为 FP16 进行计算，导致内存占用翻倍（27B 权重从 ~13.5GB

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N77

## Claim

V100 不支持原生 FP4 运算，NVFP4 量化在 V100 上实际执行时会被反量化为 FP16 进行计算，导致内存占用翻倍（27B 权重从 ~13.5GB 增至 ~54GB），超出 4x16GB=64GB 总显存限制，除非使用 offloading 或更低精度（如 INT4），否则该配置在 V100 上物理不可行

## Corrected Claim

V100 不支持原生 FP4 运算，NVFP4 量化在 V100 上实际执行时会被反量化为 FP16 进行计算，导致内存占用翻倍（27B 权重从 ~13.5GB 增至 ~54GB），超出 4x16GB=64GB 总显存限制，除非使用 offloading 或更低精度（如 INT4），否则该配置在 V100 上物理不可行

## Evidence

先验知识/题面给定，逻辑校验通过：V100 (Volta架构) 硬件不支持FP4原生运算，NVFP4需反量化为FP16计算，27B参数FP16权重约54GB，超过4x16GB=64GB显存限制（考虑KV Cache和激活值后必然OOM），物理不可行结论正确。

## Search Query

V100 FP4 support dequantize FP16 memory overhead 27B model tensor parallelism feasibility

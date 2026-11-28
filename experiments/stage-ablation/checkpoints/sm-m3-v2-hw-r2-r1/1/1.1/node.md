# N6: 4×V100-16GB (Compute Capability 7.0) 不支持原生 FP4 算术指令集（需 CC 8.9+），NVFP4 权重在 V100 上

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1

## Claim

4×V100-16GB (Compute Capability 7.0) 不支持原生 FP4 算术指令集（需 CC 8.9+），NVFP4 权重在 V100 上通过 CPU offload 或软件模拟反量化至 FP16/INT8 进行矩阵乘法，导致有效算力降至原生 FP16 的 ~10-20% [待核验: 需确认 vLLM 在 V100 上的具体 fallback kernel 性能损耗系数]。

## Corrected Claim

4×V100-16GB (Compute Capability 7.0) 不支持原生 FP4 算术指令集（需 CC 8.9+），NVFP4 权重在 V100 上需通过 CPU offload 或软件模拟反量化至 FP16/INT8 进行矩阵乘法，这将引入额外的反量化开销和内存访问延迟，导致有效算力显著低于原生 FP16 性能（具体损耗取决于实现细节，通常会有显著下降）。

## Evidence

[质询]具体性能损耗系数（~10-20%）缺乏通用基准数据支持，实际损耗高度依赖于具体的反量化实现（CPU offload vs GPU软件模拟）、内存带宽瓶颈及算子融合程度，不同框架和配置下差异巨大，该数值范围过于武断。 | 先验知识/题面给定，逻辑校验通过：V100 (CC 7.0) 确实不支持原生 FP4 指令（需 CC 8.9+），必须通过反量化至 FP16/INT8 计算，这必然导致额外开销；但具体性能损耗比例属于经验事实，无来源支持且受多种变量影响，故降级。

## Search Query

Tesla V100 FP4 support emulation performance penalty vLLM

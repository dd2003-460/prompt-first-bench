# N280: RX 7900 XTX 的 242 TOPS INT8 峰值算力是基于 RDNA 3 架构的 96 CUs * 2 FMA/clk * 4 ops/FMA (I

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N106

## Claim

RX 7900 XTX 的 242 TOPS INT8 峰值算力是基于 RDNA 3 架构的 96 CUs * 2 FMA/clk * 4 ops/FMA (INT8) * 2.4 GHz 计算得出，但该数值未考虑 ROCm 软件栈的 kernel 优化效率；在 vLLM 等主流推理框架中，由于缺乏针对 RDNA 3 的专用 INT8 GEMM kernel 优化，实际可达算力通常仅为峰值的 30-50%，即 72-121 TOPS。

## Corrected Claim

RX 7900 XTX 的 242 TOPS INT8 峰值算力是基于 RDNA 3 架构的 96 CUs * 2 FMA/clk * 4 ops/FMA (INT8) * 2.4 GHz 计算得出，但该数值未考虑 ROCm 软件栈的 kernel 优化效率；在 vLLM 等主流推理框架中，由于缺乏针对 RDNA 3 的专用 INT8 GEMM kernel 优化，实际可达算力通常显著低于峰值，具体比例取决于模型与实现。

## Evidence

[质询]具体数值（242 TOPS）及实际效率区间（30-50%）属于经验事实，缺乏直接来源支持，且不同模型/框架下的实际利用率波动较大，固定区间可能过于绝对。 | 先验知识/题面给定，逻辑校验通过；但具体数值与效率区间为经验事实，无来源直接支持，故降级。

## Search Query

ROCm RDNA 3 INT8 GEMM kernel efficiency ratio

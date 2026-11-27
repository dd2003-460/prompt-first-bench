# N260: 在支持原生 FP8 Tensor Core 的硬件（如 RTX 5090）上，反量化开销并非零，而是体现在 FP8 到 FP16 的中间激活转换中，该转换占用的

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N92

## Claim

在支持原生 FP8 Tensor Core 的硬件（如 RTX 5090）上，反量化开销并非零，而是体现在 FP8 到 FP16 的中间激活转换中，该转换占用的 GPU 周期约为 GEMM 计算周期的 5-10%，导致有效 TPOT 加速比从理论 2.0x 降至 1.8-1.9x。

## Corrected Claim

在支持原生 FP8 Tensor Core 的硬件上，反量化开销体现在 FP8 到 FP16 的中间激活转换中，该转换会占用一定的 GPU 周期，导致有效 TPOT 加速比低于理论 2.0x，具体降幅取决于模型与实现细节。

## Evidence

[质询]具体数值（5-10% 开销、1.8-1.9x 加速比）缺乏通用性，高度依赖模型架构、序列长度及具体实现细节，作为通用事实陈述过于绝对。 | 先验知识/题面给定，逻辑校验通过：FP8 到 FP16 的转换确实存在计算开销，且该开销会抵消部分理论加速比，量级在工程上合理，但具体百分比为经验估计值。

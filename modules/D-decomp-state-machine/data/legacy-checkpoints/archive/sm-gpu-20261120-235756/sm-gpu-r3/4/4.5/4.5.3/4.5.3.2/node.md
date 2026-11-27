# N275: 单张 H100 SXM 的 Prefill 算力为 989 TFLOPS (FP16)，其理论 TTFT 约为 2x RTX 5090 (660 TFLOPS)

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N97

## Claim

单张 H100 SXM 的 Prefill 算力为 989 TFLOPS (FP16)，其理论 TTFT 约为 2x RTX 5090 (660 TFLOPS) 的 67% (660/989)，即 H100 单卡 TTFT 比双 5090 快约 1.49x；若计入 H100 的 NVLink 低延迟优势，实际 TTFT 优势可能扩大至 1.6x-1.8x。

## Corrected Claim

单张 H100 SXM 的 Prefill 算力为 989 TFLOPS (FP16)，约为 2x RTX 5090 (660 TFLOPS) 的 1.49 倍。在理想算力受限场景下，H100 单卡 TTFT 理论上比双 5090 快约 1.49 倍；实际性能受内存带宽、软件优化及系统架构影响，具体优势需实测确定。

## Evidence

[质询]将Prefill算力直接等同于TTFT（首字延迟）的倒数关系过于简化，忽略了内存带宽瓶颈、KV Cache初始化开销及软件栈效率差异；此外，'NVLink低延迟优势'在单卡Prefill场景下作用有限，主要影响多卡通信，对单卡TTFT的1.6x-1.8x放大缺乏严谨依据。 | 先验知识/题面给定，逻辑校验通过（算力比值计算正确：660/989≈0.667，1/0.667≈1.49），但TTFT与算力的线性反比关系及NVLink对单卡TTFT的具体增益系数属于经验性推断，缺乏直接来源支持，故降级。

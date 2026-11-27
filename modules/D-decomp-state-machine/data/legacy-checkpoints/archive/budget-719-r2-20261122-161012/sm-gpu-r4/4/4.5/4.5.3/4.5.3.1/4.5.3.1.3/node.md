# N573: M3 Ultra 相比 M2 Ultra 的 CPU 核心数从 24 核增加至 32 核，Prefill 阶段（计算密集型）的理论 FLOPS 提升比例约为 3

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N238, N239, N240

## Claim

M3 Ultra 相比 M2 Ultra 的 CPU 核心数从 24 核增加至 32 核，Prefill 阶段（计算密集型）的理论 FLOPS 提升比例约为 33% (32/24 - 1)，但由于 Prefill 阶段受内存带宽瓶颈影响较小且存在并行度上限，实际 TTFT 加速比预计仅为 15-25%，而非线性 33%。

## Corrected Claim

M3 Ultra 相比 M2 Ultra 的 CPU 核心数从 24 核增加至 32 核，理论计算能力提升约 33%。由于实际性能受并行效率、内存带宽及软件栈优化等多重因素影响，Prefill 阶段的实际 TTFT 加速比通常低于理论峰值，具体数值取决于工作负载特征。

## Evidence

[质询]该陈述包含具体的硬件规格（M3 Ultra 32核 vs M2 Ultra 24核）和具体的性能预测范围（15-25%），属于经验事实。虽然 M3 Ultra 确实有 32 核 CPU 且 M2 Ultra 有 24 核 CPU（基于 Apple 官方发布数据），但 'TTFT 加速比预计仅为 15-25%' 是一个高度依赖具体模型大小、序列长度、内存带宽利用率及软件优化程度的经验性估计，并非从第一性原理可严格推导出的固定值。此外，Prefill 阶段通常被认为是计算密集型（Compute-bound），而非内存带宽瓶颈（Memory-bound），陈述中称 '受内存带宽瓶颈影响较小' 虽符合一般直觉，但将其作为加速比低于理论值的唯一或主要解释可能过于简化，忽略了其他并行开销和调度延迟。 | source=knowledge，逻辑自洽（32/24-1≈33% 计算正确，性能提升低于理论峰值符合工程直觉），但具体加速比范围（15-25%）为经验估计，缺乏通用性证明，且无外部来源支持该特定数值区间，故降级。

## Search Query

Apple M3 Ultra vs M2 Ultra CPU core count performance uplift

# N269: AMD RX 7900 XTX 在 ROCm 6.x 下执行 W4A16 量化推理时，INT4 权重解包（Dequantize）至 FP16 的指令序列效率及每

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N97

## Claim

AMD RX 7900 XTX 在 ROCm 6.x 下执行 W4A16 量化推理时，INT4 权重解包（Dequantize）至 FP16 的指令序列效率及每字节数据搬运的额外周期数，需对比 NVIDIA 硬件加速路径的性能差距。

## Corrected Claim

AMD RX 7900 XTX 在 ROCm 6.x 下执行 W4A16 量化推理时，INT4 权重解包至 FP16 的过程涉及额外的计算与数据搬运开销，其性能通常低于 NVIDIA 硬件加速路径，具体指令效率及周期数需依赖特定基准测试数据。

## Evidence

[质询]该陈述包含具体的硬件微架构性能指标（指令序列效率、每字节额外周期数），属于高度依赖具体硬件实现和软件栈版本的经验事实，且缺乏公开基准数据支持，无法从第一性原理推导。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该具体性能对比数据非通用公理或题面给定）

## Search Query

AMD RX 7900 XTX ROCm W4A16 dequantization instruction overhead performance

# N609: AMD EPYC 9004 系列 (Zen 4) 的 AMX 单元理论峰值吞吐量约为 2-4 TOPS/核心 (INT8)，具体数值取决于频率和核心数；以 96

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N215

## Claim

AMD EPYC 9004 系列 (Zen 4) 的 AMX 单元理论峰值吞吐量约为 2-4 TOPS/核心 (INT8)，具体数值取决于频率和核心数；以 96 核 EPYC 9654 为例，理论总 AMX 吞吐量约为 192-384 TOPS，但实际推理效率受内存带宽和调度开销限制，通常仅为理论峰值的 30-50%。

## Corrected Claim

AMD EPYC 9004 系列 (Zen 4) 支持 AVX-512 指令集，其 INT8 理论峰值吞吐量取决于具体频率和核心数，通常每核心在 0.5-1 TOPS 左右（基于 AVX-512 计算能力估算），96 核 EPYC 9654 的理论总吞吐量约为 48-96 TOPS，实际推理效率受内存带宽限制，通常远低于理论峰值。

## Evidence

[质询]AMD EPYC 9004 (Zen 4) 架构中并不存在名为 'AMX' 的单元（AMX 是 Intel 的 Advanced Matrix Extensions 指令集），AMD 对应的矩阵加速指令集为 AVX-512 或后续的 Matrix Extensions，且 2-4 TOPS/核心 的 INT8 理论峰值对于通用 CPU 核心而言量级偏高（通常 AVX-512 在 3GHz 下约为 0.5-1 TOPS/核心），存在术语混淆和数值夸大嫌疑。 | 来源不可用；逻辑校验发现术语错误（AMD 无 AMX 单元）及数值量级存疑，属于经验事实且缺乏来源支持，无法验证。

## Search Query

AMD EPYC 9004 AMX INT8 TOPS benchmark

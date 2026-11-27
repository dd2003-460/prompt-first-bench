# N147: 2×RTX 3090通过PCIe 4.0 x16互联进行张量并行（Tensor Parallelism）或流水线并行（Pipeline Parallelism）

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N28

## Claim

2×RTX 3090通过PCIe 4.0 x16互联进行张量并行（Tensor Parallelism）或流水线并行（Pipeline Parallelism）时，NCCL All-Reduce操作的实测带宽（GB/s）与理论峰值带宽（~32 GB/s双向）的比值，以此量化通信开销占比

## Corrected Claim

2×RTX 3090通过PCIe 4.0 x16互联进行张量并行或流水线并行时，NCCL All-Reduce操作的实测带宽通常显著低于理论峰值带宽（~32 GB/s双向），具体比值取决于驱动版本、NCCL配置及消息大小，需通过实际基准测试（如nccl-tests）获取，一般通信开销占比在中等规模张量并行中较为显著。

## Evidence

[质询]该陈述试图量化一个具体的经验性能指标（NCCL All-Reduce实测带宽与理论峰值的比值），但缺乏具体的软件版本、驱动版本、拓扑配置及负载大小等关键上下文，且未提供实测数据，仅凭理论峰值无法确定具体的'占比'数值，属于缺乏实证支持的经验事实。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该指标依赖具体环境配置，无法从第一性原理直接推出具体数值）

## Search Query

NCCL all-reduce bandwidth PCIe 4.0 RTX 3090 dual GPU tensor parallelism benchmark

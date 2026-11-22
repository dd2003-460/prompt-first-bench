# N265: 实际推理速度还受 Kernel 启动开销和内存分配器碎片化影响，通常比理论峰值低 5-10%，因此 RTX 4090 NVFP4 的实际稳定吞吐量约为 62-6

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N96

## Claim

实际推理速度还受 Kernel 启动开销和内存分配器碎片化影响，通常比理论峰值低 5-10%，因此 RTX 4090 NVFP4 的实际稳定吞吐量约为 62-66 tokens/s，需通过 vLLM 基准测试验证。

## Corrected Claim

实际推理速度受 Kernel 启动开销和内存分配器碎片化影响，通常低于理论峰值，RTX 4090 NVFP4 的实际稳定吞吐量需通过 vLLM 等基准测试针对具体模型进行验证。

## Evidence

[质询]具体数值（62-66 tokens/s）和性能损耗比例（5-10%）属于高度依赖具体模型、序列长度、Batch Size 及硬件驱动版本的经验事实，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

RTX 4090 vLLM inference throughput benchmark NVFP4

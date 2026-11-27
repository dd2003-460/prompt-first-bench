# N451: RTX 3090 在显存不足需 Offload 至 CPU 时的 Decode 阶段吞吐量：受限于 PCIe 4.0 x16 带宽（~32 GB/s）和 CPU

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N145

## Claim

RTX 3090 在显存不足需 Offload 至 CPU 时的 Decode 阶段吞吐量：受限于 PCIe 4.0 x16 带宽（~32 GB/s）和 CPU 内存带宽，预期 tokens/s 在 4-12 之间，具体数值取决于 Offload 策略和软件栈优化 [待核验]

## Corrected Claim

RTX 3090 在显存不足需 Offload 至 CPU 时，Decode 阶段吞吐量受限于 PCIe 4.0 x16 带宽（~32 GB/s）和 CPU 内存带宽，通常显著低于纯 GPU 推理，具体数值（如 4-12 tokens/s）取决于模型规模、Offload 策略及软件栈优化程度。

## Evidence

[质询]该陈述属于经验事实（硬件性能与软件栈优化结果），无法从第一性原理严格推导。虽然 PCIe 4.0 x16 带宽（~32 GB/s）是硬件规格，但具体的 Decode 吞吐量（4-12 tokens/s）高度依赖于模型大小、Offload 策略（如是否使用 KV Cache 压缩、异步传输优化）以及 CPU 内存带宽，缺乏具体模型和软件栈上下文，数值范围可能因配置不同而显著波动，且无来源支持该特定区间。 | 经验事实，逻辑自洽但缺来源支持。PCIe 4.0 x16 带宽限制确实会严重制约 Offload 性能，4-12 tokens/s 的量级在缺乏高效优化时是合理的估计，但具体数值需依赖实测数据，当前无可用外部证据。

## Search Query

RTX 3090 24GB Qwen3-27B INT8 CPU offload decode tokens per second 32K context

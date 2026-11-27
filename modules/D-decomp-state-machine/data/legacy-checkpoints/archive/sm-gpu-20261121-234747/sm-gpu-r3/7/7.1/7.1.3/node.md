# N447: RTX 4090 在显存不足需 Offload 至 CPU 时的 Decode 阶段吞吐量：受限于 PCIe 4.0 x16 带宽（~32 GB/s）和 CPU

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N144

## Claim

RTX 4090 在显存不足需 Offload 至 CPU 时的 Decode 阶段吞吐量：受限于 PCIe 4.0 x16 带宽（~32 GB/s）和 CPU 内存带宽，预期 tokens/s 在 5-15 之间，具体数值取决于 Offload 策略和软件栈优化 [待核验]

## Corrected Claim

RTX 4090 在显存不足需 Offload 至 CPU 时的 Decode 阶段吞吐量受限于 PCIe 4.0 x16 带宽（~32 GB/s）和 CPU 内存带宽，具体 tokens/s 数值高度依赖于模型规模、Offload 策略及软件栈优化，通常显著低于纯 GPU 推理性能。

## Evidence

[质询]该陈述为经验事实（硬件性能指标），缺乏具体来源支持，且5-15 tokens/s的量级估算依赖于特定的模型大小和Offload策略，不同场景下波动极大，无法仅凭逻辑推导确定具体数值范围。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

RTX 4090 24GB Qwen3-27B INT8 CPU offload decode tokens per second 32K context

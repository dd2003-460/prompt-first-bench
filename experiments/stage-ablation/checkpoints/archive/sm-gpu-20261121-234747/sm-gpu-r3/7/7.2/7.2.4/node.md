# N452: RTX 3090 与 RTX 4090 在 Offload 场景下的吞吐量比例：由于两者都受限于相同的 PCIe 4.0 x16 带宽（~32 GB/s）和 C

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N145

## Claim

RTX 3090 与 RTX 4090 在 Offload 场景下的吞吐量比例：由于两者都受限于相同的 PCIe 4.0 x16 带宽（~32 GB/s）和 CPU 内存带宽，预期吞吐量比例接近 1:1，差异主要来自 GPU 计算单元在 Prefill 阶段的贡献，具体比例需实测验证 [待核验]

## Corrected Claim

RTX 3090 与 RTX 4090 在 Offload 场景下，若严格受限于相同的 PCIe 4.0 x16 带宽瓶颈，理论吞吐量上限接近；但实际比例受 GPU 计算能力、内存带宽及具体 Offload 策略影响，需实测验证，不能简单断言为 1:1。

## Evidence

[质询]该陈述包含具体的硬件规格（PCIe 4.0 x16 带宽 ~32 GB/s）和性能预测（吞吐量比例接近 1:1），属于经验事实。虽然逻辑上在带宽受限场景下成立，但缺乏实测数据支持，且不同 Offload 策略（如 KV Cache 大小、Batch Size）可能导致比例显著偏离 1:1，仅凭逻辑推导不足以确认为 verified。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）。

## Search Query

RTX 3090 vs RTX 4090 CPU offload LLM inference performance comparison 32K context

# N118: 2× RTX 4090 运行 Qwen3-27B 的吞吐量瓶颈在于 PCIe 4.0 x16 带宽（~32GB/s），在 32K 上下文下 KV Cache 传

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N25

## Claim

2× RTX 4090 运行 Qwen3-27B 的吞吐量瓶颈在于 PCIe 4.0 x16 带宽（~32GB/s），在 32K 上下文下 KV Cache 传输导致有效吞吐量上限约为 12-18 tokens/s [待核验：vLLM 实测数据]，低于 BF16 理论峰值。

## Corrected Claim

2× RTX 4090 运行 Qwen3-27B 时，PCIe 4.0 x16 带宽（~32GB/s）可能成为 KV Cache 传输的瓶颈，在 32K 上下文下有效吞吐量可能显著低于 BF16 理论峰值，但具体数值（如 12-18 tokens/s）需实测验证。

## Evidence

[质询]该陈述包含具体的经验性性能数据（12-18 tokens/s）和硬件瓶颈归因，属于经验事实而非第一性原理可推导结论。在缺乏实测数据或权威基准测试来源支持的情况下，仅凭逻辑自洽无法验证具体数值量级和瓶颈归因的准确性。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

Qwen3 27B inference latency RTX 4090 PCIe bottleneck tokens per second

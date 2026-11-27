# N144: 在 Batch Size = 1 时，L40S 的 Decode 延迟约为 RTX 4090 的 1.17 倍 (1008/864)，但在 Batch Size

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N51, N52, N53

## Claim

在 Batch Size = 1 时，L40S 的 Decode 延迟约为 RTX 4090 的 1.17 倍 (1008/864)，但在 Batch Size = 8 时，L40S 因显存容量优势 (48GB vs 24GB) 可容纳更多 KV Cache，而 RTX 4090 需启用 Offload 或降低 Batch，导致 L40S 的总吞吐量 (Tokens/sec) 反超 RTX 4090 约 1.5-2.0 倍 [待核验具体基准测试数据]。

## Corrected Claim

在 Batch Size = 1 时，L40S 的 Decode 延迟通常略高于 RTX 4090；但在 Batch Size = 8 时，L40S 因显存容量优势 (48GB vs 24GB) 可容纳更多 KV Cache，而 RTX 4090 可能需启用 Offload 或降低 Batch，导致 L40S 的总吞吐量 (Tokens/sec) 可能反超 RTX 4090。

## Evidence

[质询]具体数值（1.17倍延迟、1.5-2.0倍吞吐量）缺乏公开基准测试支持，且吞吐量反超倍数高度依赖模型大小、序列长度及具体推理框架配置，属于经验事实而非第一性原理可推导结论。 | 逻辑自洽（显存容量优势在大Batch下确实能避免Offload从而提升吞吐），但作为经验事实，缺乏来源直接支持具体数值，且检索无可用来源，故降级。

## Search Query

L40S vs RTX 4090 LLM inference benchmark batch size throughput

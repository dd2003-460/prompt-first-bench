# N161: TP=2 W4 模式下，2x RTX 4090 (24GB) 每卡显存占用 9.43GB，剩余 14.57GB；该剩余空间可支持约 7,500 tokens 的

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N48

## Claim

TP=2 W4 模式下，2x RTX 4090 (24GB) 每卡显存占用 9.43GB，剩余 14.57GB；该剩余空间可支持约 7,500 tokens 的额外 KV Cache (假设 KV 每 token 占用 ~2KB? 需精确计算 Qwen3-27B KV 大小)，因此 2x 4090 在 W4 下可轻松支持 32K 上下文及 Batch Size=4-8，其瓶颈确认为 PCIe 带宽而非显存容量。

## Corrected Claim

TP=2 W4 模式下，2x RTX 4090 (24GB) 每卡显存占用 9.43GB，剩余 14.57GB。基于 Qwen3-27B 的 GQA 架构估算，每 token KV Cache 占用约 65-131KB，剩余空间仅支持约 100-200 tokens 的额外上下文。因此，2x 4090 在 W4 下无法直接支持 32K 上下文，瓶颈确认为显存容量而非 PCIe 带宽。

## Evidence

[质询]KV Cache 每 token 占用 ~2KB 的假设严重低估了 Qwen3-27B 的实际显存需求。Qwen3-27B 通常采用 GQA (Grouped Query Attention)，假设 32 层、KV Head 数约为 8 (或 4)，Head Dim 128，FP16 精度下，每 token KV 大小约为 32 * 8 * 2 * 128 * 2 bytes ≈ 131KB (若 KV Head 为 4 则约为 65KB)。即使按最乐观的 65KB 计算，14.57GB 剩余空间仅能支持约 230 tokens 的额外 KV Cache，远不足以支持 32K 上下文。原陈述中 '2KB' 的量级错误导致结论完全失效。 | 逻辑校验失败：KV Cache 大小估算存在数量级错误（2KB vs 实际 ~65-131KB），导致 '轻松支持 32K 上下文' 的结论在数学上不成立。

## Search Query

Qwen3-27B KV cache size per token W4 quantization batch size limit

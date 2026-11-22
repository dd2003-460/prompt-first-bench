# N643: N265 (RTX 4090 + BF16) 的 OOM 阈值精确值：Qwen3-27B 在 32K 上下文下 BF16 总显存需求为 55.5GB (权重54

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N265, N266, N267

## Claim

N265 (RTX 4090 + BF16) 的 OOM 阈值精确值：Qwen3-27B 在 32K 上下文下 BF16 总显存需求为 55.5GB (权重54GB + KV Cache 1.5GB)，而 RTX 4090 可用显存为 23.5GB (24GB - 0.5GB 系统/驱动开销)，缺口为 32GB，确认该配置在 vLLM/TensorRT-LLM 标准推理框架下必然抛出 CUDA OOM 错误，无需进一步量化修正。

## Corrected Claim

Qwen3-27B 在 32K 上下文下 BF16 总显存需求远超 RTX 4090 的 23.5GB 可用显存（仅权重即需 54GB），确认该配置在标准推理框架下必然抛出 CUDA OOM 错误。

## Evidence

[质询]数值量级与口径混淆：Qwen3-27B 在 BF16 下的权重显存约为 54GB (27B * 2 bytes)，但 32K 上下文的 KV Cache 显存需求远不止 1.5GB。以 Qwen3-27B 典型架构（如 32层，GQA 8 KV heads，head_dim 128）估算，单 token KV Cache 约为 32 * 8 * 128 * 2 * 2 bytes ≈ 128KB，32K tokens 需约 4GB。若考虑 vLLM 的 PagedAttention 开销及多 batch 场景，KV Cache 需求通常更高。因此，总显存需求 55.5GB 的数值可能低估了 KV Cache 部分，导致缺口计算（32GB）不准确，尽管结论（OOM）不变，但精确值存疑。 | 先验知识/题面给定，逻辑校验通过：权重显存计算正确（27B*2=54GB），RTX 4090 可用显存约 23.5GB 合理，总需求远超可用显存，OOM 结论逻辑自洽；但 KV Cache 1.5GB 的数值对于 32K 上下文而言偏低（通常需数 GB），导致总显存需求 55.5GB 的精确值缺乏严格依据，故降级为定性表述。

## Search Query

Qwen3-27B BF16 VRAM requirement 32k context RTX 4090 OOM

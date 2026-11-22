# N325: Qwen3-27B 在 FP8 (E4M3) 精度下的权重显存占用为 27GB (27B * 1 byte)，需确认该量化方案下激活值 (Activation)

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N97, N98, N99

## Claim

Qwen3-27B 在 FP8 (E4M3) 精度下的权重显存占用为 27GB (27B * 1 byte)，需确认该量化方案下激活值 (Activation) 在 32K 上下文下的峰值显存占用具体数值（通常受 Batch Size 和 Attention 计算图影响，估算为 3-8GB），以修正 N97 中 5GB 的估算值。

## Corrected Claim

Qwen3-27B 在 FP8 (E4M3) 精度下的权重显存占用约为 27GB。激活值及 KV Cache 的峰值显存占用取决于 Batch Size 和推理框架优化，在 32K 上下文下通常显著高于 5GB，具体数值需根据实际部署配置（如 Batch Size=1 或更大）进行精确计算，原 5GB 估算可能偏低。

## Evidence

[质询]激活值显存占用高度依赖于具体的推理框架（如 vLLM, TGI）、Batch Size 以及是否启用 FlashAttention 等优化技术，'3-8GB' 是一个缺乏具体配置前提的宽泛估算范围，且 32K 上下文下 KV Cache 的占用往往远超此范围（取决于 Batch Size），该数值缺乏严谨的推导依据。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且激活值显存为依赖具体实现的经验参数，无法从第一性原理严格推出唯一值）

## Search Query

Qwen3-27B FP8 activation memory usage 32k context vLLM

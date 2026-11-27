# N159: Tesla P40 在 INT8 量化下推理 Qwen3-27B 的实测吞吐量约为 3-5 tokens/s，主要受限于其 348 GB/s 的低显存带宽及缺乏

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N46

## Claim

Tesla P40 在 INT8 量化下推理 Qwen3-27B 的实测吞吐量约为 3-5 tokens/s，主要受限于其 348 GB/s 的低显存带宽及缺乏 Tensor Core 导致的计算效率低下，远低于现代消费级 GPU (RTX 4090 ~30-40 tokens/s)。

## Corrected Claim

Tesla P40 在 INT8 量化下推理 Qwen3-27B 的吞吐量显著低于现代消费级 GPU (如 RTX 4090)，主要受限于其较低的显存带宽及缺乏 Tensor Core 导致的计算效率低下。

## Evidence

[质询]该陈述包含具体的硬件规格（348 GB/s带宽）和实测性能数据（3-5 tokens/s vs 30-40 tokens/s），属于经验事实。虽然逻辑上低带宽确实限制推理速度，但具体数值缺乏来源支持，且不同量化实现（如AWQ/GPTQ）和批处理大小会显著影响吞吐量，单一数值范围可能不准确。 | 经验事实，逻辑自洽但缺来源支持。Tesla P40确实无Tensor Core且带宽较低，推理大模型速度慢于RTX 4090符合物理直觉，但具体吞吐量数值无法从第一性原理严格推出，且无外部来源验证具体数值。

## Search Query

Tesla P40 Qwen 27B INT8 inference benchmark tokens per second

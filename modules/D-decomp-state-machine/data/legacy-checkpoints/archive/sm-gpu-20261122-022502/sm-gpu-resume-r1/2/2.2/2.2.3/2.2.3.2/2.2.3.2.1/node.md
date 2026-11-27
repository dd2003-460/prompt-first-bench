# N590: B200 上 NVFP4 权重的反量化开销在 vLLM 0.6+ 版本中通过 TensorRT-LLM 优化可控制在 5% 以内，实际 Decode 吞吐上限约

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N181

## Claim

B200 上 NVFP4 权重的反量化开销在 vLLM 0.6+ 版本中通过 TensorRT-LLM 优化可控制在 5% 以内，实际 Decode 吞吐上限约为理论带宽上限的 95%，即 549 * 0.95 ≈ 521.6 tokens/s [待核验]

## Corrected Claim

在 B200 上，若 NVFP4 权重的反量化开销通过 TensorRT-LLM 优化控制在 5% 以内，且实际 Decode 吞吐达到理论带宽上限的 95%，则理论带宽为 549 tokens/s 时，实际吞吐约为 521.6 tokens/s。

## Evidence

[质询]该陈述包含具体的硬件性能指标（NVFP4反量化开销<5%、Decode吞吐上限95%）及特定软件版本（vLLM 0.6+）的优化效果，属于经验事实。检索无可用来源，无法验证这些具体数值是否准确，且不同模型规模、序列长度及硬件配置下，实际吞吐与理论带宽的比值波动较大，95%这一固定比例缺乏普遍性依据。 | 经验事实，逻辑自洽但缺来源支持。数学计算 549 * 0.95 ≈ 521.6 正确，但具体性能指标（5%开销、95%效率）无法从第一性原理推出，且无外部来源佐证。

## Search Query

vLLM TensorRT-LLM NVFP4 dequantization overhead B200

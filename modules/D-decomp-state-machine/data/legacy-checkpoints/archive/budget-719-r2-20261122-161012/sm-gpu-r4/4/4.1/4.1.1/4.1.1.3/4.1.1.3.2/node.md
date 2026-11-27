# N480: FP8 KV Cache 量化的实测精度损失：在 Llama 3 系列 70B 模型上，FP8 KV Cache 相比 BF16 KV Cache 的 Perp

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N198

## Claim

FP8 KV Cache 量化的实测精度损失：在 Llama 3 系列 70B 模型上，FP8 KV Cache 相比 BF16 KV Cache 的 Perplexity 增量通常 < 0.05，MMLU 得分下降 < 0.5%，表明 FP8 KV 量化在质量上可接受，可作为 Qwen3-27B FP8 权重的配套方案，使总 KV 显存减半至 64 KB/token。

## Corrected Claim

在 Llama 3 系列 70B 模型上，FP8 KV Cache 相比 BF16 KV Cache 的精度损失通常较小（Perplexity 增量和 MMLU 得分下降均在可接受范围内），表明 FP8 KV 量化在质量上可接受，可作为 Qwen3-27B FP8 权重的配套方案，使总 KV 显存减半至 64 KB/token。

## Evidence

[质询]该陈述包含具体的经验性数值指标（Perplexity增量<0.05, MMLU下降<0.5%）和特定模型（Llama 3 70B）的实测结果，属于经验事实。由于检索无可用来源，无法验证这些具体数值是否准确，且不同模型、不同量化实现（如E4M3 vs E5M2）及不同数据集下精度损失可能存在差异，存在将特定实验结果过度泛化的风险。 | 经验事实，逻辑自洽但缺来源支持。FP8量化KV Cache确实能显著降低显存占用（相比BF16减半），且通常精度损失较小，但具体数值指标缺乏外部证据直接支持。

## Search Query

Llama 3 70B FP8 KV cache quantization perplexity loss MMLU

# N100: FP8 量化校准策略 (Calibration Strategy) 对质量损失影响显著：静态量化 (Static) 需校准数据集 (如 512 条样本)，动态量

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N23

## Claim

FP8 量化校准策略 (Calibration Strategy) 对质量损失影响显著：静态量化 (Static) 需校准数据集 (如 512 条样本)，动态量化 (Dynamic) 无需校准但精度略低；Qwen3-27B 在 FP8 下若采用 GPTQ 或 AWQ 校准，MMLU 基准下降可控制在 <1%，而未经校准的朴素 FP8 截断可能导致下降 >5%。

## Corrected Claim

FP8 量化校准策略对质量损失影响显著：静态量化需校准数据集，动态量化无需校准但精度可能略低；对于大语言模型（如 Qwen3-27B），采用适当的校准策略（如 GPTQ/AWQ）通常能将 MMLU 等基准的性能下降控制在较低水平（如 <1%），而未经校准的朴素截断可能导致显著的性能下降。

## Evidence

[质询]陈述中关于 Qwen3-27B 在 FP8 下使用 GPTQ/AWQ 校准的具体性能数据（MMLU 下降 <1% vs >5%）属于特定模型的经验事实，参考来源仅涉及 BERT 等通用 Transformer 的 FP8 量化原理，未覆盖 Qwen3-27B 的具体基准测试结果，存在以偏概全或数据无源的风险。 | 来源 [1][2] 支持 FP8 量化需校准且能保持精度的通用逻辑，但缺乏 Qwen3-27B 具体数值支持，属经验事实缺来源直接佐证。

## Search Query

FP8 quantization calibration strategy GPTQ AWQ MMLU accuracy drop

## Retrieval Sources

- {'url': 'https://arxiv.org/html/2312.05725v2&rut=1dfacf541d180cc1304f6b2d03b35da208e53cab107ea3b30188aa7f676d62b8', 'type': 'ddg', 'title': 'FP8-BERT: Post-Training Quantization for Transformer - arXiv.org'}
- {'url': 'https://arxiv.org/abs/2312.05725&rut=2a329e003fe876fe5f2d0be9bbbf096df367fcfc7ec182ff3d918bed6fae2334', 'type': 'ddg', 'title': 'FP8-BERT: Post-Training Quantization for Transformer'}

# N227: W4量化下Qwen3-27B的MMLU准确率损失相对于BF16约为3-5% [待核验]，Perplexity增加约0.8-1.2%。该损失主要源于权重量化误差，

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N76

## Claim

W4量化下Qwen3-27B的MMLU准确率损失相对于BF16约为3-5% [待核验]，Perplexity增加约0.8-1.2%。该损失主要源于权重量化误差，与KV Cache精度无关。若任务对精度敏感（如医疗/法律），W4可能不可接受，需回退至INT8。

## Corrected Claim

W4量化下Qwen3-27B的MMLU准确率损失相对于BF16通常显著高于INT8（具体数值依量化算法而定，常见范围可能在3-5%或更高），Perplexity增加。该损失主要源于权重量化误差。若任务对精度敏感，W4可能不可接受，需回退至INT8或更高精度。

## Evidence

[质询]具体数值（3-5%准确率损失，0.8-1.2%困惑度增加）属于特定模型（Qwen3-27B）在特定量化方案下的经验测量结果，无法从第一性原理严格推导，且不同量化算法（如GPTQ, AWQ, SmoothQuant）及校准数据集会导致显著差异，缺乏通用性。 | source=knowledge，逻辑自洽（W4量化通常导致比INT8更大的精度损失，且主要源于权重误差），但具体数值为经验事实，无外部来源直接支持，依据经验事实排除条款降级。

## Search Query

Qwen3-27B W4 quantization MMLU accuracy loss

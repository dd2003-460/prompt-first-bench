# N223: INT8 KV Cache下Qwen3-27B的MMLU准确率损失相对于BF16 KV Cache约为0.5-1.0% [待核验]，Perplexity增加约0

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N75

## Claim

INT8 KV Cache下Qwen3-27B的MMLU准确率损失相对于BF16 KV Cache约为0.5-1.0% [待核验]，Perplexity增加约0.1-0.2%，该损失在通用对话任务中通常可接受，但在高精度数学/代码生成任务中可能显著，需根据具体任务基准测试决定。

## Corrected Claim

INT8 KV Cache下Qwen3-27B的MMLU准确率损失相对于BF16 KV Cache通常较小（一般在1%以内），Perplexity略有增加，该损失在通用对话任务中通常可接受，但在高精度数学/代码生成任务中可能显著，需根据具体任务基准测试决定。

## Evidence

[质询]具体数值范围（0.5-1.0% MMLU损失，0.1-0.2% Perplexity增加）缺乏针对Qwen3-27B在INT8 KV Cache下的特定基准测试数据支持，属于经验事实，不同量化实现（如SmoothQuant, GPTQ, AWQ）和校准数据集可能导致结果差异较大，直接断言固定区间存在过度精确的风险。 | 经验事实，逻辑自洽但缺来源支持（source=knowledge，但具体数值缺乏通用共识或第一性原理推导，且无外部来源验证，故降级为定性表述）

## Search Query

Qwen3-27B INT8 KV Cache MMLU accuracy loss benchmark

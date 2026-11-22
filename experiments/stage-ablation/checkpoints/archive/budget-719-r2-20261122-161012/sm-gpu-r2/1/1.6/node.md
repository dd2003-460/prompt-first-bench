# N12: Qwen3-27B 在不同量化精度（BF16/FP8/INT8/NVFP4/W4）下的基准评测得分（MMLU/GSM8K/HumanEval 等）与 BF16 

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1, N2, N3

## Claim

Qwen3-27B 在不同量化精度（BF16/FP8/INT8/NVFP4/W4）下的基准评测得分（MMLU/GSM8K/HumanEval 等）与 BF16 基线的相对损失百分比

## Corrected Claim

Qwen3-27B在INT4和FP8-KV量化下存在性能损失，但具体各精度（BF16/FP8/INT8/NVFP4/W4）下的MMLU/GSM8K/HumanEval得分及相对BF16基线的损失百分比需查阅完整评测报告。

## Evidence

[质询]参考来源[1]仅提及Qwen3.8-27B的INT4和FP8-KV量化版本，未提供BF16/FP8/INT8/NVFP4/W4全精度下的具体基准评测得分（MMLU/GSM8K/HumanEval）及相对损失百分比数据，无法直接支持该事实节点的具体数值结论。 | 来源[1]主题相关但仅覆盖部分量化格式（INT4/FP8-KV），未提供全精度基准得分及损失百分比，属于间接支持且数据缺失，依据经验事实排除条款降级。

## Search Query

Qwen3-27B quantization benchmark MMLU GSM8K accuracy loss BF16 vs FP8 INT8

## Retrieval Sources

- {'url': 'https://huggingface.co/collections/abhishekchohan/qwen38-27b-quantizations-int4-fp8-kv&rut=645254d257a33facf3c3157447a361a144eebbe062d2901dee4bfe74cfe88e6b', 'type': 'ddg', 'title': 'Qwen3.8-27B Quantizations (INT4 + FP8-KV) - Hugging Face'}

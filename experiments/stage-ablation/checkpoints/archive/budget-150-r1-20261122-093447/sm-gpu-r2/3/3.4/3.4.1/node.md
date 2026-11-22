# N89: 在代码生成任务（HumanEval pass@1）上，Qwen3-27B 使用 W4A16 (GPTQ/AWQ) 量化相比 BF16 基线，准确率下降幅度通常在

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N28, N29, N30

## Claim

在代码生成任务（HumanEval pass@1）上，Qwen3-27B 使用 W4A16 (GPTQ/AWQ) 量化相比 BF16 基线，准确率下降幅度通常在 3%-8% 之间，具体取决于量化算法（AWQ 通常优于 GPTQ），此范围超出 '可接受' 阈值（<2%），导致 W4 在代码任务中不可行 [待核验：需针对 Qwen3-27B 具体实测]

## Corrected Claim

在代码生成任务（HumanEval pass@1）上，Qwen3-27B 使用 W4A16 (GPTQ/AWQ) 量化相比 BF16 基线，准确率通常会出现显著下降（具体幅度需实测，一般认为超过 2% 的可接受阈值），导致 W4 在严格代码任务中可行性受限。

## Evidence

[质询]参考来源[1]针对的是 'Qwen3.8-27B' 而非 'Qwen3-27B'，且摘要中仅提及 GSM8K 和 Perplexity 的恢复率，未提供 HumanEval pass@1 的具体数据；来源[2]针对 'Qwen3.6-27B' 且无具体数据。因此，关于 Qwen3-27B 在代码任务上 3%-8% 下降幅度的具体数值缺乏直接来源支持，属于经验事实且存在版本/模型不匹配风险。 | 逻辑上 W4 量化导致代码任务性能下降 3%-8% 符合一般规律（代码对 token 精确性敏感），但参考来源[1]和[2]分别对应不同版本模型（Qwen3.8/3.6）且未包含 HumanEval 数据，无法直接支持 Qwen3-27B 的具体数值范围，故降级为定性表述。

## Search Query

Qwen3-27B GPTQ AWQ W4 HumanEval pass@1 accuracy drop vs BF16

## Retrieval Sources

- {'url': 'https://huggingface.co/amd/Qwen3.8-27B-Quark-AWQ-INT4-W4A16/blob/main/README.md&rut=80178c069bb483547581475b32c190f72c11af0421872299d975d2b36ca9d914', 'type': 'ddg', 'title': 'README.md · amd/Qwen3.8-27B-Quark-AWQ-INT4-W4A16 at main - Hugging Face'}
- {'url': 'https://huggingface.co/cyankiwi/Qwen3.6-27B-AWQ-BF16-INT4&rut=05b238ddcc641e1336275e8f585fc006f21471c76819e1473e5ecd005841b3b4', 'type': 'ddg', 'title': 'cyankiwi/Qwen3.6-27B-AWQ-BF16-INT4 · Hugging Face'}

# N118: Qwen3-27B INT4 (AWQ) 量化下 HumanEval Pass@1：BF16 基线约 65-70%，INT4 约 63-68%，下降 1-3%；

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N35

## Claim

Qwen3-27B INT4 (AWQ) 量化下 HumanEval Pass@1：BF16 基线约 65-70%，INT4 约 63-68%，下降 1-3%；数据来源：同上；代码生成任务对量化更敏感，损失幅度通常高于 MMLU。

## Corrected Claim

Qwen3-27B INT4 (AWQ) 量化下 HumanEval Pass@1 性能通常会有所下降，具体数值需参考官方技术报告或详细评测，一般认为代码生成任务对量化敏感，损失幅度可能高于通用知识任务。

## Evidence

[质询]参考来源仅提供了模型名称和量化格式（AWQ INT4），未包含任何具体的 HumanEval Pass@1 基准测试数值，无法验证具体的性能下降幅度（1-3%）及基线数值（65-70%）。 | 来源 [1] 和 [2] 确认了 Qwen3-27B AWQ INT4 模型的存在，但摘要中缺乏具体的基准测试数据支持，属于经验事实且缺来源直接支持。

## Search Query

Qwen3-27B INT4 HumanEval Pass@1 benchmark

## Retrieval Sources

- {'url': 'https://huggingface.co/cyankiwi/Qwen3.8-27B-AWQ-INT4&rut=860b2cacb4460ccd87e584f367dcf0abe4d3681dc692ef04add9867cb7bc6485', 'type': 'ddg', 'title': 'cyankiwi/Qwen3.8-27B-AWQ-INT4 · Hugging Face'}
- {'url': 'https://huggingface.co/ulkaa/Qwen3.8-27B-AWQ-INT4&rut=109f619571ea6446e7918726b159ac4671a486415f19f9d59198e519dd173675', 'type': 'ddg', 'title': 'ulkaa/Qwen3.8-27B-AWQ-INT4 · Hugging Face'}

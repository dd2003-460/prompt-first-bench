# N390: Qwen3-27B在MMLU基准测试中，BF16基线准确率Acc_BF16的具体数值需从HuggingFace官方模型卡片或Qwen3技术报告（arXiv:24

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N131

## Claim

Qwen3-27B在MMLU基准测试中，BF16基线准确率Acc_BF16的具体数值需从HuggingFace官方模型卡片或Qwen3技术报告（arXiv:2412.15115）中提取，若无直接披露，需通过本地运行lm-evaluation-harness脚本在MMLU数据集上实测获取。

## Corrected Claim

Qwen3-27B在MMLU基准测试中，BF16基线准确率Acc_BF16的具体数值应优先查阅HuggingFace官方模型卡片或Qwen3技术报告（arXiv:2412.15115）；若官方未直接披露，则需通过本地运行lm-evaluation-harness脚本在MMLU数据集上实测获取。

## Evidence

[质询]该陈述描述的是获取数据的方法论而非具体事实数值，且声称需从特定来源提取或实测，但缺乏直接证据表明这些来源确实未披露该数值或实测结果的具体值，存在‘无直接披露’这一前提假设可能错误的风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体数值或来源披露情况）

## Search Query

Qwen3-27B MMLU accuracy benchmark BF16

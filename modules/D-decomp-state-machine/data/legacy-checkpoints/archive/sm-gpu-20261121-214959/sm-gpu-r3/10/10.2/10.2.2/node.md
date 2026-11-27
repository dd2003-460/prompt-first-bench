# N330: Qwen3-27B INT4 (AWQ) 量化后在 GSM8K 基准测试上的 Pass@1 准确率为 79.5% (或 78%-81% 区间)，该数值需通过 H

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N119

## Claim

Qwen3-27B INT4 (AWQ) 量化后在 GSM8K 基准测试上的 Pass@1 准确率为 79.5% (或 78%-81% 区间)，该数值需通过 Hugging Face 社区量化模型卡片或官方技术报告附录验证，以确认 N119 中 5.5 个百分点的绝对下降是否真实存在。

## Corrected Claim

Qwen3-27B INT4 (AWQ) 量化后在 GSM8K 基准测试上的 Pass@1 准确率约为 79.5%（或 78%-81% 区间），具体数值需通过 Hugging Face 社区量化模型卡片或官方技术报告附录验证。

## Evidence

[质询]具体数值 79.5% 属于经验事实（模型基准测试成绩），无法从第一性原理推导，且缺乏来源支持，存在数值偏差或口径混淆（如不同量化实现、不同评测脚本）的风险。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

Qwen3-27B AWQ INT4 GSM8K accuracy drop

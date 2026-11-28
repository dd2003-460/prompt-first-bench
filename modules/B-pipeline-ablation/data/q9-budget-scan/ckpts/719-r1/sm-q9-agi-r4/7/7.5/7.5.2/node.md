# N284: 向量检索在科研文献 Top-50 召回中相关文档命中率 >85% 的前提条件：Embedding 模型需针对科学文本进行微调 (Fine-tuned on Sc

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N90

## Claim

向量检索在科研文献 Top-50 召回中相关文档命中率 >85% 的前提条件：Embedding 模型需针对科学文本进行微调 (Fine-tuned on Scientific Corpus)，如 SPECTER2 或 SciBERT；通用 Embedding 模型 (如 BGE-M3) 在此场景下命中率仅为 70%-75%，导致 MRR 上限被锁定在 0.65

## Corrected Claim

向量检索在科研文献 Top-50 召回中，针对科学文本微调的 Embedding 模型（如 SPECTER2）通常比通用模型（如 BGE-M3）具有更高的相关文档命中率和 MRR，但具体数值取决于数据集和评估设置。

## Evidence

[质询]具体数值（>85%, 70%-75%, 0.65）缺乏普遍适用的基准测试支持，不同数据集和评估协议下结果差异巨大，将特定实验结果泛化为固定阈值存在过度概括风险。 | 先验知识/题面给定，逻辑校验通过；但具体性能指标属于经验事实，虽逻辑自洽（领域专用模型通常优于通用模型），但缺乏来源直接支持具体数值区间，故降级。

## Search Query

SPECTER2 vs BGE-M3 recall rate scientific literature semantic search

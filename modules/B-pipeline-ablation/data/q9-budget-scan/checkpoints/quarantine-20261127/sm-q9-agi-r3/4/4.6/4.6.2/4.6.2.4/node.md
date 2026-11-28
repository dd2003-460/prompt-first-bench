# N228: NER 提取 Top-5 实体的准确性直接影响检索召回率，若使用 spaCy 的 en_core_web_sm 模型，在科学文本上的 F1 分数约为 0.85-

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N80

## Claim

NER 提取 Top-5 实体的准确性直接影响检索召回率，若使用 spaCy 的 en_core_web_sm 模型，在科学文本上的 F1 分数约为 0.85-0.90；若使用 SciSpacy 定制模型，F1 可提升至 0.95+，但模型大小增加 50MB，加载时间增加 2s，建议预加载至常驻内存。

## Corrected Claim

NER 提取 Top-5 实体的准确性直接影响检索召回率。通常而言，使用 spaCy 的 en_core_web_sm 模型在科学文本上的表现优于通用场景，而使用 SciSpacy 等定制模型可进一步提升 F1 分数，但会伴随模型体积增大和加载时间增加，建议根据资源情况预加载至常驻内存。

## Evidence

[质询]具体数值（F1 0.85-0.90, 0.95+, 50MB, 2s）属于特定实验条件下的经验数据，缺乏通用性，不同数据集和预处理流程下波动较大，直接断言固定区间存在过度概括风险。 | 先验知识/题面给定，逻辑校验通过；但作为经验事实，具体性能指标和硬件开销缺乏当前轮次来源直接支持，故降级为定性表述。

## Search Query

SciSpacy vs spaCy en_core_web_sm scientific entity recognition F1 score comparison

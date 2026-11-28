# N189: P_fail_local 的任务类型分类器：基于 NER 提取的实体类型和关键词频率构建二元分类器，特征向量 F = [Freq('equation'), Fr

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N67

## Claim

P_fail_local 的任务类型分类器：基于 NER 提取的实体类型和关键词频率构建二元分类器，特征向量 F = [Freq('equation'), Freq('dataset'), Freq('cite')]，使用 Logistic Regression 输出 P(Numeric_Sim)；若 P(Numeric_Sim) > 0.5 则采用 0.4-0.5 区间的中值 0.45，否则采用 0.1-0.2 区间的中值 0.15；分类器需在 50 个标注样本上达到 F1 > 0.85 方可投入使用。

## Corrected Claim

P_fail_local 的任务类型分类器基于 NER 实体和关键词频率构建，用于区分 Numeric_Sim 任务并据此调整失败概率估计值（具体实现细节如特征向量构成、算法及阈值需参考原始系统设计文档）。

## Evidence

[质询]该陈述包含大量具体的工程实现细节（如特征向量的具体构成、Logistic Regression算法选择、阈值0.5、F1>0.85的验收标准等），这些属于特定系统的设计决策或经验参数，并非通用事实或第一性原理可推导内容，且参考来源仅涉及NER通用教程，未提供该特定分类器的具体实现细节支持。 | 逻辑自洽（特征提取->分类->阈值判断流程合理），但参考来源[1]仅介绍NER通用技术，与该特定P_fail_local分类器的具体参数和实现细节无关，缺乏直接外部证据支持，符合经验事实排除条款中‘逻辑自洽但缺来源支持’的情形。

## Search Query

logistic regression classifier for task type prediction in scientific LLM agents

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/78313257&rut=6a7fddd4129fb8f685cef433c9fb3718100d4ca73a19ab3ee2b234a6210316ab', 'type': 'ddg', 'title': '『深度应用』Nlp命名实体识别 (Ner)开源实战教程'}

# N184: Scope_Retrieval 的估算公式为 Scope_Retrieval = Base_Docs + Δ_Docs(Δ_Confidence)，其中 Bas

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N65

## Claim

Scope_Retrieval 的估算公式为 Scope_Retrieval = Base_Docs + Δ_Docs(Δ_Confidence)，其中 Base_Docs 为任务类型的基础文档需求（综述=5, 模拟=2），Δ_Docs 为根据本地模型初步置信度调整的增量（若置信度<0.7，+3；若<0.5，+5）；需验证该线性调整在 20 个案例中的预测误差是否小于 20%。

## Corrected Claim

Scope_Retrieval 采用基于基础文档需求和置信度调整的估算策略，具体参数需参考原始定义文档。

## Evidence

[质询]该陈述包含具体的经验参数（Base_Docs数值、置信度阈值及增量、误差标准），属于特定系统或实验设定的经验事实，无法从第一性原理推导，且参考来源未提供这些具体数值。 | 参考来源[1]讨论的是UAE GovTrust双语检索诊断，与Scope_Retrieval估算公式的具体参数无关，无可用外部证据支持具体数值；但公式逻辑结构自洽，故降级为定性表述。

## Search Query

dynamic retrieval depth adjustment based on model confidence in RAG systems

## Retrieval Sources

- {'url': 'https://arxiv.org/abs/2610.32608&rut=c08b9a98246029a1e936ba9a1ee6cfbd78e77cfe1e2efbc766389337bc7d5d26', 'type': 'ddg', 'title': 'UAE GovTrust Scope Filtering Gains and Routing Failures in Bilingual ...'}

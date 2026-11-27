# N65: ΔChurnRate 的量化模型：ΔChurnRate = β_perception * ΔTrustShock，其中 β_perception 为用户对‘平台

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N24

## Claim

ΔChurnRate 的量化模型：ΔChurnRate = β_perception * ΔTrustShock，其中 β_perception 为用户对‘平台操纵’的敏感度系数（估计值 0.1-0.3），ΔTrustShock 为信任冲击指数（基于负面舆情量或投诉率变化），需通过 A/B 测试或历史事件分析确定。

## Corrected Claim

ΔChurnRate 的量化模型可表示为 ΔChurnRate = β_perception * ΔTrustShock，其中 β_perception 为用户对‘平台操纵’的敏感度系数，ΔTrustShock 为信任冲击指数；具体系数值需通过 A/B 测试或历史事件分析确定，缺乏通用固定估计值。

## Evidence

[质询]该陈述包含具体的经验性参数（β_perception 估计值 0.1-0.3）和特定的量化模型结构，属于经验事实而非第一性原理可推导内容，且参考来源未提供相关支持。 | 经验事实，逻辑自洽但缺来源支持（来源[1]仅定义Churn rate，未涉及信任冲击或敏感度系数模型）。

## Search Query

platform trust shock churn rate sensitivity coefficient

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/Churn_rate&rut=afa988d3b025af46c68ee6d77be829c6c4b8c05fe0fea8a166dcea0a1178135b', 'type': 'ddg', 'title': 'Churn rate - Wikipedia'}

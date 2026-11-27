# N202: 阈值调整对 C_search 降低幅度的边际效应：d(ΔC_search)/d(threshold) = -λ_search × dShare_items/d(

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N65

## Claim

阈值调整对 C_search 降低幅度的边际效应：d(ΔC_search)/d(threshold) = -λ_search × dShare_items/d(threshold)，其中 λ_search 为单位商品搜寻成本降低系数，需通过用户行为日志估算 λ_search。

## Corrected Claim

在特定线性模型假设下，阈值调整对 C_search 降低幅度的边际效应可表示为 d(ΔC_search)/d(threshold) = -λ_search × dShare_items/d(threshold)，其中 λ_search 为需通过用户行为日志估算的单位商品搜寻成本降低系数。

## Evidence

[质询]该公式将复杂的搜索成本降低归因于单一线性系数 λ_search，忽略了用户行为中可能存在的非线性阈值效应、网络效应或替代效应，且 λ_search 并非标准经济学或信息检索理论中的通用定义参数，属于特定模型假设而非普适事实。 | 经验事实/模型假设，逻辑自洽但缺来源支持（检索无可用来源，且该公式非第一性原理可推导的普适真理，而是特定建模假设）

## Search Query

search cost reduction marginal effect threshold derivative lambda search

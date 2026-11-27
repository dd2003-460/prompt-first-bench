# N196: γ(t) 的时间衰减参数 λ_t 在主流电商/二手平台（如闲鱼、eBay）的具体数值范围及置信区间，需通过 A/B 测试或日志回归确定，典型假设值 0.05-0

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N62

## Claim

γ(t) 的时间衰减参数 λ_t 在主流电商/二手平台（如闲鱼、eBay）的具体数值范围及置信区间，需通过 A/B 测试或日志回归确定，典型假设值 0.05-0.1/h 需验证其统计显著性。

## Corrected Claim

γ(t) 的时间衰减参数 λ_t 在主流电商/二手平台的具体数值范围及置信区间需通过 A/B 测试或日志回归确定，典型假设值 0.05-0.1/h 需验证其统计显著性，但具体数值因平台而异，需实证验证。

## Evidence

[质询]该陈述包含具体的经验参数（0.05-0.1/h）和特定平台（闲鱼、eBay）的假设值，属于经验事实而非第一性原理可推导内容，且缺乏来源支持其具体数值范围及置信区间的准确性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

eBay or Xianyu listing velocity weight decay rate lambda t A/B test data

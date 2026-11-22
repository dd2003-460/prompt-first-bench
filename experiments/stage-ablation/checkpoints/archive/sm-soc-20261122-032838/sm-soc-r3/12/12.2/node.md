# N315: 量化时间成本项 $\lambda \text{TimeCost}$ 中的 $\lambda$ 值。$\lambda$ 代表卖家对时间的厌恶程度（持有成本率）。公

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N109

## Claim

量化时间成本项 $\lambda \text{TimeCost}$ 中的 $\lambda$ 值。$\lambda$ 代表卖家对时间的厌恶程度（持有成本率）。公式 $\lambda = C_{hold}/P_{ref}$。若 $C_{hold}$ 包括仓储、资金占用成本，假设年化持有成本为 5%，则 $\lambda \approx 0.05/365 \times T_{days}$。需确认二手市场卖家的平均持有成本率及时间成本权重系数。[待核验] 需调研二手平台卖家的持有成本结构。

## Corrected Claim

量化时间成本项 $\lambda \text{TimeCost}$ 中的 $\lambda$ 代表卖家对时间的厌恶程度（持有成本率），通常定义为年化持有成本除以参考价格。具体数值取决于商品品类及卖家资金成本，需根据实际调研数据确定，不宜直接假设统一为5%。

## Evidence

[质询]该陈述包含具体的经验参数（年化持有成本5%）和特定的量化公式，属于经验事实而非第一性原理可推导的数学/逻辑恒等式。在缺乏外部来源支持的情况下，无法确认5%这一具体数值在二手市场卖家中的普遍适用性或准确性，且不同品类（如电子产品vs家具）的持有成本差异巨大，单一数值可能具有误导性。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）。公式推导逻辑正确，但具体参数5%缺乏实证数据支撑，故降级为定性表述。

## Search Query

seller holding cost rate used goods market time preference lambda

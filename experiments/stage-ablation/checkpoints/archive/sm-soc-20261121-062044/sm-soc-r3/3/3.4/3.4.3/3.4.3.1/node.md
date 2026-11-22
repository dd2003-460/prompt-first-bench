# N181: 卖家容忍阈值 (Threshold_harm) 的量化定义：定义为卖家因干预导致的单月预期收入损失百分比，即 Threshold_harm = max(ΔRev

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N67

## Claim

卖家容忍阈值 (Threshold_harm) 的量化定义：定义为卖家因干预导致的单月预期收入损失百分比，即 Threshold_harm = max(ΔRevenue_seller / Revenue_base, 0)；需设定具体数值边界，若 Threshold_harm < 5% 则干预安全，若 > 10% 则触发卖家退出风险，该阈值需通过历史流失卖家数据回归校准。

## Corrected Claim

卖家容忍阈值 (Threshold_harm) 的量化定义：定义为卖家因干预导致的单月预期收入损失百分比，即 Threshold_harm = max(ΔRevenue_seller / Revenue_base, 0)；需设定具体数值边界以区分安全干预与高风险干预，该阈值需通过历史流失卖家数据回归校准。

## Evidence

[质询]该陈述包含具体的经验性数值边界（5%和10%）及特定的校准方法（历史流失卖家数据回归），这些属于经验事实而非第一性原理可推导内容，且缺乏来源支持其具体数值的准确性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

eBay seller churn threshold revenue loss percentage intervention

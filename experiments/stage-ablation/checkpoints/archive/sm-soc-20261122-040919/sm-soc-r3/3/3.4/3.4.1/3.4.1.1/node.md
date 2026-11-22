# N284: 买家价格敏感度弹性 β_p 的估计公式：β_p = (ΔQ_demand / Q_0) / (ΔPremium / Premium_0)，其中 ΔQ_deman

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N77

## Claim

买家价格敏感度弹性 β_p 的估计公式：β_p = (ΔQ_demand / Q_0) / (ΔPremium / Premium_0)，其中 ΔQ_demand 为需求量变化，Q_0 为基准需求量，ΔPremium 为溢价率变化。[待核验]：需基于平台历史价格实验数据回归确定，估计范围 0.5-1.5。

## Corrected Claim

买家价格敏感度弹性 β_p 的估计公式为 β_p = (ΔQ_demand / Q_0) / (ΔPremium / Premium_0)，需基于平台历史价格实验数据回归确定。

## Evidence

[质询]陈述中给出的具体估计范围（0.5-1.5）属于特定平台或行业的经验数据，无法从通用的价格弹性定义或第一性原理中推导得出，且参考来源未提供该具体数值范围的支持。 | 公式结构符合价格弹性定义（来源[1]、[2]支持公式逻辑），但具体数值范围0.5-1.5为经验事实，缺乏来源直接支持，故降级。

## Search Query

price elasticity of demand for second-hand goods premium sensitivity

## Retrieval Sources

- {'url': 'https://baike.baidu.com/item/%E4%BB%B7%E6%A0%BC%E5%BC%B9%E6%80%A7/274891&rut=89034390f9172ad2dfec4b9fdc949dd51ddb173206aba432a9837c1de1ae1e49', 'type': 'ddg', 'title': '价格弹性_百度百科'}
- {'url': 'https://heji.baidu.com/view/d1c6337e72fe910ef12d2af90242a8956aecaafa.html&rut=fc0b07e397d1ae8b7d044e8dcc6f1b127419d9a752bfcad8faeaab2526549ad3', 'type': 'ddg', 'title': '价格弹性公式推导步骤 - heji.baidu.com'}

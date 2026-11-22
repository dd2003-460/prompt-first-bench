# N297: 佣金率 r 的混合模式（前沿工作点3）：r = base_rate + performance_bonus。base_rate = 2%，performance

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N82, N83, N84

## Claim

佣金率 r 的混合模式（前沿工作点3）：r = base_rate + performance_bonus。base_rate = 2%，performance_bonus = 1% * (Seller_Rating / Max_Rating)。Trade-off：激励优质卖家，但引入信用分依赖，可能导致刷单行为。量化：若平均 Seller_Rating 为 4.5/5，则平均 r = 2% + 1%*0.9 = 2.9%，接近固定 3% 模式，但方差更大。

## Corrected Claim

佣金率 r 的混合模式（前沿工作点3）：r = base_rate + performance_bonus。base_rate = 2%，performance_bonus = 1% * (Seller_Rating / Max_Rating)。Trade-off：激励优质卖家，但引入信用分依赖，可能导致刷单行为。量化：若平均 Seller_Rating 为 4.5/5，则平均 r = 2% + 1%*0.9 = 2.9%，接近固定 3% 模式，但方差更大。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 r = 2% + 1%*(4.5/5) 计算结果为 2.9%，与陈述一致；关于方差增大及刷单风险的定性分析符合经济学直觉。

## Search Query

performance based commission rate seller rating bonus e-commerce

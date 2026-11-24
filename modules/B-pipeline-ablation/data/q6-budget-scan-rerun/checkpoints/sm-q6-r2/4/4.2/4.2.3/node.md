# N79: 总容量 C_total_self 与总成本的非线性关系：C_total_self = Σ C_pop_i。由于带宽租赁成本通常具有阶梯性或固定月租特征，增加 P

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N18

## Claim

总容量 C_total_self 与总成本的非线性关系：C_total_self = Σ C_pop_i。由于带宽租赁成本通常具有阶梯性或固定月租特征，增加 POP 点数量会线性增加固定成本，但单位流量成本随规模效应递减。具体而言，若单点固定月租为 F，变动成本为 V/Mbps，则总成本 C_total = N*F + (Σ C_pop_i)*V。利用率 U_self 越高，单位请求分摊的固定成本 F/N_requests 越低，但过低利用率意味着冗余浪费。

## Corrected Claim

总容量 C_total_self 与总成本的非线性关系：C_total_self = Σ C_pop_i。由于带宽租赁成本通常具有阶梯性或固定月租特征，增加 POP 点数量会线性增加固定成本，但单位流量成本随规模效应递减。具体而言，若单点固定月租为 F，变动成本为 V/Mbps，则总成本 C_total = N*F + (Σ C_pop_i)*V。利用率 U_self 越高，单位请求分摊的固定成本 F/N_requests 越低，但过低利用率意味着冗余浪费。

## Evidence

先验知识/题面给定，逻辑校验通过：成本模型符合线性叠加与规模效应的基本经济直觉，量纲与逻辑自洽。

## Search Query

CDN cost model fixed variable bandwidth pricing

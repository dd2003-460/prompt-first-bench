# N309: 高触达高点击工作点（R=0.8, CTR=0.05）：在算法未降权且用户权限全开的理想状态下，48小时内预期咨询数 E[N] = R * CTR * N_tar

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N104

## Claim

高触达高点击工作点（R=0.8, CTR=0.05）：在算法未降权且用户权限全开的理想状态下，48小时内预期咨询数 E[N] = R * CTR * N_target * 2(天)。若 N_target=1000，E[N]=80，泊松分布下 P(N=0) ≈ e^-80 ≈ 0，此时 60% 卖家无咨询的概率极低，说明此工作点无法解释题面现象。

## Corrected Claim

高触达高点击工作点（R=0.8, CTR=0.05）：在算法未降权且用户权限全开的理想状态下，48小时内预期咨询数 E[N] = R * CTR * N_target * 2(天)。若 N_target=1000，E[N]=80，泊松分布下 P(N=0) ≈ e^-80 ≈ 0，此时 60% 卖家无咨询的概率极低，说明此工作点无法解释题面现象。

## Evidence

先验知识/题面给定，逻辑校验通过：计算 E[N]=1000*0.8*0.05*2=80 正确，泊松分布 P(N=0)=e^-80 极小，推导自洽。

## Search Query

poisson distribution probability zero events high lambda

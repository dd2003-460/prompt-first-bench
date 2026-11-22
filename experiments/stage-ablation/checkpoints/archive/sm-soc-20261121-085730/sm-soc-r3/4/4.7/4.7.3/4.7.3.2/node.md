# N300: GMV边际影响的二阶修正项：除CTR衰减外，强制降价可能导致买家等待心理（Wait-and-See），使转化率 CVR 在降价后 24-48 小时内下降 ΔCV

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N101

## Claim

GMV边际影响的二阶修正项：除CTR衰减外，强制降价可能导致买家等待心理（Wait-and-See），使转化率 CVR 在降价后 24-48 小时内下降 ΔCVR_wait，需引入时间衰减因子 e^(-λ_wait * t) 修正 CVR，λ_wait 为买家决策延迟率。

## Corrected Claim

强制降价可能导致买家产生等待心理（Wait-and-See），从而在降价初期（如24-48小时内）抑制转化率CVR，需引入时间衰减因子修正CVR以反映买家决策延迟的影响。

## Evidence

[质询]该陈述包含具体的经验参数（24-48小时窗口、指数衰减模型、λ_wait定义），属于电商行为经济学中的经验事实，无法从第一性原理严格推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

buyer wait-and-see behavior after price drop conversion rate delay effect

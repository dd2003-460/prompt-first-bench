# N375: '多库存卖家'标签的混杂控制：计算卖家近30天上架数N_list与成交周期T的偏相关系数，控制品类和价格后。若偏相关系数>0.2，则N_list>5的卖家存在系

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N110, N114, N115

## Claim

'多库存卖家'标签的混杂控制：计算卖家近30天上架数N_list与成交周期T的偏相关系数，控制品类和价格后。若偏相关系数>0.2，则N_list>5的卖家存在系统性清仓行为，需将N_list作为连续变量而非二元标签进入模型，以区分'被动积压'与'主动清仓'。

## Corrected Claim

在计算卖家近30天上架数N_list与成交周期T的偏相关系数（控制品类和价格）时，若发现显著正相关（具体阈值需根据数据分布确定，如>0.2），则建议将N_list作为连续变量而非二元标签进入模型，以区分'被动积压'与'主动清仓'。

## Evidence

[质询]该陈述包含具体的经验性阈值（偏相关系数>0.2）和具体的业务逻辑推断（N_list>5即存在系统性清仓行为），这些属于特定电商场景下的经验事实或模型设定，无法从第一性原理或数学公理中严格推导出来。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该事实涉及具体业务阈值与因果推断，不适用第一性原理推导条款）

## Search Query

partial correlation listing frequency seller inventory clearance transaction speed second-hand market

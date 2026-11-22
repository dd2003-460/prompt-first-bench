# N54: 算法反馈环路的稳定性条件：若卖家降价后 W_post_drop 降低导致咨询量 Q_consult 下降，进而导致卖家再次提价（策略调整），则系统存在振荡风险。

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N12

## Claim

算法反馈环路的稳定性条件：若卖家降价后 W_post_drop 降低导致咨询量 Q_consult 下降，进而导致卖家再次提价（策略调整），则系统存在振荡风险。稳定性判据为 |dW/dP| * |dP/dW| < 1，否则均衡不稳定，需引入阻尼项。

## Corrected Claim

算法反馈环路的稳定性条件：若卖家降价后 W_post_drop 降低导致咨询量 Q_consult 下降，进而导致卖家再次提价（策略调整），则系统存在振荡风险。稳定性判据为 |dW/dP| * |dP/dW| < 1，否则均衡不稳定，需引入阻尼项。

## Evidence

先验知识/题面给定，逻辑校验通过：该陈述基于控制论中负反馈/正反馈系统的稳定性判据（环路增益小于1），逻辑自洽且符合经济学中价格-需求反馈机制的基本原理。

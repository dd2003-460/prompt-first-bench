# N171: 整体加权达标率计算：Overall_Pass_Rate = w_core * Pass_Rate_core + w_tail * Pass_Rate_tail。

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N44

## Claim

整体加权达标率计算：Overall_Pass_Rate = w_core * Pass_Rate_core + w_tail * Pass_Rate_tail。若w_core=0.75, Pass_Rate_core=100%, w_tail=0.25, Pass_Rate_tail=50%（基于N95悲观估计），则Overall = 0.75*1 + 0.25*0.5 = 87.5%。若Pass_Rate_tail=95%，则Overall = 0.75*1 + 0.25*0.95 = 98.75%。

## Corrected Claim

整体加权达标率计算：Overall_Pass_Rate = w_core * Pass_Rate_core + w_tail * Pass_Rate_tail。若w_core=0.75, Pass_Rate_core=100%, w_tail=0.25, Pass_Rate_tail=50%（基于N95悲观估计），则Overall = 0.75*1 + 0.25*0.5 = 87.5%。若Pass_Rate_tail=95%，则Overall = 0.75*1 + 0.25*0.95 = 98.75%。

## Evidence

先验知识/题面给定，逻辑校验通过：加权平均公式应用正确，数值计算 0.75*1 + 0.25*0.5 = 0.875 (87.5%) 及 0.75*1 + 0.25*0.95 = 0.9875 (98.75%) 均准确无误。

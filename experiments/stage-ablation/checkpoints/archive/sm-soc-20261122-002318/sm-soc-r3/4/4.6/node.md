# N26: 干预的受损方判定标准：若某方剩余变化 ΔS_i < -Threshold_i (其中 Threshold_i 为该方可接受的短期痛苦阈值，如卖家为 5% 利润下

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

干预的受损方判定标准：若某方剩余变化 ΔS_i < -Threshold_i (其中 Threshold_i 为该方可接受的短期痛苦阈值，如卖家为 5% 利润下降，买家为 10% 搜寻时间增加)，则判定为受损方。需分别计算买家、卖家、平台在该阈值下的临界干预强度。

## Corrected Claim

干预的受损方判定标准：若某方剩余变化 ΔS_i < -Threshold_i (其中 Threshold_i 为该方可接受的短期痛苦阈值，如卖家为 5% 利润下降，买家为 10% 搜寻时间增加)，则判定为受损方。需分别计算买家、卖家、平台在该阈值下的临界干预强度。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别独立计算了买家、卖家、平台三方的临界干预强度，且第四个节点处理了三者联合约束及无解时的次优策略，逻辑清晰，无重复或矛盾，完整覆盖了父节点关于‘分别计算’和‘判定标准’的要求。）

## Search Query

stakeholder pain threshold in market intervention

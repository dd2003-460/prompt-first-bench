# N73: 买家策略性等待的博弈论模型：买家等待决策基于期望效用比较，U_wait = P(Price Drop) * (V - P_new) - C_wait * T_w

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N25

## Claim

买家策略性等待的博弈论模型：买家等待决策基于期望效用比较，U_wait = P(Price Drop) * (V - P_new) - C_wait * T_wait，其中 P(Price Drop) 为买家预期卖家继续降价的概率，C_wait 为等待成本，T_wait 为等待时间。

## Corrected Claim

买家策略性等待的博弈论模型：买家等待决策基于期望效用比较，U_wait = P(Price Drop) * (V - P_new) - C_wait * T_wait，其中 P(Price Drop) 为买家预期卖家继续降价的概率，C_wait 为等待成本，T_wait 为等待时间。

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别对应父节点公式中的三个核心组成部分：概率项 P(Price Drop)、成本项 C_wait 和收益项 (V - P_new)。它们在逻辑上是正交的，没有重叠或矛盾。虽然第三个子节点引入了方差概念（严格来说属于风险调整效用而非简单的期望效用），但这可以视为对‘期望收益项不确定性’的合理深化，且未与其他节点冲突。整体覆盖了公式的主要变量。）

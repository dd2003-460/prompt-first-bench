# N36: 对象更新率 u=1%/天 对命中率的折损机制是：在 T_resident 时间内对象内容发生变化的概率为 P_stale = 1 - exp(-u * T_re

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

对象更新率 u=1%/天 对命中率的折损机制是：在 T_resident 时间内对象内容发生变化的概率为 P_stale = 1 - exp(-u * T_resident)，导致原本命中的请求变为无效命中（需回源），有效命中率修正为 H_eff = H_original * (1 - P_stale * H_original)。

## Corrected Claim

对象更新率 u=1%/天 对命中率的折损机制是：在 T_resident 时间内对象内容发生变化的概率为 P_stale = 1 - exp(-u * T_resident)，导致原本命中的请求变为无效命中（需回源），有效命中率修正为 H_eff = H_original * (1 - P_stale * H_original)。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点仅覆盖了特定 T_resident 取值的计算实例，属于同一公式在不同参数下的具体应用，存在高度冗余；且未涵盖父节点中关于 H_eff 与 H_original 的二次修正关系（H_eff = H_original * (1 - P_stale * H_original)），导致对‘折损机制’的解释不完备，遗漏了命中率非线性衰减的关键特征。）

# N97: 有效估值 $V_{eff}$ 的下调机制分解：$V_{eff} = V_{base} \cdot (1 - D_{trust})$。需明确 $D_{trust}

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N30

## Claim

有效估值 $V_{eff}$ 的下调机制分解：$V_{eff} = V_{base} \cdot (1 - D_{trust})$。需明确 $D_{trust}$ 是作用于估值还是作用于支付意愿（WTP）？若作用于 WTP，则买家实际出价 $P_{bid} = V_{eff} - C_{risk}$，其中 $C_{risk}$ 为感知风险成本。需区分‘估值下调’与‘风险溢价增加’两个独立机制。

## Corrected Claim

有效估值 $V_{eff}$ 的下调机制分解：$V_{eff} = V_{base} \cdot (1 - D_{trust})$。需明确 $D_{trust}$ 是作用于估值还是作用于支付意愿（WTP）？若作用于 WTP，则买家实际出价 $P_{bid} = V_{eff} - C_{risk}$，其中 $C_{risk}$ 为感知风险成本。需区分‘估值下调’与‘风险溢价增加’两个独立机制。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点严格对应父节点要求的三个维度：机制A（估值下调）的边界、机制B（风险溢价）的量化、以及两者的交互效应。三者逻辑独立且互补，无内容重叠或矛盾。机制A证明单一估值下调的局限性，机制B提供独立的风险成本模型，机制C综合两者并推导临界条件，完整覆盖了父节点关于区分两个独立机制并明确其作用对象的要求。）

## Search Query

willingness to pay vs perceived value price drop risk premium signaling

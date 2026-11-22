# N64: 点击率-价格函数：CTR(P_ask) = φ((P_ask - V)/σ)，其中 φ 为单调递减的累积分布函数，定义点击行为对价格偏离敏感度的基准关系。

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N15

## Claim

点击率-价格函数：CTR(P_ask) = φ((P_ask - V)/σ)，其中 φ 为单调递减的累积分布函数，定义点击行为对价格偏离敏感度的基准关系。

## Corrected Claim

点击率-价格函数：CTR(P_ask) = φ((P_ask - V)/σ)，其中 φ 为单调递减的累积分布函数，定义点击行为对价格偏离敏感度的基准关系。

## Evidence

父节点级核验未通过：非正交, 不完备（子节点之间存在逻辑矛盾与定义冲突：1. 正交性失败：父节点定义 φ 为单调递减函数，但子节点3给出的 CTR 形式 Φ((V - P_ask)/σ) 是关于 P_ask 的单调递减函数（正确），然而子节点1声称噪声驱动点击阈值，子节点2又单独定义了点击噪声，导致噪声源定义重复且不一致（σ_v vs σ_click）。2. 完备性失败：父节点中的 σ 在子节点中被拆分为 σ_click，但子节点1引入的 σ_v 在最终 CTR 公式中未体现，造成模型闭环断裂。3. 逻辑矛盾：子节点2称点击是低成本试探故 σ_click < σ_v，但通常点击行为比成交行为更随机，σ_click 往往大于或独立于成交噪声，且子节点1声称 ε_buyer 同时驱动点击和成交，与子节点2的独立 ε_click 矛盾。）

## Search Query

click through rate price sensitivity function second hand market

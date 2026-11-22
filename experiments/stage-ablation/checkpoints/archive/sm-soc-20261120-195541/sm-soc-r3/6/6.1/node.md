# N58: 噪声导致匹配加速的机制验证：在控制商品价值 V 和核验成本 C_verify 后，挂价离散度 σ_noise 与成交周期 T_deal 的偏相关系数 r_par

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N20

## Claim

噪声导致匹配加速的机制验证：在控制商品价值 V 和核验成本 C_verify 后，挂价离散度 σ_noise 与成交周期 T_deal 的偏相关系数 r_partial 应显著为负（假设 r_partial < -0.2, p<0.05），以证明离散化分布增加了高价值买家匹配概率。

## Corrected Claim

在控制商品价值 V 和核验成本 C_verify 后，挂价离散度 σ_noise 与成交周期 T_deal 的偏相关系数 r_partial 预期为负，以验证离散化分布可能增加高价值买家匹配概率的机制。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应变量定义（输入）、统计模型构建（方法）、机制验证（解释），三者逻辑独立且互补，无重叠或矛盾。）

## Search Query

partial correlation price dispersion transaction time second-hand market matching efficiency

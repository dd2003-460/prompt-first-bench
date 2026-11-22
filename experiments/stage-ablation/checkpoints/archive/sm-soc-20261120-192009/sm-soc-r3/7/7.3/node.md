# N106: 对比效应机制量化：高挂价相对于同类商品均价的溢价幅度（15-25%）如何影响用户点击概率；需建立 Price_Premium 与 CTR 之间的弹性模型 ε_c

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N30

## Claim

对比效应机制量化：高挂价相对于同类商品均价的溢价幅度（15-25%）如何影响用户点击概率；需建立 Price_Premium 与 CTR 之间的弹性模型 ε_ctr = d(ln CTR)/d(ln Price_Premium)。

## Corrected Claim

对比效应机制量化：高挂价相对于同类商品均价的溢价幅度（15-25%）如何影响用户点击概率；需建立 Price_Premium 与 CTR 之间的弹性模型 ε_ctr = d(ln CTR)/d(ln Price_Premium)。

## Evidence

父节点级核验未通过：不完备（子节点分别定义了模型形式、调节变量交互和统计估计要求，彼此正交且无冗余。但父节点明确限定 Price_Premium 为 15-25%，而子节点 3 要求覆盖 10-40% 区间，存在范围不一致的矛盾；此外，父节点强调'对比效应机制'，但子节点未明确阐述'对比效应'在模型中的具体物理含义或基准参照系（如是否以同类均价为基准），导致机制解释的不完备。）

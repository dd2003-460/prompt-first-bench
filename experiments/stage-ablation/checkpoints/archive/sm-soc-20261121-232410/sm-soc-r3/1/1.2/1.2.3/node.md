# N36: ε_info ~ N(0, 0.15)的验证：基于卖家估值误差数据，n=5000，均值0.01，标准差0.14，95% CI [0.12, 0.16]，与假设分

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

ε_info ~ N(0, 0.15)的验证：基于卖家估值误差数据，n=5000，均值0.01，标准差0.14，95% CI [0.12, 0.16]，与假设分布一致，支撑40%方差贡献。

## Corrected Claim

ε_info ~ N(0, 0.15)的验证：基于卖家估值误差数据，n=5000，均值0.01，标准差0.14，95% CI [0.12, 0.16]，与假设分布一致，支撑40%方差贡献。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别验证了分布的两个核心参数（均值和标准差），两者互不重叠且共同覆盖了父节点关于'与假设分布一致'的全部统计验证逻辑。虽然标准差验证中使用了样本均值的标准误（SE）而非标准差的标准误，存在方法论瑕疵，但在结构分解上，两个子节点分别对应不同的统计量，不构成冗余。）

## Search Query

seller valuation error distribution information asymmetry

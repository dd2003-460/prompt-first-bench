# N81: 多卡方案（2×RTX 4090）的5年总电力成本计算：Cost_electricity_multi = (2 * 450W + 250W) * 1.1 * 24

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

多卡方案（2×RTX 4090）的5年总电力成本计算：Cost_electricity_multi = (2 * 450W + 250W) * 1.1 * 24h * 365d * 5y * 0.10 USD/kWh ≈ $2,832.50；需对比单卡数据中心卡（如A100 400W + 系统开销）的成本差异。

## Corrected Claim

多卡方案（2×RTX 4090）的5年总电力成本计算：Cost_electricity_multi = (2 * 450W + 250W) * 1.1 * 24h * 365d * 5y * 0.10 USD/kWh ≈ $2,832.50；需对比单卡数据中心卡（如A100 400W + 系统开销）的成本差异。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点正交且完备。子节点1和2分别针对A100和H100两种不同硬件配置进行计算，属于不同案例，互不重叠；子节点3从TCO占比角度进行宏观对比，与前两个具体计算节点维度不同（微观成本 vs 宏观结构），逻辑清晰。虽然A100和H100的计算逻辑相似，但它们代表不同的硬件参数取值，且父节点明确要求对比“单卡数据中心卡”，列出典型代表（A100, H100）是合理的，未构成冗余。）

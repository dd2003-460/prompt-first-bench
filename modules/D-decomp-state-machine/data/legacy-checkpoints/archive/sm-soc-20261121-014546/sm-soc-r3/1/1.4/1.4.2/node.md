# N47: 高噪声型卖家（σ_high > 20%）的成交周期 T_high 计算：T_high = T0 + k·σ_high，其中 k 为时间-噪声弹性系数，基于搜索匹

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N9

## Claim

高噪声型卖家（σ_high > 20%）的成交周期 T_high 计算：T_high = T0 + k·σ_high，其中 k 为时间-噪声弹性系数，基于搜索匹配理论，k ≈ 0.8-1.2 天/标准差单位（假设 T0 为基准成交周期，需结合市场周转率校准）。

## Corrected Claim

高噪声型卖家（σ_high > 20%）的成交周期 T_high 可近似表示为 T_high = T0 + k·σ_high，其中 k 为时间-噪声弹性系数，其具体数值需结合特定市场的周转率及实证数据校准，通常量级在 0.8-1.2 天/标准差单位左右。

## Evidence

父节点级核验未通过：不完备（子节点2完全复述了父节点的核心公式，导致信息冗余（虽然正交性在逻辑上未冲突，但存在语义重复）；更严重的是完备性不足，父节点强调k需基于'搜索匹配理论'及'市场周转率校准'，子节点仅提及校准，未拆解k的理论推导或校准方法；且子节点4引入了搜索成本公式，但该公式在父节点中未明确定义，属于外部引入的新维度，虽相关但未在父节点中作为'计算T_high'的直接组成部分被明确界定，导致边界模糊。）

## Search Query

search matching model time to sale variance seller noise elasticity

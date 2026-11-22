# N49: 显著性检验的量化：定义效应量ΔT = T_deal_baseline - T_deal_high_price，当ΔT > 0.5 * T_deal_baseli

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

显著性检验的量化：定义效应量ΔT = T_deal_baseline - T_deal_high_price，当ΔT > 0.5 * T_deal_baseline且p < 0.05时，认为高挂价+高咨询假设能显著解释成交周期缩短，用于验证单一假设的解释力。

## Corrected Claim

显著性检验的量化：定义效应量ΔT = T_deal_baseline - T_deal_high_price，当ΔT > 0.5 * T_deal_baseline且p < 0.05时，认为高挂价+高咨询假设能显著解释成交周期缩短，用于验证单一假设的解释力。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1聚焦于效应量ΔT的置信区间构建及结合效应大小阈值的显著性判定，子节点2聚焦于p值计算的具体统计检验方法选择（t检验vs非参数检验）。两者分别处理'效应量估计/区间'和'假设检验方法'两个不同维度，无重复或矛盾，且共同覆盖了父节点中定义的ΔT计算、阈值判断及p<0.05检验要求。）

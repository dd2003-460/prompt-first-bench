# N123: 性价比指标 (Cost_Efficiency) 的分母计算：Total_TCO_3yr = CapEx + OpEx_energy + OpEx_mainten

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N27

## Claim

性价比指标 (Cost_Efficiency) 的分母计算：Total_TCO_3yr = CapEx + OpEx_energy + OpEx_maintenance。其中 OpEx_maintenance_A (消费级) ≈ $500/3y (驱动/稳定性风险)，OpEx_maintenance_B (数据中心) ≈ $100/3y (高 MTBF)，需纳入总成本。

## Corrected Claim

性价比指标 (Cost_Efficiency) 的分母计算：Total_TCO_3yr = CapEx + OpEx_energy + OpEx_maintenance。其中 OpEx_maintenance_A (消费级) ≈ $500/3y (驱动/稳定性风险)，OpEx_maintenance_B (数据中心) ≈ $100/3y (高 MTBF)，需纳入总成本。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点分别计算了工作点A的下限和工作点B的上限，两者针对不同硬件配置，逻辑上正交。但存在两个主要问题：1. 完备性不足：父节点定义包含CapEx+OpEx_energy+OpEx_maintenance，但子节点仅提供了极端的Min/Max边界估算，未提供基准值或中间状态，无法完整覆盖‘Total_TCO_3yr’这一指标的正常计算需求；2. 冗余性高：两个子节点本质上是同一公式（TCO = CapEx + OpEx_energy + OpEx_maintenance）在不同硬件参数下的实例化，属于‘一个参数的不同取值’，应合并为统一的计算逻辑或参数表，而非拆分为两个独立的定性/定量节点。）

## Search Query

consumer GPU vs datacenter GPU maintenance cost MTBF reliability

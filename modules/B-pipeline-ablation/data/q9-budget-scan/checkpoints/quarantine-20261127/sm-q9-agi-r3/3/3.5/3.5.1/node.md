# N60: 服务器空闲功耗 (Idle Power) 基线测量：在 4x V100-SXM2 处于 idle 状态 (无推理负载) 时，整机功耗约为 150-200W (C

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

服务器空闲功耗 (Idle Power) 基线测量：在 4x V100-SXM2 处于 idle 状态 (无推理负载) 时，整机功耗约为 150-200W (CPU+RAM+PSU损耗)。计算公式：Monthly_Cost_Idle = Idle_Power_W * 24 * 30 / 1000 * Price_per_kWh。若 Idle_Power=180W, Price=0.5 CNY/kWh，则月成本 ≈ 64.8 CNY。

## Corrected Claim

服务器空闲功耗 (Idle Power) 基线测量：在 4x V100-SXM2 处于 idle 状态 (无推理负载) 时，整机功耗约为 150-200W (CPU+RAM+PSU损耗)。计算公式：Monthly_Cost_Idle = Idle_Power_W * 24 * 30 / 1000 * Price_per_kWh。若 Idle_Power=180W, Price=0.5 CNY/kWh，则月成本 ≈ 64.8 CNY。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1聚焦于物理层面的功耗基线测量（区分了无CUDA上下文和有CUDA上下文两种状态），子节点2聚焦于基于上述基线的经济成本测算及运维策略对比（常驻vs冷启动）。两者维度不同（物理量 vs 经济/运维决策），逻辑互补且无重复或矛盾。虽然涉及相同的功率数值，但属于因果链条上的不同环节，不构成冗余。）

# N46: 卖家实际获得的补贴金额 Subsidy = 0.05 × P_actual，若选择流量券形式，则等值流量权重 W_subsidy = Subsidy / C_t

- **status**: pending
- **level**: L3
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

卖家实际获得的补贴金额 Subsidy = 0.05 × P_actual，若选择流量券形式，则等值流量权重 W_subsidy = Subsidy / C_traffic_unit，其中 C_traffic_unit 为单次有效曝光的边际成本。

## Corrected Claim

卖家实际获得的补贴金额 Subsidy = 0.05 × P_actual，若选择流量券形式，则等值流量权重 W_subsidy = Subsidy / C_traffic_unit，其中 C_traffic_unit 为单次有效曝光的边际成本。

## Evidence

父节点级核验未通过：不完备（子节点之间正交，分别描述了流量券的转化效率（静态价值）和时效性衰减（动态价值），无重叠。但不完备，父节点明确给出了补贴金额计算公式（Subsidy = 0.05 × P_actual）及流量权重转换公式（W_subsidy = Subsidy / C_traffic_unit），而子节点仅探讨了流量券的后续效能参数（η_conv 和 λ_decay），完全缺失了对父节点核心定义（即补贴计算逻辑和初始权重确定）的分解或解释。）

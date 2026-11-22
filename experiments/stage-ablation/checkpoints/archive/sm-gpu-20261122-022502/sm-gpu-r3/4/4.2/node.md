# N22: 电力与散热运营成本 (OpEx) 模型：TCO_power = (P_card + P_overhead) × T_hours × $kWh; 2×4090 峰

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

电力与散热运营成本 (OpEx) 模型：TCO_power = (P_card + P_overhead) × T_hours × $kWh; 2×4090 峰值功耗约 700W (2×350W)，1×A100 约 400W，假设 24/7 运行 3 年，电价 $0.15/kWh，2×4090 的 3 年电力成本约为 $1,113，而 1×A100 约为 $637，多卡方案在能耗上增加约 75% 的运营成本。

## Corrected Claim

电力与散热运营成本 (OpEx) 模型：TCO_power = (P_card + P_overhead) × T_hours × $kWh; 2×4090 峰值功耗约 700W (2×350W)，1×A100 约 400W，假设 24/7 运行 3 年，电价 $0.15/kWh，2×4090 的 3 年电力成本约为 $1,113，而 1×A100 约为 $637，多卡方案在能耗上增加约 75% 的运营成本。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应公式 TCO_power = (P_card + P_overhead) × T_hours × $kWh 中的四个独立变量（P_card, P_overhead, T_hours, $kWh）。各节点关注点不同（GPU功耗、主机功耗、时间、电价），互不重叠且无逻辑矛盾。虽然 P_card 和 P_overhead 共同构成总功耗 P_total，但在工程估算中将其拆分为计算核心功耗和系统基础功耗是标准且必要的做法，不属于冗余。）

## Search Query

RTX 4090 power consumption watts A100 power consumption watts

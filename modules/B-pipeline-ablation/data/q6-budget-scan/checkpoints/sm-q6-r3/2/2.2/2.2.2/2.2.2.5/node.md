# N162: POP分布不均对F_core实际值的影响：由于北上广深单点覆盖能力强，实际F_core分布不均，核心区域自建节点的实际流量占比F_core_actual = 0

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N61

## Claim

POP分布不均对F_core实际值的影响：由于北上广深单点覆盖能力强，实际F_core分布不均，核心区域自建节点的实际流量占比F_core_actual = 0.623 * (1 - Imbalance_Factor)，其中Imbalance_Factor=0.15（基于N100-N101数据计算），则F_core_actual = 0.623 * 0.85 = 0.529，表明实际自建流量占比低于理论值，需调整混合策略切分比例

## Corrected Claim

POP分布不均对F_core实际值的影响：由于北上广深单点覆盖能力强，实际F_core分布不均，核心区域自建节点的实际流量占比F_core_actual = 0.623 * (1 - Imbalance_Factor)，其中Imbalance_Factor=0.15（基于N100-N101数据计算），则F_core_actual = 0.623 * 0.85 = 0.529，表明实际自建流量占比低于理论值，需调整混合策略切分比例

## Evidence

先验知识/题面给定，逻辑校验通过：0.623 * (1 - 0.15) = 0.52955 ≈ 0.529，计算无误，逻辑自洽。

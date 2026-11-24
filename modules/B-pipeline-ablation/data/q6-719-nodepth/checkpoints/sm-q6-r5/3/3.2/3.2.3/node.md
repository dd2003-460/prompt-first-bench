# N72: 自建带宽成本 P_bw_self 的固定+变动结构：P_bw_self = (C_bandwidth_rent_fixed / Traffic_out_effe

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N17

## Claim

自建带宽成本 P_bw_self 的固定+变动结构：P_bw_self = (C_bandwidth_rent_fixed / Traffic_out_effective) + C_marginal_bw，其中 C_bandwidth_rent_fixed 为带宽租赁固定月租（10个POP点，每点10Gbps带宽，月租约¥5k-10k/点，总计¥50k-100k/月），C_marginal_bw 为超出部分的边际成本（通常极低或为零，因带宽已包干）；当 Traffic_out_effective 较大时，固定成本分摊导致单位成本降低，边际成本趋近于0。

## Corrected Claim

自建带宽成本 P_bw_self 的固定+变动结构：P_bw_self = (C_bandwidth_rent_fixed / Traffic_out_effective) + C_marginal_bw，其中 C_bandwidth_rent_fixed 为带宽租赁固定月租（10个POP点，每点10Gbps带宽，月租约¥5k-10k/点，总计¥50k-100k/月），C_marginal_bw 为超出部分的边际成本（通常极低或为零，因带宽已包干）；当 Traffic_out_effective 较大时，固定成本分摊导致单位成本降低，边际成本趋近于0。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应公式中的固定成本项（Node 1）、单位成本计算实例（Node 2）、边际成本项（Node 3）以及影响成本的关键约束/利用率指标（Node 4）。各节点在逻辑上分别解释了 P_bw_self 公式的不同组成部分及其经济含义，彼此独立且无重复。Node 4 虽涉及利用率，但它是解释为何 Node 2 中单位成本高昂的原因，属于结构性解释而非单纯数值重复，因此不构成冗余。）

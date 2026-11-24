# N18: 全自建策略的资源利用率模型：利用率 U_self = (实际服务带宽 B_served) / (自建节点总容量 C_total_self)，其中 C_total

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4

## Claim

全自建策略的资源利用率模型：利用率 U_self = (实际服务带宽 B_served) / (自建节点总容量 C_total_self)，其中 C_total_self 由 10 个 POP 点的单点容量 C_pop 决定，C_pop 需覆盖单点峰值流量 B_peak_pop = (B_avg × R_pg) / 10 × geo_share_i，geo_share_i 为第 i 个 POP 的地理流量占比，典型自建利用率目标为 40%–60% 以平衡成本与冗余。

## Corrected Claim

全自建策略的资源利用率模型：利用率 U_self = (实际服务带宽 B_served) / (自建节点总容量 C_total_self)，其中 C_total_self 由 10 个 POP 点的单点容量 C_pop 决定，C_pop 需覆盖单点峰值流量 B_peak_pop = (B_avg × R_pg) / 10 × geo_share_i，geo_share_i 为第 i 个 POP 的地理流量占比，典型自建利用率目标为 40%–60% 以平衡成本与冗余。

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别对应父节点公式中的分子（B_served/B_peak）、分母中的单点容量确定逻辑（C_pop）以及分母的总和与成本约束（C_total_self/Cost），逻辑链条清晰，无重叠或矛盾。）

## Search Query

self-hosted CDN POP point capacity planning utilization target 40-60%

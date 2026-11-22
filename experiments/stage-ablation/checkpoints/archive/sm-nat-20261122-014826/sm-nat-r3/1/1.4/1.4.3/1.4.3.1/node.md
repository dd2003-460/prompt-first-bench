# N95: 理论最优子集 C 的字节吞吐量贡献值 Total_opt = Σ_{i∈C_opt} (r_i * s_i)，其中 C_opt 为 128GB 容量下通过 0-

- **status**: verified
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N35, N36, N37

## Claim

理论最优子集 C 的字节吞吐量贡献值 Total_opt = Σ_{i∈C_opt} (r_i * s_i)，其中 C_opt 为 128GB 容量下通过 0-1 背包问题求解出的最大化流量子集，该值作为命中率分母的基准参照。

## Corrected Claim

理论最优子集 C 的字节吞吐量贡献值 Total_opt = Σ_{i∈C_opt} (r_i * s_i)，其中 C_opt 为 128GB 容量下通过 0-1 背包问题求解出的最大化流量子集，该值作为命中率分母的基准参照。

## Evidence

逻辑推导成立，来源未直接覆盖

## Search Query

0-1 knapsack problem CDN cache optimization Pareto distribution beta 0.9

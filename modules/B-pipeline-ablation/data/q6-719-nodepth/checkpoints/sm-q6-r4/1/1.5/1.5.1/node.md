# N53: T_transfer = Object_Size / Effective_Bandwidth_to_Origin，其中 Effective_Bandwidth_

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N10

## Claim

T_transfer = Object_Size / Effective_Bandwidth_to_Origin，其中 Effective_Bandwidth_to_Origin 受源站出口带宽限制（典型单源站出口 1-10 Gbps）及 TCP 窗口大小限制（MSS × cwnd）[待核验]

## Corrected Claim

T_transfer = Object_Size / Effective_Bandwidth_to_Origin，其中 Effective_Bandwidth_to_Origin 受源站出口带宽限制（典型单源站出口 1-10 Gbps）及 TCP 窗口大小限制（MSS × cwnd）[待核验]

## Evidence

父节点级核验未通过：不完备（子节点1关注分子（对象大小分布），子节点2关注分母（源站带宽及TCP限制），两者维度不同，正交性良好。但完备性不足：父节点公式 T = Size / Bandwidth 中，'Effective_Bandwidth' 不仅受源站出口限制，还受中间网络链路、CDN节点上行带宽以及并发竞争（多路复用/排队）的影响，子节点2仅讨论了源站侧瓶颈，未涵盖网络路径或并发调度对有效带宽的动态影响。）

## Search Query

TCP window size limit large file transfer bandwidth efficiency

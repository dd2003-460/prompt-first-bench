# N19: 自建节点可行性下限：单POP承载能力上限 C_max_pop = min(带宽瓶颈 B_pop / 单请求平均大小 s, 计算/存储瓶颈 CPU_pop / 单

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

自建节点可行性下限：单POP承载能力上限 C_max_pop = min(带宽瓶颈 B_pop / 单请求平均大小 s, 计算/存储瓶颈 CPU_pop / 单请求CPU成本)，需满足 总日均下载量 2TB / 10 POPs ≤ C_max_pop × 0.8 (安全余量)，否则需增加POP数量或放弃自建方案。

## Corrected Claim

自建节点可行性下限：单POP承载能力上限 C_max_pop = min(带宽瓶颈 B_pop / 单请求平均大小 s, 计算/存储瓶颈 CPU_pop / 单请求CPU成本)，需满足 总日均下载量 2TB / 10 POPs ≤ C_max_pop × 0.8 (安全余量)，否则需增加POP数量或放弃自建方案。

## Evidence

先验知识/题面给定，逻辑校验通过：公式量纲一致（流量/大小=请求数，流量/时间=QPS），安全余量系数0.8符合工程惯例，逻辑自洽。

## Search Query

CDN edge node maximum bandwidth capacity per POP 10Gbps 25Gbps storage limit

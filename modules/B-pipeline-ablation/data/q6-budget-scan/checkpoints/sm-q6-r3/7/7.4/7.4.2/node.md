# N339: 峰值带宽$B_{peak}$的精确计算公式为：$B_{peak} = (V_{daily} / 86400) \times K_{peak}$，其中$V_{da

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N126

## Claim

峰值带宽$B_{peak}$的精确计算公式为：$B_{peak} = (V_{daily} / 86400) \times K_{peak}$，其中$V_{daily}=2\text{TB}$，$K_{peak}=2.0$，代入得$B_{peak} \approx 37\text{Mbps}$。

## Corrected Claim

峰值带宽$B_{peak}$的精确计算公式为：$B_{peak} = (V_{daily} / 86400) \times K_{peak}$，其中$V_{daily}=2\text{TB}$，$K_{peak}=2.0$，代入得$B_{peak} \approx 37\text{Mbps}$。

## Evidence

先验知识/题面给定，逻辑校验通过：2TB = 2 * 1024^4 bytes，除以86400秒再乘以2.0，结果约为37.05 Mbps，与陈述一致。

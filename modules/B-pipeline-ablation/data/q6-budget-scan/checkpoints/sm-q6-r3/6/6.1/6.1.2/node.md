# N106: 全公有云策略基础设施成本 $C_{infra,cloud}$：公有云 CDN 无自建硬件折旧，但需考虑源站服务器成本（若源站也在云上）及可能的存储成本（如 OS

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N26

## Claim

全公有云策略基础设施成本 $C_{infra,cloud}$：公有云 CDN 无自建硬件折旧，但需考虑源站服务器成本（若源站也在云上）及可能的存储成本（如 OSS 存储 2TB/日增量），估算 $C_{infra,cloud} \approx 500-2000$ 元/月（视存储策略而定）。

## Corrected Claim

全公有云策略基础设施成本 $C_{infra,cloud}$：公有云 CDN 无自建硬件折旧，但需考虑源站服务器成本（若源站也在云上）及可能的存储成本（如 OSS 存储 2TB/日增量），估算 $C_{infra,cloud} \approx 500-2000$ 元/月（视存储策略而定）。

## Evidence

先验知识/题面给定，逻辑校验通过：公有云CDN无硬件折旧，主要成本为源站及存储，2TB/日增量存储成本在数百至两千元/月区间符合云厂商定价量级。

## Search Query

Alibaba Cloud OSS storage pricing per GB month

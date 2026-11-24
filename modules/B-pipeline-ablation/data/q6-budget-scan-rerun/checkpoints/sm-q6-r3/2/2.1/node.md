# N11: 基础设施成本（CAPEX/OPEX）公式：Cost_infra = (节点数 × 单节点硬件折旧/年 + 机房租金/年) / 年请求总量 × 1000；公有云 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N2

## Claim

基础设施成本（CAPEX/OPEX）公式：Cost_infra = (节点数 × 单节点硬件折旧/年 + 机房租金/年) / 年请求总量 × 1000；公有云 CDN 此项为 0（纯 OPEX 按量付费），自建 10 POP 点需计算硬件（服务器/交换机）及机房成本

## Corrected Claim

基础设施成本（CAPEX/OPEX）公式：Cost_infra = (节点数 × 单节点硬件折旧/年 + 机房租金/年) / 年请求总量 × 1000；公有云 CDN 此项为 0（纯 OPEX 按量付费），自建 10 POP 点需计算硬件（服务器/交换机）及机房成本

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN infrastructure cost calculation formula CAPEX OPEX node hardware depreciation colocation cost

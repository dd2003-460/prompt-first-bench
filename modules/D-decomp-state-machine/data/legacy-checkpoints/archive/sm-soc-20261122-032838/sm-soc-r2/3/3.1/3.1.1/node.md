# N63: 方案A（强制显示近期成交价）的工程实施成本 $C_A$ 由前端UI组件开发与后端数据聚合服务组成，$C_A = C_{UI} + C_{DB}$。在成熟二手平台

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N14

## Claim

方案A（强制显示近期成交价）的工程实施成本 $C_A$ 由前端UI组件开发与后端数据聚合服务组成，$C_A = C_{UI} + C_{DB}$。在成熟二手平台架构中，$C_{UI} \approx 5-10$ 人日，$C_{DB}$ 取决于实时性要求：若允许T+1延迟，$C_{DB} \approx 2-5$ 人日；若需实时（T+0），需引入流式计算，$C_{DB}$ 增至 10-20 人日。总成本 $C_A \in [7, 30]$ 人日。

## Corrected Claim

方案A（强制显示近期成交价）的工程实施成本 $C_A$ 由前端UI组件开发与后端数据聚合服务组成，$C_A = C_{UI} + C_{DB}$。在成熟二手平台架构中，$C_{UI} \approx 5-10$ 人日，$C_{DB}$ 取决于实时性要求：若允许T+1延迟，$C_{DB} \approx 2-5$ 人日；若需实时（T+0），需引入流式计算，$C_{DB}$ 增至 10-20 人日。总成本 $C_A \in [7, 30]$ 人日。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

cost of implementing price history display UI backend development person-days

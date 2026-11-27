# N63: 方案A（强制显示近期成交价）的工程实施成本 $C_A$ 由前端UI组件开发与后端数据聚合服务组成，$C_A = C_{UI} + C_{DB}$。在成熟二手平台

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N14

## Claim

方案A（强制显示近期成交价）的工程实施成本 $C_A$ 由前端UI组件开发与后端数据聚合服务组成，$C_A = C_{UI} + C_{DB}$。在成熟二手平台架构中，$C_{UI} \approx 5-10$ 人日，$C_{DB}$ 取决于实时性要求：若允许T+1延迟，$C_{DB} \approx 2-5$ 人日；若需实时（T+0），需引入流式计算，$C_{DB}$ 增至 10-20 人日。总成本 $C_A \in [7, 30]$ 人日。

## Corrected Claim

方案A（强制显示近期成交价）的工程实施成本 $C_A$ 由前端UI组件开发与后端数据聚合服务组成，$C_A = C_{UI} + C_{DB}$。在成熟二手平台架构中，$C_{UI} \approx 5-10$ 人日，$C_{DB}$ 取决于实时性要求：若允许T+1延迟，$C_{DB} \approx 2-5$ 人日；若需实时（T+0），需引入流式计算，$C_{DB}$ 增至 10-20 人日。总成本 $C_A \in [7, 30]$ 人日。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应公式中的 C_UI 和 C_DB 的两个不同技术路径（T+1 与 T+0），逻辑上互斥且无重复。虽然 C_DB 被拆分为两个子节点，但这代表了两种不同的架构选型场景，属于对父节点中条件分支的完整展开，而非简单的参数冗余。父节点的所有关键成本构成（UI、DB-T+1、DB-T+0）均被覆盖。）

## Search Query

cost of implementing price history display UI backend development person-days

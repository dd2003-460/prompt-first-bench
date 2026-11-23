# N315: 工作点 C（高成本低性/最小冗余）：采用 1 人/节点 7x24 轮班制 + 外包夜班支持（外包成本 50% 折扣），等效 $FTE_C = 10 \times

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N117

## Claim

工作点 C（高成本低性/最小冗余）：采用 1 人/节点 7x24 轮班制 + 外包夜班支持（外包成本 50% 折扣），等效 $FTE_C = 10 \times 1 \times 0.7 + 1 = 8$ 人，$C_{ops}^C = 8 \times 40,000 = 320,000$ 元/月，支持 MTTR ≤ 30min 的基础 SLA。

## Corrected Claim

工作点 C（高成本低性/最小冗余）：采用 1 人/节点 7x24 轮班制 + 外包夜班支持（外包成本 50% 折扣），等效 $FTE_C = 10 \times 1 \times 0.7 + 1 = 8$ 人，$C_{ops}^C = 8 \times 40,000 = 320,000$ 元/月，支持 MTTR ≤ 30min 的基础 SLA。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 10*1*0.7+1=8 及 8*40000=320000 正确，量级符合常规运维成本估算逻辑。

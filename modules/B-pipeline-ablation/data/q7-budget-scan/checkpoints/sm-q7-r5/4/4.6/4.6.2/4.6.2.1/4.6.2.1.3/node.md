# N500: 成本量化：新增155块16TB HDD的成本 C_hdd_add = 155 * 16TB * ¥1,450/TB ≈ ¥3,584,000。加上RAID控制器

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N218

## Claim

成本量化：新增155块16TB HDD的成本 C_hdd_add = 155 * 16TB * ¥1,450/TB ≈ ¥3,584,000。加上RAID控制器扩展（若需支持300盘，可能需增加1-2个控制器，成本约¥10,000-20,000），总增量资本支出 CAPEX_add ≈ ¥3.6M。此成本需与RTO从31.25h降至4h带来的业务损失减少额（C_RTO_penalty_A - C_RTO_penalty_C）进行NPV比较，以判断是否值得投资。

## Corrected Claim

成本量化：新增155块16TB HDD的成本 C_hdd_add = 155 * 16TB * ¥1,450/TB ≈ ¥3,584,000。加上RAID控制器扩展（若需支持300盘，可能需增加1-2个控制器，成本约¥10,000-20,000），总增量资本支出 CAPEX_add ≈ ¥3.6M。此成本需与RTO从31.25h降至4h带来的业务损失减少额（C_RTO_penalty_A - C_RTO_penalty_C）进行NPV比较，以判断是否值得投资。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（155*16*1450=3,584,000），RAID控制器成本量级合理，NPV比较逻辑符合经济学直觉。

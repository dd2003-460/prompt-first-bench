# N292: 业务单位时间价值 V_biz 的量化区间：若年营收基数为 ¥1 亿，敏感度系数 0.3，则 V_biz = ¥1 亿 × 0.3 / 8760 ≈ ¥3,425

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N100

## Claim

业务单位时间价值 V_biz 的量化区间：若年营收基数为 ¥1 亿，敏感度系数 0.3，则 V_biz = ¥1 亿 × 0.3 / 8760 ≈ ¥3,425/小时；若年营收基数为 ¥10 亿，则 V_biz ≈ ¥34,250/小时；此值直接决定 RTO 代价在 TCO 中的占比，需作为敏感性分析的关键变量。

## Corrected Claim

业务单位时间价值 V_biz 的量化区间：若年营收基数为 ¥1 亿，敏感度系数 0.3，则 V_biz = ¥1 亿 × 0.3 / 8760 ≈ ¥3,425/小时；若年营收基数为 ¥10 亿，则 V_biz ≈ ¥34,250/小时；此值直接决定 RTO 代价在 TCO 中的占比，需作为敏感性分析的关键变量。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 100,000,000 * 0.3 / 8760 ≈ 3424.66，四舍五入为 3425，量级与逻辑均正确。

## Search Query

cost of downtime per hour calculation formula

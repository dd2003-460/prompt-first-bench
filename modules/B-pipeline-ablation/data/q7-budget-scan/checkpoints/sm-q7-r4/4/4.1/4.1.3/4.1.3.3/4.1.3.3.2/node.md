# N794: 中营收高敏感工作点：V_biz = ¥1 亿 * 0.3 / 8760 ≈ ¥3,425/小时，适用于中小型 SaaS 核心数据库，停机直接导致 API 5xx

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N292

## Claim

中营收高敏感工作点：V_biz = ¥1 亿 * 0.3 / 8760 ≈ ¥3,425/小时，适用于中小型 SaaS 核心数据库，停机直接导致 API 5xx 错误并触发 SLA 违约。

## Corrected Claim

中营收高敏感工作点：V_biz = ¥1 亿 * 0.3 / 8760 ≈ ¥3,425/小时，适用于中小型 SaaS 核心数据库，停机直接导致 API 5xx 错误并触发 SLA 违约。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程正确（100,000,000 * 0.3 / 8760 ≈ 3424.66），业务场景描述符合SaaS行业常识。

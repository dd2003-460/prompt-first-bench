# N245: 计算最终动态有效命中率 H_eff：H_eff = H_static * (1 - M_invalidation) = 0.97 * (1 - 0.000008

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N91

## Claim

计算最终动态有效命中率 H_eff：H_eff = H_static * (1 - M_invalidation) = 0.97 * (1 - 0.0000086) ≈ 0.9699916，相比静态命中率绝对下降约 0.0000084 个百分点。

## Corrected Claim

计算最终动态有效命中率 H_eff：H_eff = H_static * (1 - M_invalidation) = 0.97 * (1 - 0.0000086) ≈ 0.9699916，相比静态命中率绝对下降约 0.0000084 个百分点。

## Evidence

先验知识/题面给定，逻辑校验通过：0.97 * (1 - 0.0000086) = 0.97 * 0.9999914 = 0.969991658，四舍五入后约为 0.9699916；绝对下降值为 0.97 - 0.9699916 = 0.0000084，计算无误。

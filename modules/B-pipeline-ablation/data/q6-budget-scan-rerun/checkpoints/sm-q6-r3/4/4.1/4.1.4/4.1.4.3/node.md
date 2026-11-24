# N341: 公有云CDN整体P99延迟修正值计算：L_p99_cloud_corrected = 0.95 * L_hit + 0.05 * L_miss。代入数值：若 L

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N109

## Claim

公有云CDN整体P99延迟修正值计算：L_p99_cloud_corrected = 0.95 * L_hit + 0.05 * L_miss。代入数值：若 L_hit=15ms, L_miss=80ms，则 L_p99_cloud_corrected = 0.95*15 + 0.05*80 = 14.25 + 4 = 18.25ms。此值需与 N108 中的全局抖动项叠加。

## Corrected Claim

公有云CDN整体P99延迟修正值计算：L_p99_cloud_corrected = 0.95 * L_hit + 0.05 * L_miss。代入数值：若 L_hit=15ms, L_miss=80ms，则 L_p99_cloud_corrected = 0.95*15 + 0.05*80 = 14.25 + 4 = 18.25ms。此值需与 N108 中的全局抖动项叠加。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 0.95*15 + 0.05*80 = 14.25 + 4 = 18.25 正确，公式结构符合加权平均逻辑。

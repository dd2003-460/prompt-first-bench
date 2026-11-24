# N340: 冷启动延迟的年化成本 = Annualized_Events × Affected_Users_Per_Event × ΔLTV_Per_User，假设年均突发

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N118

## Claim

冷启动延迟的年化成本 = Annualized_Events × Affected_Users_Per_Event × ΔLTV_Per_User，假设年均突发事件 10 次，每次影响 100k 用户，ΔLTV_Per_User 基于 N137 估算为 ¥0.5-2.0/用户，则年化成本约为 ¥50k-200k，需与公有云CDN的弹性扩容溢价对比。

## Corrected Claim

冷启动延迟的年化成本 = Annualized_Events × Affected_Users_Per_Event × ΔLTV_Per_User，假设年均突发事件 10 次，每次影响 100k 用户，ΔLTV_Per_User 基于 N137 估算为 ¥0.5-2.0/用户，则年化成本约为 ¥50k-200k，需与公有云CDN的弹性扩容溢价对比。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（10 * 100,000 * 0.5 = 50,000; 10 * 100,000 * 2.0 = 200,000），量级合理，符合成本估算逻辑。

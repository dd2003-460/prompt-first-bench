# N534: TTL=24h 工作点下的新鲜度违约风险成本：C_freshness_risk = P_stale * R_stale * Loss_per_stale_req

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N174

## Claim

TTL=24h 工作点下的新鲜度违约风险成本：C_freshness_risk = P_stale * R_stale * Loss_per_stale_request，其中 P_stale 为静态内容在24h内被更新的概率（图片<0.1%，短视频<0.5%），R_stale 为受影响请求数，Loss_per_stale_request 为单次陈旧内容导致的用户流失或投诉成本（¥0.01-0.1/req）；量化表明对于80%静态内容，C_freshness_risk < ¥50/月，远低于带宽节约 ¥1,152/月。

## Corrected Claim

TTL=24h 工作点下的新鲜度违约风险成本：C_freshness_risk = P_stale * R_stale * Loss_per_stale_request，其中 P_stale 为静态内容在24h内被更新的概率（图片<0.1%，短视频<0.5%），R_stale 为受影响请求数，Loss_per_stale_request 为单次陈旧内容导致的用户流失或投诉成本（¥0.01-0.1/req）；量化表明对于80%静态内容，C_freshness_risk < ¥50/月，远低于带宽节约 ¥1,152/月。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合成本计算逻辑，数值量级（静态内容更新概率低、单次损失小）与结论（风险成本远低于带宽节约）在工程直觉上自洽。

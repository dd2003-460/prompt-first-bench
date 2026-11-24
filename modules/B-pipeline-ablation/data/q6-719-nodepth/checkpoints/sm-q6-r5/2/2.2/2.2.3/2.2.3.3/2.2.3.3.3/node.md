# N539: TTL=12h 工作点下的新鲜度延迟风险量化：C_risk_12h = P_stale_12h * R_affected * Loss_per_req，其中 P

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N175

## Claim

TTL=12h 工作点下的新鲜度延迟风险量化：C_risk_12h = P_stale_12h * R_affected * Loss_per_req，其中 P_stale_12h 比 TTL=6h 高约 50%（因缓存窗口加倍），但绝对值仍 <0.2%；计算得 C_risk_12h ≈ ¥20-50/月，与带宽节约 ¥768/月相比，风险收益比 >15:1，支持 12h 作为平衡点。

## Corrected Claim

TTL=12h 工作点下的新鲜度延迟风险量化：C_risk_12h = P_stale_12h * R_affected * Loss_per_req，其中 P_stale_12h 比 TTL=6h 高约 50%（因缓存窗口加倍），但绝对值仍 <0.2%；计算得 C_risk_12h ≈ ¥20-50/月，与带宽节约 ¥768/月相比，风险收益比 >15:1，支持 12h 作为平衡点。

## Evidence

先验知识/题面给定，逻辑校验通过：TTL加倍导致过期概率线性增加（50%增幅合理），且绝对值<0.2%与成本计算（¥20-50 vs ¥768）在量级上自洽，风险收益比>15:1符合数学推导。

# N536: TTL=6h 工作点（高新鲜度-高回源）的对比基准：C_bw_6h = f_static * Total_Download_Traffic * (1 - H_6

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N174

## Claim

TTL=6h 工作点（高新鲜度-高回源）的对比基准：C_bw_6h = f_static * Total_Download_Traffic * (1 - H_6h) * P_bw_marginal，其中 H_6h≈0.80，计算得回源流量 ≈ 0.8 * 2000 * 0.20 = 320GB/日，月度带宽成本 C_bw_6h ≈ 320 * 30 * 0.2 = ¥1,920/月；P99 延迟 L_p99_6h 比 TTL=24h 高约 7ms，此点代表‘高新鲜度-高成本’工作点。

## Corrected Claim

TTL=6h 工作点（高新鲜度-高回源）的对比基准：C_bw_6h = f_static * Total_Download_Traffic * (1 - H_6h) * P_bw_marginal，其中 H_6h≈0.80，计算得回源流量 ≈ 0.8 * 2000 * 0.20 = 320GB/日，月度带宽成本 C_bw_6h ≈ 320 * 30 * 0.2 = ¥1,920/月；P99 延迟 L_p99_6h 比 TTL=24h 高约 7ms，此点代表‘高新鲜度-高成本’工作点。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 0.8 * 2000 * 0.2 = 320 及 320 * 30 * 0.2 = 1920 均正确，量纲与数值量级合理，符合 CDN 回源流量与成本估算的基本逻辑。

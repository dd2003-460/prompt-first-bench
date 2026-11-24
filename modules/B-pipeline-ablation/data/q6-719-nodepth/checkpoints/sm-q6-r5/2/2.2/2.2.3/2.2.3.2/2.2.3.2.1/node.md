# N533: TTL=24h 工作点下的精确回源带宽节约量：ΔB_back = f_static * Total_Download_Traffic * (H_24h - H_

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N174

## Claim

TTL=24h 工作点下的精确回源带宽节约量：ΔB_back = f_static * Total_Download_Traffic * (H_24h - H_6h)，其中 f_static=0.8, Total_Download_Traffic=2TB/日, H_24h≈0.92, H_6h≈0.80，计算得 ΔB_back ≈ 0.8 * 2000GB * 0.12 = 192GB/日；此值直接决定月度带宽成本节约 C_save_bw = 192 * 30 * P_bw_marginal。

## Corrected Claim

TTL=24h 工作点下的精确回源带宽节约量：ΔB_back = f_static * Total_Download_Traffic * (H_24h - H_6h)，其中 f_static=0.8, Total_Download_Traffic=2TB/日, H_24h≈0.92, H_6h≈0.80，计算得 ΔB_back ≈ 0.8 * 2000GB * 0.12 = 192GB/日；此值直接决定月度带宽成本节约 C_save_bw = 192 * 30 * P_bw_marginal。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合缓存带宽节约的基本定义（静态流量占比 * 总流量 * 命中率提升），数值计算 0.8 * 2000 * 0.12 = 192 准确无误，量纲一致。

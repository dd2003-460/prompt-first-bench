# N642: 工作点B（低成本/低缓存）的月度回源带宽增量成本 ΔC_backhaul_B = (H_A - H_B) * Total_Daily_Traffic * 30 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N214

## Claim

工作点B（低成本/低缓存）的月度回源带宽增量成本 ΔC_backhaul_B = (H_A - H_B) * Total_Daily_Traffic * 30 * P_bw_per_GB，其中 H_A=0.80, H_B=0.75, Total_Daily_Traffic=2000GB, P_bw_per_GB≈¥0.2/GB，计算得 ΔC_backhaul_B ≈ (0.05 * 2000 * 30 * 0.2) = ¥600/月/POP（假设流量均匀分布或按全国总成本分摊）。

## Corrected Claim

工作点B（低成本/低缓存）的月度回源带宽增量成本 ΔC_backhaul_B = (H_A - H_B) * Total_Daily_Traffic * 30 * P_bw_per_GB，其中 H_A=0.80, H_B=0.75, Total_Daily_Traffic=2000GB, P_bw_per_GB≈¥0.2/GB，计算得 ΔC_backhaul_B ≈ (0.05 * 2000 * 30 * 0.2) = ¥600/月/POP（假设流量均匀分布或按全国总成本分摊）。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合成本计算逻辑，数值代入 (0.05 * 2000 * 30 * 0.2 = 600) 计算准确，量纲一致。

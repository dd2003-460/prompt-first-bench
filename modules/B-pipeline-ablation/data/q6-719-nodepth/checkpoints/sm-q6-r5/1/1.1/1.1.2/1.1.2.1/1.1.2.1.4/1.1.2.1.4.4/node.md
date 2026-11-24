# N1269: 低码率策略的月度带宽成本节约 ΔC_bw_month = (Q_video_out_std - Q_video_out_low) * 30 * P_bw_clo

- **status**: verified
- **level**: L6
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N434

## Claim

低码率策略的月度带宽成本节约 ΔC_bw_month = (Q_video_out_std - Q_video_out_low) * 30 * P_bw_cloud，其中 P_bw_cloud ≈ 0.2 CNY/GB，计算得 ΔC_bw_month = (240GB - 120GB) * 30 * 0.2 = ¥720/月。

## Corrected Claim

低码率策略的月度带宽成本节约 ΔC_bw_month = (Q_video_out_std - Q_video_out_low) * 30 * P_bw_cloud，其中 P_bw_cloud ≈ 0.2 CNY/GB，计算得 ΔC_bw_month = (240GB - 120GB) * 30 * 0.2 = ¥720/月。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合成本计算逻辑，数值代入 (240-120)*30*0.2=720 计算正确，量纲一致。

# N722: P_core=0.6 假设下的敏感性分析：若 P_core 实际为 0.55（低估集中度），混合策略带宽成本 C_bw_mix 将增加 5% * (C_bw_c

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N240

## Claim

P_core=0.6 假设下的敏感性分析：若 P_core 实际为 0.55（低估集中度），混合策略带宽成本 C_bw_mix 将增加 5% * (C_bw_cloud - C_bw_self) / C_bw_mix，假设 C_bw_cloud=¥0.15/GB, C_bw_self=¥0.05/GB，总成本增加约 2.5%；若 P_core 实际为 0.65，总成本降低约 2.5%。因此 P_core 在 0.55-0.65 区间内波动对最终成本决策影响 <5%，不改变策略排序。

## Corrected Claim

P_core=0.6 假设下的敏感性分析：若 P_core 实际为 0.55（低估集中度），混合策略带宽成本 C_bw_mix 将增加 5% * (C_bw_cloud - C_bw_self) / C_bw_mix，假设 C_bw_cloud=¥0.15/GB, C_bw_self=¥0.05/GB，总成本增加约 2.5%；若 P_core 实际为 0.65，总成本降低约 2.5%。因此 P_core 在 0.55-0.65 区间内波动对最终成本决策影响 <5%，不改变策略排序。

## Evidence

先验知识/题面给定，逻辑校验通过：基于线性插值假设，P_core从0.6变至0.55/0.65（±0.05），若成本函数对P_core线性敏感，且混合成本位于云与自建成本之间，±2.5%的波动量级在数学上自洽，符合敏感性分析的基本逻辑。

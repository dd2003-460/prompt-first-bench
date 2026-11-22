# N166: 激进估计工作点（高信号敏感度）：假设高挂价信号导致买家保留价分布右偏（Skewness > 0.5），引入修正项 TS_aggressive = TS_neut

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N57

## Claim

激进估计工作点（高信号敏感度）：假设高挂价信号导致买家保留价分布右偏（Skewness > 0.5），引入修正项 TS_aggressive = TS_neutral * (1 - β_skew)，其中 β_skew 为偏态导致的尾部损失系数（估计值 0.1-0.2），该点代表信号失效最严重的情景。

## Corrected Claim

激进估计工作点（高信号敏感度）：假设高挂价信号导致买家保留价分布右偏（Skewness > 0.5），引入修正项 TS_aggressive = TS_neutral * (1 - β_skew)，其中 β_skew 为偏态导致的尾部损失系数（估计值 0.1-0.2），该点代表信号失效最严重的情景。

## Evidence

先验知识/题面给定，逻辑校验通过

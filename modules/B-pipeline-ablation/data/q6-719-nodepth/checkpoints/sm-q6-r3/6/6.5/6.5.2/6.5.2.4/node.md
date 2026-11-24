# N527: 地理分布变化对带宽成本的影响系数：当P_core从0.8降至0.5时，C_bw_mix的增量 ΔC_bw = (P_tail_new - P_tail_old)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N173

## Claim

地理分布变化对带宽成本的影响系数：当P_core从0.8降至0.5时，C_bw_mix的增量 ΔC_bw = (P_tail_new - P_tail_old) * (C_bw_public - C_bw_self) = (0.5 - 0.2) * (C_bw_public - C_bw_self)，需计算C_bw_public - C_bw_self的具体值。

## Corrected Claim

地理分布变化对带宽成本的影响系数：当P_core从0.8降至0.5时，C_bw_mix的增量 ΔC_bw = (P_tail_new - P_tail_old) * (C_bw_public - C_bw_self) = (0.5 - 0.2) * (C_bw_public - C_bw_self)，需计算C_bw_public - C_bw_self的具体值。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导符合线性加权平均成本模型，变量定义与增量计算逻辑自洽。

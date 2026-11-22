# N527: RX 7800 XT 的 TDP 确认为 263W (官方规格)，在 LLM 推理负载下平均功耗 P_avg = 0.7 * 263W = 184.1W；该值基

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N183

## Claim

RX 7800 XT 的 TDP 确认为 263W (官方规格)，在 LLM 推理负载下平均功耗 P_avg = 0.7 * 263W = 184.1W；该值基于 N103 经验系数，需考虑 RX 7800 XT 在 BF16/INT4 混合精度下的实际功耗波动范围 (±10%)，即 P_avg 区间为 165.7W-202.5W，用于 TCO 敏感性分析。

## Corrected Claim

RX 7800 XT 的 TDP 确认为 263W (官方规格)，在 LLM 推理负载下平均功耗 P_avg = 0.7 * 263W = 184.1W；该值基于 N103 经验系数，需考虑 RX 7800 XT 在 BF16/INT4 混合精度下的实际功耗波动范围 (±10%)，即 P_avg 区间为 165.7W-202.5W，用于 TCO 敏感性分析。

## Evidence

先验知识/题面给定，逻辑校验通过：RX 7800 XT 官方 TDP 确为 263W，0.7 负载系数及 ±10% 波动范围的数学计算（184.1W, 165.7W-202.5W）准确无误，符合工程估算逻辑。

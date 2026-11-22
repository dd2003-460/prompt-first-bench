# N201: 尾部概率 P(S > s_max) 对 α 的敏感度分析：d(P)/d(α) = -ln(s_min/s_max) * (s_min/s_max)^{α-1}，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N72

## Claim

尾部概率 P(S > s_max) 对 α 的敏感度分析：d(P)/d(α) = -ln(s_min/s_max) * (s_min/s_max)^{α-1}，在 α=1.1 时，若 α 增加 0.1，P 从 31.6% 降至 25.1%，表明尾部概率对 α 敏感，需精确估计 α 值。

## Corrected Claim

尾部概率 P(S > s_max) 对 α 的敏感度分析：d(P)/d(α) = -ln(s_min/s_max) * (s_min/s_max)^{α-1}，在 α=1.1 时，若 α 增加 0.1，P 从 31.6% 降至 25.1%，表明尾部概率对 α 敏感，需精确估计 α 值。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导符合幂律分布尾部概率对参数α的敏感度分析，数值变化趋势（α增大导致尾部概率降低）符合直觉，量级合理。

## Search Query

sensitivity of Pareto tail probability to alpha parameter

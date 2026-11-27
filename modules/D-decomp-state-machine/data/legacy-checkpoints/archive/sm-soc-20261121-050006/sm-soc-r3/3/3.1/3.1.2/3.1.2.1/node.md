# N227: 共享随机源：P(ReadLabel) 的估计公式为 P(ReadLabel) = 1 - exp(-λ_exposure * T_exposure * (1 -

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N69

## Claim

共享随机源：P(ReadLabel) 的估计公式为 P(ReadLabel) = 1 - exp(-λ_exposure * T_exposure * (1 - Fatigue_rate))，其中 λ_exposure 为标签曝光率（估计 0.3-0.5），T_exposure 为买家平均浏览时长（秒），Fatigue_rate 为搜索疲劳率；该值在 N69 公式中作为乘数项，其分布方差 Var(P(ReadLabel)) 取决于 T_exposure 的分布稳定性。

## Corrected Claim

共享随机源：P(ReadLabel) 的估计公式为 P(ReadLabel) = 1 - exp(-λ_exposure * T_exposure * (1 - Fatigue_rate))，其中 λ_exposure 为标签曝光率（估计 0.3-0.5），T_exposure 为买家平均浏览时长（秒），Fatigue_rate 为搜索疲劳率；该值在 N69 公式中作为乘数项，其分布方差 Var(P(ReadLabel)) 取决于 T_exposure 的分布稳定性。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

user attention span probability model exponential decay reading rate

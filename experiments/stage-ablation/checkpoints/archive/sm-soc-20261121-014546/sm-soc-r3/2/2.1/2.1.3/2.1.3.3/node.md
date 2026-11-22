# N195: 下游投影 2：SNR_crit 的敏感性分析，若 SNR_crit 从 1.0 提升至 1.2（因买家更挑剔），则 P(no_inquiry) 在相同 SNR 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N55

## Claim

下游投影 2：SNR_crit 的敏感性分析，若 SNR_crit 从 1.0 提升至 1.2（因买家更挑剔），则 P(no_inquiry) 在相同 SNR 下增加，需调整 σ_noise 或 ΔP 以维持 60% 的观测频率。

## Corrected Claim

下游投影 2：SNR_crit 的敏感性分析，若 SNR_crit 从 1.0 提升至 1.2（因买家更挑剔），则 P(no_inquiry) 在相同 SNR 下增加，需调整 σ_noise 或 ΔP 以维持 60% 的观测频率。

## Evidence

先验知识/题面给定，逻辑校验通过：SNR_crit 提高意味着判定阈值变高，在相同信号噪声比下，误判为无查询的概率增加，需调整参数以维持观测频率，符合统计检测理论逻辑。

## Search Query

sensitivity analysis critical signal to noise ratio buyer selectivity

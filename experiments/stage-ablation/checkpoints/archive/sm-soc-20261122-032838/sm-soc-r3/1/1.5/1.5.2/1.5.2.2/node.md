# N152: ‘降价后无咨询’的替代机制：通知缺失与搜索惯性。即使 P_low < P_threshold，若买家未收到降价通知，且原搜索列表未刷新，则咨询概率 P_inqu

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N49

## Claim

‘降价后无咨询’的替代机制：通知缺失与搜索惯性。即使 P_low < P_threshold，若买家未收到降价通知，且原搜索列表未刷新，则咨询概率 P_inquiry ≈ 0。量化：假设 60% 的买家在降价后 48h 内未重新搜索该商品（搜索惯性），且平台未推送降价通知（推送率 r_push=0），则 P_inquiry = P(re-search) * P(accept | re-search)。若 P(re-search)=0.4，则 P_inquiry ≤ 0.4。若 P(accept | re-search)=1（价格已低于阈值），则 60% 无咨询可由 40% 搜索率解释，无需 P_low > P_threshold。

## Corrected Claim

‘降价后无咨询’的替代机制：通知缺失与搜索惯性。即使 P_low < P_threshold，若买家未收到降价通知，且原搜索列表未刷新，则咨询概率 P_inquiry ≈ 0。量化：假设 60% 的买家在降价后 48h 内未重新搜索该商品（搜索惯性），且平台未推送降价通知（推送率 r_push=0），则 P_inquiry = P(re-search) * P(accept | re-search)。若 P(re-search)=0.4，则 P_inquiry ≤ 0.4。若 P(accept | re-search)=1（价格已低于阈值），则 60% 无咨询可由 40% 搜索率解释，无需 P_low > P_threshold。

## Evidence

先验知识/题面给定，逻辑校验通过：基于概率乘法原理，P_inquiry = P(re-search) * P(accept | re-search)，当 P(re-search)=0.4 且 P(accept)=1 时，P_inquiry=0.4，即 60% 无咨询，推导自洽。

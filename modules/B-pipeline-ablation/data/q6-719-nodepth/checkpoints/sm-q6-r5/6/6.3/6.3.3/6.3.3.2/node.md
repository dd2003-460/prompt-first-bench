# N333: Lambda 的动态修正：Lambda 并非恒定，而是随延迟增加而增加（用户容忍度非线性）；在 L_p99 > 100ms 时，Lambda 应从基础值 ¥0.

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N109

## Claim

Lambda 的动态修正：Lambda 并非恒定，而是随延迟增加而增加（用户容忍度非线性）；在 L_p99 > 100ms 时，Lambda 应从基础值 ¥0.001/ms/req 修正为 ¥0.005-0.010/ms/req（基于N126的阈值效应），导致 Cost_latency_extra 放大5-10倍。

## Corrected Claim

Lambda 的动态修正：Lambda 并非恒定，而是随延迟增加而增加（用户容忍度非线性）；在 L_p99 > 100ms 时，Lambda 应从基础值 ¥0.001/ms/req 修正为 ¥0.005-0.010/ms/req（基于N126的阈值效应），导致 Cost_latency_extra 放大5-10倍。

## Evidence

先验知识/题面给定，逻辑校验通过

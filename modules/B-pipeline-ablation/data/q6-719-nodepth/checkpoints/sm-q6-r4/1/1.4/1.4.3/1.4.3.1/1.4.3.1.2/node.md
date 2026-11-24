# N537: 工作点A的P99延迟约束验证：在Hit_Rate=90%下，剩余10%请求的回源延迟T_origin需满足0.1×T_origin + 0.9×T_cache 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N181

## Claim

工作点A的P99延迟约束验证：在Hit_Rate=90%下，剩余10%请求的回源延迟T_origin需满足0.1×T_origin + 0.9×T_cache ≤ T_target；若T_target=200ms且T_cache=50ms，则要求T_origin ≤ 1600ms，需确认源站RTT是否超标。

## Corrected Claim

工作点A的P99延迟约束验证：在Hit_Rate=90%下，剩余10%请求的回源延迟T_origin需满足0.1×T_origin + 0.9×T_cache ≤ T_target；若T_target=200ms且T_cache=50ms，则要求T_origin ≤ 1600ms，需确认源站RTT是否超标。

## Evidence

先验知识/题面给定，逻辑校验通过：加权平均延迟公式 0.1*T_origin + 0.9*50 <= 200 推导得 T_origin <= 1600ms，数学推导正确且量级合理。

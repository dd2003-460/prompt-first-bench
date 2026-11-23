# N204: 鉴权T_auth的P99延迟构成：T_auth_P99 = T_token_verify + T_rate_limit_check + T_permission

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N61

## Claim

鉴权T_auth的P99延迟构成：T_auth_P99 = T_token_verify + T_rate_limit_check + T_permission_check，其中T_token_verify为JWT/Token验证时间（典型0.5-2ms），T_rate_limit_check为限流检查时间（典型0.1-0.5ms），T_permission_check为权限检查时间（典型0.5-1ms），P99值通常取T_token_verify=2ms场景，故T_auth_P99≈3-5ms，若使用分布式缓存（如Redis）可降至1-2ms，需评估缓存命中率对P99的影响

## Corrected Claim

鉴权T_auth的P99延迟构成：T_auth_P99 = T_token_verify + T_rate_limit_check + T_permission_check，其中T_token_verify为JWT/Token验证时间（典型0.5-2ms），T_rate_limit_check为限流检查时间（典型0.1-0.5ms），T_permission_check为权限检查时间（典型0.5-1ms），P99值通常取T_token_verify=2ms场景，故T_auth_P99≈3-5ms，若使用分布式缓存（如Redis）可降至1-2ms，需评估缓存命中率对P99的影响

## Evidence

先验知识/题面给定，逻辑校验通过：各组件典型延迟量级（JWT验证、限流、权限检查）符合工程常识，P99取值逻辑自洽，分布式缓存优化方向合理。

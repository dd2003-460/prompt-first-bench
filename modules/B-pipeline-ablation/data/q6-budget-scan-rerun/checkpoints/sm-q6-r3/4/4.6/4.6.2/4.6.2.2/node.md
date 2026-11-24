# N279: 工作点B（标准DNS切换）：采用 DNS TTL 切换机制，T_switch = 300s，P99 延迟抖动 ΔP99_B = (300s / T_target

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N89

## Claim

工作点B（标准DNS切换）：采用 DNS TTL 切换机制，T_switch = 300s，P99 延迟抖动 ΔP99_B = (300s / T_target) × 100%，当 T_target=100ms 时 ΔP99_B = 300000%（严重超标，表明 DNS 切换不适合 P99 敏感场景，需结合缓存预热策略降低实际影响）

## Corrected Claim

工作点B（标准DNS切换）：采用 DNS TTL 切换机制，T_switch = 300s，P99 延迟抖动 ΔP99_B = (300s / T_target) × 100%，当 T_target=100ms 时 ΔP99_B = 300000%（严重超标，表明 DNS 切换不适合 P99 敏感场景，需结合缓存预热策略降低实际影响）

## Evidence

先验知识/题面给定，逻辑校验通过：公式 ΔP99_B = (T_switch / T_target) × 100% 代入 T_switch=300s, T_target=100ms(0.1s) 计算得 300/0.1 * 100% = 300000%，数值量级与逻辑自洽。

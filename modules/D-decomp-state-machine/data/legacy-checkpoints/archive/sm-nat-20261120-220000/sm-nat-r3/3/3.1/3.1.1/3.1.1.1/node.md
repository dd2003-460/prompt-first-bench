# N97: 重填充失败率f_refill的高成本低性工作点：在源站高负载场景下，P(超时)从0.1%升至1%，P(去重失败)从0.01%升至0.1%，则f_refill =

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N34

## Claim

重填充失败率f_refill的高成本低性工作点：在源站高负载场景下，P(超时)从0.1%升至1%，P(去重失败)从0.01%升至0.1%，则f_refill = 0.001 + 0.01 + 0.001 = 0.012（1.2%），导致综合折损从0.951%升至9.5%，显著影响长期持有成本。

## Corrected Claim

重填充失败率f_refill的高成本低性工作点：在源站高负载场景下，P(超时)从0.1%升至1%，P(去重失败)从0.01%升至0.1%，则f_refill = 0.001 + 0.01 + 0.001 = 0.012（1.2%），导致综合折损从0.951%升至1.2%，显著影响长期持有成本。

## Evidence

[质询]数值计算存在内部矛盾：0.001 + 0.01 + 0.001 的算术和应为 0.012，但陈述中声称综合折损从 0.951% 升至 9.5%，而 0.012 对应 1.2%，与 9.5% 不符，存在量级或逻辑错误。 | 无可用外部证据，且逻辑校验发现数值计算与结论不一致，无法排除错误。

## Search Query

CDN origin server timeout rate high load scenario refill failure rate

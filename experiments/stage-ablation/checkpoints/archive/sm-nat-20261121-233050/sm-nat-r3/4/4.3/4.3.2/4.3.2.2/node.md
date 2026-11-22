# N126: 工作点2（TTL/最终一致性，TTL=1小时）：P_expire_within_TTL = 1 - exp(-0.01 * (1/24)) ≈ 0.000417

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N48

## Claim

工作点2（TTL/最终一致性，TTL=1小时）：P_expire_within_TTL = 1 - exp(-0.01 * (1/24)) ≈ 0.000417。H_dynamic_hit ≈ P_expire * P_reuse_after_expire。若TTL过期后对象在下次请求前未被重新缓存，则失效。假设 P_reuse_after_expire ≈ 0.5（50%概率在TTL内再次访问）。H_dynamic_hit ≈ 0.000417 * 0.5 ≈ 0.0002 (0.02%)。此值低于ETag场景，因为TTL过期导致的失效更频繁但恢复更慢。

## Corrected Claim

工作点2（TTL/最终一致性，TTL=1小时）：P_expire_within_TTL = 1 - exp(-0.01 * (1/24)) ≈ 0.000417。H_dynamic_hit ≈ P_expire * P_reuse_after_expire。若TTL过期后对象在下次请求前未被重新缓存，则失效。假设 P_reuse_after_expire 为某特定值（例如0.5），则 H_dynamic_hit ≈ 0.000417 * 0.5 ≈ 0.0002 (0.02%)。此值低于ETag场景，因为TTL过期导致的失效更频繁但恢复更慢。

## Evidence

[质询]该陈述包含具体的经验性假设参数（如 P_reuse_after_expire ≈ 0.5），这属于特定场景下的经验事实，无法从第一性原理或数学公理中严格推导出来。虽然数学计算过程正确，但核心参数缺乏外部来源支持，且不同工作负载下该概率差异巨大，直接断言为0.5缺乏普适性依据。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且参数为经验假设，不适用第一性原理推导条款）

## Search Query

CDN TTL cache hit rate calculation with update rate

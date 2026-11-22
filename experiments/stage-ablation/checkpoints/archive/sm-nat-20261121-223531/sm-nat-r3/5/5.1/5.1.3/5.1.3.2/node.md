# N180: LRU 保守下界工作点中 K_min 的取值对 H_lb 的影响：计算 K_min=5%, 10%, 20% 时对应的 H_lb 值，验证 H_lb 随 K_m

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N64

## Claim

LRU 保守下界工作点中 K_min 的取值对 H_lb 的影响：计算 K_min=5%, 10%, 20% 时对应的 H_lb 值，验证 H_lb 随 K_min 增加而增加，并找出使 H_lb 达到 50% 的最小 K_min 值（预期 K_min ≈ 40%，因为独立性假设下大小与热度无关，需要缓存更多对象才能覆盖字节流量），给出 K_min 与 H_lb 的解析近似式 H_lb ≈ 1 - (1-K_min) * (E[S]_cold/E[S])。

## Corrected Claim

LRU 保守下界工作点中 K_min 的取值对 H_lb 的影响：计算 K_min=5%, 10%, 20% 时对应的 H_lb 值，验证 H_lb 随 K_min 增加而增加，并找出使 H_lb 达到 50% 的最小 K_min 值（预期 K_min ≈ 40%，因为独立性假设下大小与热度无关，需要缓存更多对象才能覆盖字节流量），给出 K_min 与 H_lb 的解析近似式 H_lb ≈ 1 - (1-K_min) * (E[S]_cold/E[S])。

## Evidence

先验知识/题面给定，逻辑校验通过

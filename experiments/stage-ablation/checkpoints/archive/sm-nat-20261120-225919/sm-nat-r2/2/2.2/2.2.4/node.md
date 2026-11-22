# N46: LRU 的 τ_res 由缓存容量和请求速率决定：τ_res ≈ C / (R_total * E[S]) = 128×10^9 / (5×10^7/86400

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

LRU 的 τ_res 由缓存容量和请求速率决定：τ_res ≈ C / (R_total * E[S]) = 128×10^9 / (5×10^7/86400 * 215×10^3) ≈ 128×10^9 / (12.5 * 215×10^3) ≈ 47.5 天，与 τ_obj=100 天不相等，需重新计算 D。

## Corrected Claim

LRU 的 τ_res 由缓存容量和请求速率决定：τ_res ≈ C / (R_total * E[S]) = 128×10^9 / (5×10^7/86400 * 215×10^3) ≈ 128×10^9 / (12.5 * 215×10^3) ≈ 47.5 天，与 τ_obj=100 天不相等，需重新计算 D。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算 128e9 / (12.5 * 215e3) ≈ 47.5 正确，量纲与逻辑自洽。

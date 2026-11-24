# N519: 长 TTL 工作点下的缓存失效同步成本 C_invalidate_ttl 极低，近似为 0，因为无需频繁调用 CDN 刷新 API，主要成本仅在于初始加载后的被

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N167

## Claim

长 TTL 工作点下的缓存失效同步成本 C_invalidate_ttl 极低，近似为 0，因为无需频繁调用 CDN 刷新 API，主要成本仅在于初始加载后的被动过期，与短 TTL 策略中每 GB 更新需 ¥0.001-0.01 的 API 调用费形成对比。

## Corrected Claim

长 TTL 工作点下的缓存失效同步成本 C_invalidate_ttl 极低，近似为 0，因为无需频繁调用 CDN 刷新 API，主要成本仅在于初始加载后的被动过期，与短 TTL 策略中每 GB 更新需 ¥0.001-0.01 的 API 调用费形成对比。

## Evidence

先验知识/题面给定，逻辑校验通过：长TTL策略下缓存失效主要依赖被动过期，无需频繁主动调用CDN刷新API，因此同步成本极低，与短TTL的高频API调用成本形成合理对比。

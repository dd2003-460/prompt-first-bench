# N535: TTL=24h 工作点下的 P99 延迟改善量化：ΔL_p99 = L_backhaul * (1 - H_6h) - L_backhaul * (1 - H_

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N174

## Claim

TTL=24h 工作点下的 P99 延迟改善量化：ΔL_p99 = L_backhaul * (1 - H_6h) - L_backhaul * (1 - H_24h) + L_jitter_reduction，其中 L_backhaul≈50ms, (1-H_6h)=0.20, (1-H_24h)=0.08, L_jitter_reduction≈1ms（因回源请求减少导致的队列抖动降低）；计算得 ΔL_p99 ≈ 50*(0.20-0.08) + 1 = 7ms，证实 TTL 延长对 P99 有显著正向贡献。

## Corrected Claim

TTL=24h 工作点下的 P99 延迟改善量化：ΔL_p99 = L_backhaul * (1 - H_6h) - L_backhaul * (1 - H_24h) + L_jitter_reduction，其中 L_backhaul≈50ms, (1-H_6h)=0.20, (1-H_24h)=0.08, L_jitter_reduction≈1ms（因回源请求减少导致的队列抖动降低）；计算得 ΔL_p99 ≈ 50*(0.20-0.08) + 1 = 7ms，证实 TTL 延长对 P99 有显著正向贡献。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导符合缓存延迟模型直觉，数值计算 50*(0.12)+1=7ms 准确，量级合理。

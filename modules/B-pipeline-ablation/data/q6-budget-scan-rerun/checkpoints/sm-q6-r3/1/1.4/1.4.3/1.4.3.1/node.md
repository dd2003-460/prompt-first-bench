# N159: 工作点A（高命中/低成本）：假设长尾区域公有云CDN缓存命中率 CHR_tail=90%，回源延迟 T_origin_fallback=150ms，则P99_t

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N48

## Claim

工作点A（高命中/低成本）：假设长尾区域公有云CDN缓存命中率 CHR_tail=90%，回源延迟 T_origin_fallback=150ms，则P99_tail ≈ 120ms (RTT) + 10ms (处理) + 0.1*150ms (回源) = 145ms，此工作点代表最优延迟表现，但需验证90%命中率在三四线长尾场景下的可达性（通常受限于节点密度，可能需下调至85%）。

## Corrected Claim

工作点A（高命中/低成本）：假设长尾区域公有云CDN缓存命中率 CHR_tail=90%，回源延迟 T_origin_fallback=150ms，则P99_tail ≈ 120ms (RTT) + 10ms (处理) + 0.1*150ms (回源) = 145ms，此工作点代表最优延迟表现，但需验证90%命中率在三四线长尾场景下的可达性（通常受限于节点密度，可能需下调至85%）。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（120+10+15=145ms），工程参数量级（CDN命中率、延迟）符合常识，无内部矛盾。

## Search Query

Cloudflare China tail region cache hit ratio P99 latency

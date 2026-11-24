# N586: 自建 POP 若未部署多线 BGP，长尾区域跨网用户的 P99 延迟将额外增加 ΔT_cross_self ≈ 15-25ms，使得总 P99 可能达到 40-

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N191

## Claim

自建 POP 若未部署多线 BGP，长尾区域跨网用户的 P99 延迟将额外增加 ΔT_cross_self ≈ 15-25ms，使得总 P99 可能达到 40-60ms，此时与公有云 CDN 在长尾区域的 P99 差异缩小至 5-10ms 以内，甚至可能反超。

## Corrected Claim

自建 POP 若未部署多线 BGP，长尾区域跨网用户的 P99 延迟将额外增加 ΔT_cross_self ≈ 15-25ms，使得总 P99 可能达到 40-60ms，此时与公有云 CDN 在长尾区域的 P99 差异缩小至 5-10ms 以内，甚至可能反超。

## Evidence

先验知识/题面给定，逻辑校验通过

# N160: 工作点B（基准/中成本）：假设长尾区域公有云CDN缓存命中率 CHR_tail=80%，回源延迟 T_origin_fallback=150ms，则P99_ta

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N48

## Claim

工作点B（基准/中成本）：假设长尾区域公有云CDN缓存命中率 CHR_tail=80%，回源延迟 T_origin_fallback=150ms，则P99_tail ≈ 120ms + 10ms + 0.2*150ms = 160ms，此工作点为N48给定的基准值，用于计算混合策略中 w_tail 部分的延迟贡献，需确认150ms回源延迟是否包含源站处理时间（通常源站处理50-100ms，网络传输50-100ms）。

## Corrected Claim

工作点B（基准/中成本）：假设长尾区域公有云CDN缓存命中率 CHR_tail=80%，回源延迟 T_origin_fallback=150ms，则P99_tail ≈ 120ms + 10ms + 0.2*150ms = 160ms，此工作点为N48给定的基准值，用于计算混合策略中 w_tail 部分的延迟贡献，需确认150ms回源延迟是否包含源站处理时间（通常源站处理50-100ms，网络传输50-100ms）。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 120+10+0.2*150=160 正确，且 150ms 回源延迟符合典型源站处理+网络传输的量级范围。

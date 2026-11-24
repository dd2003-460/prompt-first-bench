# N48: 长尾区域公有云CDN的P99延迟具体构成：P99_tail = RTT_tail + T_processing_pub + T_origin_fallback。

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

长尾区域公有云CDN的P99延迟具体构成：P99_tail = RTT_tail + T_processing_pub + T_origin_fallback。假设长尾区域（三四线）平均RTT为40ms，P99 RTT为120ms；T_processing_pub为10ms；若缓存未命中，需回源，回源延迟T_origin_fallback约为100-200ms（取决于源站位置）。假设长尾区域缓存命中率CHR_tail为80%，则P99_tail ≈ 120 + 10 + (0.2 * 150) = 160ms。若CHR_tail降至70%，P99_tail ≈ 120 + 10 + (0.3 * 150) = 175ms。

## Corrected Claim

长尾区域公有云CDN的P99延迟具体构成：P99_tail = RTT_tail + T_processing_pub + T_origin_fallback。假设长尾区域（三四线）平均RTT为40ms，P99 RTT为120ms；T_processing_pub为10ms；若缓存未命中，需回源，回源延迟T_origin_fallback约为100-200ms（取决于源站位置）。假设长尾区域缓存命中率CHR_tail为80%，则P99_tail ≈ 120 + 10 + (0.2 * 150) = 160ms。若CHR_tail降至70%，P99_tail ≈ 120 + 10 + (0.3 * 150) = 175ms。

## Evidence

父节点级核验未通过：有冗余（子节点本质上是对父节点中变量（CHR_tail 和 T_origin_fallback）不同取值的枚举，属于同一公式的参数敏感性分析，而非独立的结构或机制分解。）

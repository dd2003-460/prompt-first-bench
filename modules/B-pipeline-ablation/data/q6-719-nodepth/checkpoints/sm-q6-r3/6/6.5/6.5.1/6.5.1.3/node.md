# N522: 长尾区域P99延迟 P99_tail = RTT_tail + T_proc + H_miss_tail * (RTT_origin + T_transfer)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N172

## Claim

长尾区域P99延迟 P99_tail = RTT_tail + T_proc + H_miss_tail * (RTT_origin + T_transfer)，其中RTT_tail为长尾区域到POP的RTT，H_miss_tail为长尾区域缓存未命中率，需代入具体数值计算。

## Corrected Claim

长尾区域P99延迟 P99_tail = RTT_tail + T_proc + H_miss_tail * (RTT_origin + T_transfer)，其中RTT_tail为长尾区域到POP的RTT，H_miss_tail为长尾区域缓存未命中率，需代入具体数值计算。

## Evidence

先验知识/题面给定，逻辑校验通过

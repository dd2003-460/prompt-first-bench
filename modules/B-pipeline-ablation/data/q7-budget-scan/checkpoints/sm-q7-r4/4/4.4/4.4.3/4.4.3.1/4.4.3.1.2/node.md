# N812: 云存储 PUT 请求的一致性窗口 T_consistency_window 不仅包含 T_ack，还包含客户端超时重试机制：若客户端设置 Timeout=2s，

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N302

## Claim

云存储 PUT 请求的一致性窗口 T_consistency_window 不仅包含 T_ack，还包含客户端超时重试机制：若客户端设置 Timeout=2s，而 T_ack≈65ms，则 P_timeout = 0；但若网络抖动导致 RTT 瞬时升至 500ms，T_ack 可能突破 500ms，触发客户端重试，重试导致的额外成本 = Retry_Count * (T_retry_wait + T_ack_new)，假设年重试率 0.1%，每次重试增加 1 个请求成本 ¥0.01/万次，年化额外成本可忽略（<¥100），但需关注长尾延迟对 SLA 的影响。

## Corrected Claim

云存储 PUT 请求的一致性窗口 T_consistency_window 不仅包含 T_ack，还包含客户端超时重试机制：若客户端设置 Timeout=2s，而 T_ack≈65ms，则 P_timeout = 0；但若网络抖动导致 RTT 瞬时升至 500ms，T_ack 可能突破 500ms，触发客户端重试，重试导致的额外成本 = Retry_Count * (T_retry_wait + T_ack_new)，假设年重试率 0.1%，每次重试增加 1 个请求成本 ¥0.01/万次，年化额外成本可忽略（<¥100），但需关注长尾延迟对 SLA 的影响。

## Evidence

先验知识/题面给定，逻辑校验通过：Timeout(2s) > RTT(500ms) 故 P_timeout=0 逻辑成立；成本估算量级合理（0.1%重试率下年化成本极低符合直觉）；SLA长尾影响符合工程常识。

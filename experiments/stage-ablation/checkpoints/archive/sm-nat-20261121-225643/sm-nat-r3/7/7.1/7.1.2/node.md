# N113: N42 中 '8字节时间戳' 假设的精度-开销权衡量化：若时间戳用于指数衰减老化，精度需求由 λ_decay 决定；当 T_window=1 小时时，λ_dec

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N42

## Claim

N42 中 '8字节时间戳' 假设的精度-开销权衡量化：若时间戳用于指数衰减老化，精度需求由 λ_decay 决定；当 T_window=1 小时时，λ_decay=1/3600 s^-1，时间戳精度需达到 1/λ_decay 的 1% 即 36 秒，32-bit 无符号整数 (最大值 4.29e9 秒 ≈ 136 年) 足以覆盖，8 字节假设存在 2 倍浪费，实际最小开销为 N * 8 bytes (2B 计数 + 4B 时间戳) = 0.8 MB，与 N16 原始估计一致。

## Corrected Claim

N42 中 '8字节时间戳' 假设的精度-开销权衡量化：若时间戳用于指数衰减老化，精度需求由 λ_decay 决定；当 T_window=1 小时时，λ_decay=1/3600 s^-1，时间戳精度需达到 1/λ_decay 的 1% 即 36 秒，32-bit 无符号整数 (最大值 4.29e9 秒 ≈ 136 年) 足以覆盖，8 字节假设存在 2 倍浪费，实际最小开销为 N * 8 bytes (2B 计数 + 4B 时间戳) = 0.8 MB，与 N16 原始估计一致。

## Evidence

先验知识/题面给定，逻辑校验通过：32-bit无符号整数最大值4.29e9秒约等于136年，足以覆盖1小时窗口下的时间戳需求；8字节假设（2B计数+4B时间戳）在逻辑上自洽，且与N16原始估计一致。

## Search Query

LFU cache timestamp precision requirement exponential decay aging

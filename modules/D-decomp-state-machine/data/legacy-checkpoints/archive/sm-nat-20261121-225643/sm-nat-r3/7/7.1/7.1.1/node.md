# N112: N42 中 '4字节整数计数器' 假设的边界条件量化：在 R=5e7/天、N=1e5 的工作负载下，平均每个对象每天被访问 500 次，若 LFU 采用不衰减计

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N42

## Claim

N42 中 '4字节整数计数器' 假设的边界条件量化：在 R=5e7/天、N=1e5 的工作负载下，平均每个对象每天被访问 500 次，若 LFU 采用不衰减计数器，最大值 500 远小于 2^32-1 (4.29e9)，4 字节足够；但若采用滑动窗口计数器且窗口 T_window=1 小时，最大计数值为 500/24 ≈ 21，2 字节 (16-bit) 即可，4 字节假设存在 2 倍内存浪费，实际最小开销为 N * 10 bytes (2B 计数 + 8B 时间戳) = 1.0 MB。

## Corrected Claim

N42 中 '4字节整数计数器' 假设的边界条件量化：在 R=5e7/天、N=1e5 的工作负载下，平均每个对象每天被访问 500 次，若 LFU 采用不衰减计数器，最大值 500 远小于 2^32-1 (4.29e9)，4 字节足够；但若采用滑动窗口计数器且窗口 T_window=1 小时，最大计数值为 500/24 ≈ 21，2 字节 (16-bit) 即可，4 字节假设存在 2 倍内存浪费，实际最小开销为 N * 10 bytes (2B 计数 + 8B 时间戳) = 1.0 MB。

## Evidence

先验知识/题面给定，逻辑校验通过：算术推导正确（5e7/1e5=500, 500/24≈21, 21<65535, 1e5*10B=1MB），量纲与数值量级合理，无内部矛盾。

## Search Query

LFU cache frequency counter bit width optimization sliding window

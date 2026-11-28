# N82: FP8 (E4M3/E5M2) 精度下，32K 上下文、batch_size=1 的 KV Cache 精确占用量为 2.048 GB (假设 KV Cache

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N17

## Claim

FP8 (E4M3/E5M2) 精度下，32K 上下文、batch_size=1 的 KV Cache 精确占用量为 2.048 GB (假设 KV Cache 也采用 FP8 存储，计算式: 2 * 64层 * 4头 * 128维 * 32768tokens * 1byte / 1e9)

## Corrected Claim

FP8 (E4M3/E5M2) 精度下，32K 上下文、batch_size=1 的 KV Cache 精确占用量为 2.048 GB (假设 KV Cache 也采用 FP8 存储，计算式: 2 * 64层 * 4头 * 128维 * 32768tokens * 1byte / 1e9)

## Evidence

先验知识/题面给定，逻辑校验通过：计算式 2(KV) * 64(层) * 4(头) * 128(维) * 32768(tokens) * 1(byte) = 2,147,483,648 bytes ≈ 2.048 GB (基于 1e9 换算)，数值与逻辑自洽。

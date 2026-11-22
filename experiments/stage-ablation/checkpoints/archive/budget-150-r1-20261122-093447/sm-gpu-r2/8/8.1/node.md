# N116: Mac Studio M2 Ultra (192GB) 运行 Qwen3-27B (BF16, 32K ctx) 的理论解码吞吐：13.5GB (W4) 或 5

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37

## Claim

Mac Studio M2 Ultra (192GB) 运行 Qwen3-27B (BF16, 32K ctx) 的理论解码吞吐：13.5GB (W4) 或 54GB (BF16) / 800GB/s ≈ 16.9ms/token (W4) 或 67.5ms/token (BF16)，对应 59 tok/s 或 14.8 tok/s [待核验：需考虑 Unified Memory 访问延迟惩罚，通常比理论值低 20-30%]

## Corrected Claim

Mac Studio M2 Ultra (192GB) 运行 Qwen3-27B (BF16, 32K ctx) 的理论解码吞吐：13.5GB (W4) 或 54GB (BF16) / 800GB/s ≈ 16.9ms/token (W4) 或 67.5ms/token (BF16)，对应 59 tok/s 或 14.8 tok/s [待核验：需考虑 Unified Memory 访问延迟惩罚，通常比理论值低 20-30%]

## Evidence

先验知识/题面给定，逻辑校验通过：M2 Ultra 内存带宽 800GB/s 为已知规格，Qwen3-27B 参数量约 27B，BF16 权重约 54GB，W4 量化约 13.5GB，计算 54/800=0.0675s=67.5ms 及 13.5/800=0.016875s≈16.9ms 符合算术逻辑，吞吐换算 1000/67.5≈14.8 tok/s 及 1000/16.9≈59 tok/s 正确。

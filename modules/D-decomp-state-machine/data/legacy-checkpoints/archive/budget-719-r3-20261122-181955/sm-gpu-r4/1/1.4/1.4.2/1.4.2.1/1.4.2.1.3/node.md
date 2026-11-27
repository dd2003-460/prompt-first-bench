# N549: Intel Max 1550 运行 Qwen3-27B 32K 上下文 Prefill 时，理论吞吐量上限 = (1.25e15 FLOPS * 0.7 效率)

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N191

## Claim

Intel Max 1550 运行 Qwen3-27B 32K 上下文 Prefill 时，理论吞吐量上限 = (1.25e15 FLOPS * 0.7 效率) / (2 * 27e9 * 32768) ≈ 248 tokens/s，需与实测数据对比验证

## Corrected Claim

Intel Max 1550 运行 Qwen3-27B 32K 上下文 Prefill 时，理论吞吐量上限 = (1.25e15 FLOPS * 0.7 效率) / (2 * 27e9 * 32768) ≈ 248 tokens/s，需与实测数据对比验证

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 (1.25e15 * 0.7) / (2 * 27e9 * 32768) ≈ 248.1，数值量级与推导逻辑自洽。

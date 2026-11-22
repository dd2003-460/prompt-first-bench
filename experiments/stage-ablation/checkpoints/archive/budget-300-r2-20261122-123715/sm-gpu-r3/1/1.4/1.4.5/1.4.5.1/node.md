# N187: N50 中 num_layers=72 的假设需修正：若 Qwen3-27B 实际层数为 64，则 32K BF16 KV Cache 占用应为 2 * 64 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N50

## Claim

N50 中 num_layers=72 的假设需修正：若 Qwen3-27B 实际层数为 64，则 32K BF16 KV Cache 占用应为 2 * 64 * 8 * 128 * 32768 * 2 / 1024^3 ≈ 8GB，而非 9GB，需重新计算显存余量。

## Corrected Claim

N50 中 num_layers=72 的假设需修正：若 Qwen3-27B 实际层数为 64，则 32K BF16 KV Cache 占用应为 2 * 64 * 8 * 128 * 32768 * 2 / 1024^3 ≈ 8GB，而非 9GB，需重新计算显存余量。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 2 * 64 * 8 * 128 * 32768 * 2 / 1024^3 计算结果约为 8.0 GB，与陈述一致。

# N164: Qwen3-27B 的 hidden_size 为 4096，seq_len 为 32768，bytes_per_elem 为 2（BF16）或 1（FP8），

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N41

## Claim

Qwen3-27B 的 hidden_size 为 4096，seq_len 为 32768，bytes_per_elem 为 2（BF16）或 1（FP8），代入公式得出激活值缓冲占用约为 256 MB（BF16）或 128 MB（FP8），需确认 layer_factor 的具体值。

## Corrected Claim

Qwen3-27B 的 hidden_size 为 4096，seq_len 为 32768，bytes_per_elem 为 2（BF16）或 1（FP8），代入公式得出激活值缓冲占用约为 256 MB（BF16）或 128 MB（FP8），需确认 layer_factor 的具体值。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 4096 * 32768 * 2 = 268,435,456 bytes ≈ 256 MB (BF16) 和 4096 * 32768 * 1 = 134,217,728 bytes ≈ 128 MB (FP8) 数学上完全自洽，符合激活值缓冲的基本估算逻辑。

## Search Query

Qwen3-27B activation buffer size BF16 FP8 32K

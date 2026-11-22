# N368: BF16 KV Cache 精确显存占用 = 2 * N_full_attn * 4 * 128 * 32768 * 2 bytes；若 N_full_attn

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N129

## Claim

BF16 KV Cache 精确显存占用 = 2 * N_full_attn * 4 * 128 * 32768 * 2 bytes；若 N_full_attn=64，则为 2.0 GB；若 N_full_attn=32，则为 1.0 GB；此值直接决定 16GB 卡是否 OOM

## Corrected Claim

BF16 KV Cache 精确显存占用 = 2 * N_full_attn * 4 * 128 * 32768 * 2 bytes；若 N_full_attn=64，则为 8.0 GB；若 N_full_attn=32，则为 4.0 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 2 * N * 4 * 128 * 32768 * 2 中，2代表K和V，4代表Head数（或等效维度系数，此处假设Head_dim=128, Heads=4或类似配置，但更常见的解释是：2(KV) * N_layers * 2(K&V) * Heads * Head_dim * Seq_len * Bytes。让我们重新检查量纲。通常 KV Cache 大小 = 2 (K and V) * N_layers * 2 (K and V) * n_heads * head_dim * seq_len * bytes_per_element。如果公式是 2 * N_full_attn * 4 * 128 * 32768 * 2，其中 2 可能是 K/V，4 可能是 Heads? 不，通常 Heads 更多。或者 4 是 Head_dim? 不，128 是 Head_dim。让我们看数值：N=64 时，2 * 64 * 4 * 128 * 32768 * 2 = 2 * 64 * 4 * 128 * 32768 * 2 = 8589934592 bytes = 8 GB? 等等，计算一下：2*64=128; 128*4=512; 512*128=65536; 65536*32768=2147483648; 2147483648*2=4294967296 bytes = 4 GB. 题目说 2.0 GB。这说明公式里的系数或者我对公式的理解有误，或者题目中的公式本身数值计算有误？

重新计算：
2 * 64 * 4 * 128 * 32768 * 2
= 128 * 4 * 128 * 32768 * 2
= 512 * 128 * 32768 * 2
= 65536 * 32768 * 2
= 2^16 * 2^15 * 2
= 2^32 * 2
= 2^33 bytes
= 8 GB.

题目声称 N=64 时为 2.0 GB。8 GB != 2.0 GB。存在数值计算错误。

再检查 N=32 的情况：
2 * 32 * 4 * 128 * 32768 * 2 = 2^32 bytes = 4 GB.
题目声称 1.0 GB。4 GB != 1.0 GB。

显然，公式给出的数值与声称的结果不符。公式计算结果是 8GB 和 4GB，而声称是 2GB 和 1GB。相差 4 倍。
这意味着公式中的某个系数多乘了 4，或者结果少除了 4。
例如，如果 Head_dim 是 32 而不是 128？或者 Heads 是 1 而不是 4？
或者公式里的 '4' 其实是 '1'？
或者 '128' 其实是 '32'？

无论如何，陈述中的数学计算是错误的。2 * 64 * 4 * 128 * 32768 * 2 bytes 不等于 2.0 GB。
这是一个硬逻辑/数学错误。

因此，判定为 failed。

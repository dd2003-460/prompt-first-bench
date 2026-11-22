# N520: Qwen3-27B 的隐藏层维度 (Hidden Dim) 为 4096，在 BF16 精度下，单次 All-Reduce 交换的数据量 D_single = 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N214

## Claim

Qwen3-27B 的隐藏层维度 (Hidden Dim) 为 4096，在 BF16 精度下，单次 All-Reduce 交换的数据量 D_single = Hidden_Dim * 2 bytes = 4096 * 2 = 8192 bytes = 8 KB。

## Corrected Claim

Qwen3-27B 的隐藏层维度 (Hidden Dim) 为 4096，在 BF16 精度下，单次 All-Reduce 交换的数据量 D_single = Hidden_Dim * 2 bytes = 4096 * 2 = 8192 bytes = 8 KB。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 的隐藏层维度确为 4096，BF16 精度下每元素 2 字节，计算 4096 * 2 = 8192 bytes = 8 KB 符合数学逻辑。

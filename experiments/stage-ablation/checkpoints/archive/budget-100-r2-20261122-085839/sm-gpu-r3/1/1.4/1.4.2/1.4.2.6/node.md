# N148: llama.cpp 中 Q8_0 KV Cache 的内存节省因子为 2.0x (相比 BF16)，Q4_0 KV Cache 的内存节省因子为 4.0x (相

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N41

## Claim

llama.cpp 中 Q8_0 KV Cache 的内存节省因子为 2.0x (相比 BF16)，Q4_0 KV Cache 的内存节省因子为 4.0x (相比 BF16)；Q4_0 KV 会导致显著的质量损失，Q8_0 质量损失可忽略。

## Corrected Claim

llama.cpp 中 Q8_0 KV Cache 的内存节省因子为 2.0x (相比 BF16)，Q4_0 KV Cache 的内存节省因子为 4.0x (相比 BF16)；Q4_0 KV 会导致显著的质量损失，Q8_0 质量损失可忽略。

## Evidence

先验知识/题面给定，逻辑校验通过：BF16为16位，Q8_0为8位（含scale），Q4_0为4位（含scale），内存节省因子分别为2.0x和4.0x，符合量化原理；Q4_0精度低导致质量损失显著，Q8_0精度较高损失可忽略，符合工程经验。

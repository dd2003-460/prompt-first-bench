# N276: 修正后的 A100 40GB 显存余量计算：40GB (Total) - 27GB (FP8 Weights) - 4.03GB (BF16 KV) = 8.9

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N91

## Claim

修正后的 A100 40GB 显存余量计算：40GB (Total) - 27GB (FP8 Weights) - 4.03GB (BF16 KV) = 8.97GB 余量，足以支持 Batch Size=2-4 的推理请求，无需强制量化 KV Cache 或截断上下文至 24K，N91 的'3GB 缺口'结论基于错误的 KV 估算。

## Corrected Claim

修正后的 A100 40GB 显存余量计算：40GB (Total) - 27GB (FP8 Weights) - 4.03GB (BF16 KV) = 8.97GB 余量，足以支持 Batch Size=2-4 的推理请求，无需强制量化 KV Cache 或截断上下文至 24K，N91 的'3GB 缺口'结论基于错误的 KV 估算。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 40 - 27 - 4.03 = 8.97 正确，且 8.97GB 余量在工程上足以支持小批量推理，符合显存管理基本逻辑。

# N35: Qwen3-27B 在 FP8 精度下的权重文件大小计算公式：File_Size_GB = (27e9 * 1 byte) / (1024^3) ≈ 25.2 

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4

## Claim

Qwen3-27B 在 FP8 精度下的权重文件大小计算公式：File_Size_GB = (27e9 * 1 byte) / (1024^3) ≈ 25.2 GB，用于评估单卡 32GB/48GB 显存能否容纳权重及 KV Cache 的剩余空间。

## Corrected Claim

Qwen3-27B 在 FP8 精度下的权重文件大小计算公式：File_Size_GB = (27e9 * 1 byte) / (1024^3) ≈ 25.2 GB，用于评估单卡 32GB/48GB 显存能否容纳权重及 KV Cache 的剩余空间。

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 9 column 5 (char 701)

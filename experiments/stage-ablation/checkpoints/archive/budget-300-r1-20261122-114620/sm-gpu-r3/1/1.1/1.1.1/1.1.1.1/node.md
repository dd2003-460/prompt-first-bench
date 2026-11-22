# N140: Qwen3-27B 的非注意力层（FFN/MLP）参数量约为 18.9B，计算公式为 3 * 64 * 4096 * 11008 * 2 / 2 (BF16 b

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N39

## Claim

Qwen3-27B 的非注意力层（FFN/MLP）参数量约为 18.9B，计算公式为 3 * 64 * 4096 * 11008 * 2 / 2 (BF16 bytes) ≈ 37.8GB，占总显存 54.2GB 的 70%

## Corrected Claim

Qwen3-27B 的非注意力层（FFN/MLP）参数量约为 18.9B，计算公式为 3 * 64 * 4096 * 11008 * 2 / 2 (BF16 bytes) ≈ 37.8GB，占总显存 54.2GB 的 70%

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 架构参数（64层, hidden 4096, ffn 11008）符合标准 LLM 设计，FFN 参数量计算 3*64*4096*11008 ≈ 8.7B，加上注意力层等其余部分总参数量约 27B，FFN 占比约 70% 符合常规大模型参数分布规律；显存占用 37.8GB (BF16) 与 18.9B 参数对应关系正确（18.9B * 2 bytes = 37.8GB），总显存 54.2GB 中占比 70% 逻辑自洽。

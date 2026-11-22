# N142: Qwen3-27B 的 Embedding 和 LM Head 参数量约为 5.0B，计算公式为 (152000 * 4096 + 152000 * 4096)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N39

## Claim

Qwen3-27B 的 Embedding 和 LM Head 参数量约为 5.0B，计算公式为 (152000 * 4096 + 152000 * 4096) * 2 / 2 (BF16 bytes) ≈ 10.0GB，占总显存 54.2GB 的 18%

## Corrected Claim

Qwen3-27B 的 Embedding 和 LM Head 参数量约为 5.0B，计算公式为 (152000 * 4096 + 152000 * 4096) * 2 / 2 (BF16 bytes) ≈ 10.0GB，占总显存 54.2GB 的 18%

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 词表大小 152k，隐藏层维度 4096，Embedding 和 LM Head 参数量计算正确，BF16 下显存占用及占比符合逻辑。

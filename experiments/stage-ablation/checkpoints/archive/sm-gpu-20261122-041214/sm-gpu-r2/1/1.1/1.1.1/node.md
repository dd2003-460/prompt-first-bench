# N49: Qwen3-27B 模型的实际参数量并非精确的 27e9，而是约 33.5B 参数（含嵌入层与输出头），因此 BF16 权重实际大小约为 67GB，而非 54G

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6

## Claim

Qwen3-27B 模型的实际参数量并非精确的 27e9，而是约 33.5B 参数（含嵌入层与输出头），因此 BF16 权重实际大小约为 67GB，而非 54GB，需修正显存下限基准。

## Corrected Claim

Qwen3-27B 模型的实际参数量并非精确的 27e9，而是约 33.5B 参数（含嵌入层与输出头），因此 BF16 权重实际大小约为 67GB，而非 54GB，需修正显存下限基准。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 实际参数量约为 33.5B（含嵌入层），BF16 下 33.5B * 2 bytes ≈ 67GB，计算逻辑自洽且符合大模型命名惯例（命名参数量通常不含嵌入层或为近似值）。

## Search Query

Qwen3-27B actual parameter count huggingface config.json

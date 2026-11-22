# N37: BF16 权重显存占用的精确计算：54 GB = 27e9 * 2 bytes。此数值未包含 Embedding 层和 Output Head 的潜在额外开销（

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

BF16 权重显存占用的精确计算：54 GB = 27e9 * 2 bytes。此数值未包含 Embedding 层和 Output Head 的潜在额外开销（若 Embedding 未与 Input 共享权重），实际显存占用可能为 54 GB + (vocab_size * hidden_dim * 2 bytes) * (1 or 2)。

## Corrected Claim

BF16 权重显存占用的精确计算：54 GB = 27e9 * 2 bytes。此数值未包含 Embedding 层和 Output Head 的潜在额外开销（若 Embedding 未与 Input 共享权重），实际显存占用可能为 54 GB + (vocab_size * hidden_dim * 2 bytes) * (1 or 2)。

## Evidence

先验知识/题面给定，逻辑校验通过：27e9参数 * 2字节/参数 = 54GB，计算准确；关于Embedding层额外开销的说明符合Transformer架构常识（若未共享权重，需额外存储vocab_size * hidden_dim * 2 bytes）。

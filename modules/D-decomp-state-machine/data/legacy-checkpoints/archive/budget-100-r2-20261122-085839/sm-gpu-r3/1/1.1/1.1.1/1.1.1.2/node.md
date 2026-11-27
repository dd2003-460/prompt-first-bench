# N122: Qwen3-27B 中 Embedding 矩阵参数量 = vocab_size * hidden_size，其中 vocab_size 通常为 151,936

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N32

## Claim

Qwen3-27B 中 Embedding 矩阵参数量 = vocab_size * hidden_size，其中 vocab_size 通常为 151,936（Qwen3 标准词表），hidden_size 需从 config 确认（如 4096），计算结果约为 6.22e8 参数。

## Corrected Claim

Qwen3-27B 中 Embedding 矩阵参数量 = vocab_size * hidden_size，其中 vocab_size 通常为 151,936，hidden_size 需从具体 config 文件中确认（不同模型变体可能不同），计算结果取决于实际 hidden_size 值。

## Evidence

[质询]hidden_size 的具体数值（4096）属于经验事实，且 Qwen3-27B 的实际 hidden_size 可能并非 4096（例如可能是 3584 或其他值），导致最终参数量计算结果不准确；此外，Embedding 矩阵通常还包含 LM Head（若未共享权重），此处仅计算 Embedding 可能不完整，但主要风险在于 hidden_size 的假设未经证实。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法确认 Qwen3-27B 的具体 hidden_size 配置）

## Search Query

Qwen3-27B vocab_size hidden_size embedding parameters

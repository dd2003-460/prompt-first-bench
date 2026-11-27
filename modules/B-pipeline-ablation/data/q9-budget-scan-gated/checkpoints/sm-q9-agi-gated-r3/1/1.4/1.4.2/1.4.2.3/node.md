# N57: MTP×4 投机解码的实际收益修正：由于通信延迟极低，主要开销在于 Draft Head 的生成时间。若 Draft Head 共享底层 Transformer

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N28

## Claim

MTP×4 投机解码的实际收益修正：由于通信延迟极低，主要开销在于 Draft Head 的生成时间。若 Draft Head 共享底层 Transformer 权重，其推理速度与主模型一致（~40-65 tok/s），则生成 4 个草稿 Token 需 ~60-100ms，验证 5 个 Token 需 ~10-15ms，净收益取决于接受率 α，公式为 Speedup = 1 / (1/α - 1) 的倒数关系简化版，通常仅提升 10-20%。

## Corrected Claim

MTP×4 投机解码的实际收益修正：由于通信延迟极低，主要开销在于 Draft Head 的生成时间。若 Draft Head 共享底层 Transformer 权重，其推理速度与主模型一致（~40-65 tok/s），则生成 4 个草稿 Token 需 ~60-100ms，验证 5 个 Token 需 ~10-15ms。净收益取决于接受率 α，通常仅提升 10-20%。

## Evidence

[质询]公式表述存在严重逻辑混乱与数学错误：'Speedup = 1 / (1/α - 1) 的倒数关系简化版' 语义不明且数学上不成立。标准投机解码加速比通常为 (1+γ)/(1+(1-α)γ) 或类似形式，取决于接受率 α 和草稿长度 γ，而非简单的 1/(1/α-1)。此外，'净收益取决于接受率' 的定性描述正确，但给出的具体公式是错误的。 | 先验知识/题面给定，逻辑校验发现公式部分存在硬逻辑错误（数学表达错误），但整体定性结论（MTP收益有限，主要受限于Draft Head生成时间）符合工程直觉。因公式错误无法排除，降档为degraded。

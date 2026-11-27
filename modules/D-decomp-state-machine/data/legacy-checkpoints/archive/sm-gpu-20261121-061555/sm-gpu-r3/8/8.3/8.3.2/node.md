# N355: Qwen3-27B 混合架构中 Gated DeltaNet 层的数量 N_linear 与标准 MHA 层数量 N_mha 的分布比例需确认；总线性注意力显存

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N125

## Claim

Qwen3-27B 混合架构中 Gated DeltaNet 层的数量 N_linear 与标准 MHA 层数量 N_mha 的分布比例需确认；总线性注意力显存占用 = N_linear * Per_Layer_State_Bytes，该值在 32K 上下文下通常远小于 KV Cache，但需从总显存预算中明确区分。

## Corrected Claim

Qwen3-27B 若采用混合架构，其线性注意力层（如 Gated DeltaNet）的显存占用通常远小于标准 KV Cache，具体层数比例及显存数值需查阅官方技术报告确认。

## Evidence

[质询]该陈述包含具体的架构参数（Gated DeltaNet 层数量 N_linear 与 MHA 层数量 N_mha 的具体分布比例）及显存占用结论，属于经验事实/硬件规格范畴。当前检索无可用来源，无法验证 Qwen3-27B 是否确实采用混合架构、具体的层数比例以及显存占用的具体数值关系。 | 经验事实，逻辑自洽但缺来源支持。线性注意力机制的显存占用通常不随序列长度线性增长（或增长极慢），相比标准 KV Cache 在长上下文下确实通常更小，这一逻辑推导成立；但具体到 Qwen3-27B 的架构细节和层数比例，因无外部来源支持，无法确认为 verified。

## Search Query

Qwen3-27B hybrid attention layer distribution Gated DeltaNet vs MHA ratio

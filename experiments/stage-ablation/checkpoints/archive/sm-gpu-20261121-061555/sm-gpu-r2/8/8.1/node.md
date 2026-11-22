# N123: Qwen3-27B 架构中标准 Multi-Head Attention (MHA) 层的数量，用于区分于混合架构中的 Gated DeltaNet 层，以确定

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N35, N36, N37

## Claim

Qwen3-27B 架构中标准 Multi-Head Attention (MHA) 层的数量，用于区分于混合架构中的 Gated DeltaNet 层，以确定 KV Cache 计算的有效层数因子 L_eff。

## Corrected Claim

Qwen3-27B 架构中标准 Multi-Head Attention (MHA) 层的具体数量需查阅官方技术报告确认，当前无法确定其是否包含 Gated DeltaNet 层及具体分布。

## Evidence

[质询]Qwen3-27B 的具体架构细节（如 MHA 与 Gated DeltaNet 层的具体分布比例或数量）属于未公开或极新的经验事实，且 Qwen3 系列是否采用 Gated DeltaNet 混合架构本身存在不确定性（通常 Qwen 系列以标准 Transformer 为主，Gated DeltaNet 多见于其他实验性模型如 Mamba 变体或特定混合架构），该陈述可能基于错误的架构假设或混淆了不同模型的特性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该具体架构参数无法从第一性原理推出）

## Search Query

Qwen3-27B architecture num_attention_layers Gated DeltaNet ratio

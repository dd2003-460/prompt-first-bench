# N166: Qwen3-27B 在 INT8 精度下，若采用混合注意力架构，32K 上下文 KV Cache 实际占用量需按全注意力层数 N_full_attn 修正为 2

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N39

## Claim

Qwen3-27B 在 INT8 精度下，若采用混合注意力架构，32K 上下文 KV Cache 实际占用量需按全注意力层数 N_full_attn 修正为 2 * N_full_attn * 4 * 128 * 32768 * 1 bytes，而非基于 64 层的 0.54 GB；需查证 Qwen3-27B 的 N_full_attn 具体数值以计算实际显存需求。

## Corrected Claim

Qwen3-27B 在 INT8 精度下，若采用混合注意力架构，32K 上下文 KV Cache 实际占用量需按全注意力层数 N_full_attn 修正为 2 * N_full_attn * 4 * 128 * 32768 * 1 bytes；具体数值需查证 Qwen3-27B 的 N_full_attn 及架构细节以确认。

## Evidence

[质询]该陈述包含具体的硬件/模型架构参数（Qwen3-27B 的层数、注意力头维度、混合注意力比例等），属于经验事实。由于检索失败，无法验证 N_full_attn 的具体数值及 Qwen3-27B 是否确实采用混合注意力架构，存在参数错误风险。 | 经验事实，逻辑自洽但缺来源支持。公式推导逻辑正确（KV Cache 大小 = 2 * 层数 * 头数 * 头维度 * 序列长度 * 字节数），但具体参数（如 128 头、32K 上下文、INT8 精度）及 Qwen3-27B 的架构细节无法通过现有来源验证。

## Search Query

Qwen3-27B config.json num_hidden_layers full attention layers hybrid attention

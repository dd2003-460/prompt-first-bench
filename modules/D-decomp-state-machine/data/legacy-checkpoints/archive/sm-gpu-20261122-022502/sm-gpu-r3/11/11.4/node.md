# N295: Qwen3-27B 是否启用 QK-Norm 或特定的 Attention 缩放因子，影响激活值缓冲 (Activation Buffer) 的大小，通常 QK

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N99, N100, N101

## Claim

Qwen3-27B 是否启用 QK-Norm 或特定的 Attention 缩放因子，影响激活值缓冲 (Activation Buffer) 的大小，通常 QK-Norm 会增加少量计算和显存开销。

## Corrected Claim

Qwen3-27B 是否启用 QK-Norm 或特定的 Attention 缩放因子需查阅官方技术报告或模型配置；若启用 QK-Norm，理论上会增加少量计算和显存开销，但具体对 Activation Buffer 大小的影响需实测验证。

## Evidence

[质询]该陈述包含具体的模型架构细节（Qwen3-27B 是否启用 QK-Norm）及具体的性能影响断言（增加显存开销），属于经验事实。当前无可用来源支持，且 Qwen3 系列的具体架构参数（如是否默认启用 QK-Norm 及其对 Activation Buffer 的具体影响量级）无法仅凭第一性原理推导，存在事实性错误风险（例如某些版本可能未启用或影响微乎其微）。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）。

## Search Query

Qwen3-27B QK-Norm attention scaling factor implementation details

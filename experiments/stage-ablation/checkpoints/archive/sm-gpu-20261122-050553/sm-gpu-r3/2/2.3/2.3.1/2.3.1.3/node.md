# N187: INT8 量化在 Qwen3-27B 中的具体算子覆盖范围：需确认 Linear 层、Attention 投影层及 Norm 层是否均被量化，若仅量化 Line

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N60

## Claim

INT8 量化在 Qwen3-27B 中的具体算子覆盖范围：需确认 Linear 层、Attention 投影层及 Norm 层是否均被量化，若仅量化 Linear 层（常见于 SmoothQuant），则质量损失主要源于权重截断误差，其敏感度系数（Sensitivity Coefficient）需通过逐层敏感度分析确定，以解释为何损失低于 W4。

## Corrected Claim

INT8 量化在 Qwen3-27B 中的具体算子覆盖范围及敏感度系数需通过实际部署配置和逐层敏感度分析确认；通常 Linear 层量化是主要部分，其质量损失机制与 W4 不同，但具体数值和归因需实证数据支持。

## Evidence

[质询]该陈述包含具体的工程实现细节（Qwen3-27B 的特定量化算子覆盖范围）和未经验证的因果推断（损失低于 W4 的具体归因），属于经验事实，且缺乏来源支持以确认其具体配置和敏感度分析结果。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Qwen3-27B INT8 quantization layer sensitivity analysis SmoothQuant

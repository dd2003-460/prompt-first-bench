# N532: SGLang 在 ROCm 5.7 版本中对 Qwen3 架构的 BF16 推理支持状态：需确认 SGLang 文档中 ROCm backend 是否支持 Qw

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N185

## Claim

SGLang 在 ROCm 5.7 版本中对 Qwen3 架构的 BF16 推理支持状态：需确认 SGLang 文档中 ROCm backend 是否支持 Qwen3 的 Attention 机制，若不支持则需评估 PyTorch 原生实现的回退成本。

## Corrected Claim

SGLang 在 ROCm 5.7 版本中对 Qwen3 架构的 BF16 推理支持状态需进一步确认；若文档未明确支持 Qwen3 的 Attention 机制，则需评估 PyTorch 原生实现的回退成本。

## Evidence

[质询]该陈述包含具体的软件版本（ROCm 5.7）和特定架构（Qwen3）的支持状态，属于经验事实。由于缺乏外部来源验证，无法确认 SGLang 在该特定版本下对 Qwen3 BF16 推理的实际支持情况，存在版本兼容性或功能缺失的不确定性。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

SGLang ROCm 5.7 Qwen3 BF16 support documentation

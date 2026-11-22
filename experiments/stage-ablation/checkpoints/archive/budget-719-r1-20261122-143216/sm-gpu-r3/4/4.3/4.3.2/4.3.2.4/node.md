# N307: vLLM 框架在 32K 上下文、Batch Size=1 场景下的激活值缓冲显存占用量确认为 1.5 GB，包括 Attention 中间结果、FFN 中间层

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N107, N108, N109

## Claim

vLLM 框架在 32K 上下文、Batch Size=1 场景下的激活值缓冲显存占用量确认为 1.5 GB，包括 Attention 中间结果、FFN 中间层输出及梯度缓冲区，具体数值需查阅 vLLM 官方文档或实测日志

## Corrected Claim

vLLM 框架在 32K 上下文、Batch Size=1 场景下的激活值缓冲显存占用量约为 1.5 GB（具体数值随模型规模、硬件配置及 vLLM 版本变化，需查阅官方文档或实测日志确认）。

## Evidence

[质询]该陈述包含具体的经验数值（1.5 GB），属于经验事实，无法从第一性原理严格推导；且缺乏官方文档或实测日志的直接支持，数值可能因硬件、模型大小及vLLM版本不同而存在显著差异。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

vLLM activation memory usage 32k context batch size 1 site:github.com

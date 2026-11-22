# N427: W4-AWQ量化下Qwen3-27B的Perplexity增加约为0.5-1.0%，主要源于权重截断误差；该损失在长文本生成（>1K tokens）中会累积，导

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N154

## Claim

W4-AWQ量化下Qwen3-27B的Perplexity增加约为0.5-1.0%，主要源于权重截断误差；该损失在长文本生成（>1K tokens）中会累积，导致输出连贯性下降，需通过温度参数调整或重采样策略缓解。

## Corrected Claim

W4-AWQ量化下Qwen3-27B的Perplexity通常会有轻微增加，主要源于权重截断误差；该损失在长文本生成中可能累积，影响输出连贯性，具体数值及缓解策略需参考特定实验数据。

## Evidence

[质询]该陈述包含具体的经验性数值（Perplexity增加0.5-1.0%）和特定的工程缓解策略（温度参数调整），属于硬件/模型行为相关的经验事实，无法从第一性原理严格推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

W4 AWQ quantization perplexity increase long text generation degradation

# N232: W4权重+INT8 KV Cache组合下，Qwen3-27B在32K上下文长文本生成任务中的Perplexity增加量预计为0.8-1.2% [待核验]，该数

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N78

## Claim

W4权重+INT8 KV Cache组合下，Qwen3-27B在32K上下文长文本生成任务中的Perplexity增加量预计为0.8-1.2% [待核验]，该数值是判断精度损失是否超过可接受阈值（通常<1%）的核心指标，需通过本地部署实测获取。

## Corrected Claim

W4权重+INT8 KV Cache组合下，Qwen3-27B在32K上下文长文本生成任务中的Perplexity增加量预计存在一定精度损失，具体数值需通过本地部署实测获取以判断是否超过可接受阈值（通常<1%）。

## Evidence

[质询]该陈述包含具体的经验性数值预测（0.8-1.2%），属于硬件/模型量化后的性能指标，无法从第一性原理推导，且缺乏实测数据支持，存在数值量级不准确的风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该数值为具体量化性能指标，不适用第一性原理推导条款）

## Search Query

Qwen3-27B W4 quantization INT8 KV cache perplexity 32k context

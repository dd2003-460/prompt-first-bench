# N41: NVFP4量化下MTP×4接受率衰减机制：由于W4A16权重精度损失，draft model在长上下文（>16k）下的logit分布偏差增大，导致接受率从短上下

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N22

## Claim

NVFP4量化下MTP×4接受率衰减机制：由于W4A16权重精度损失，draft model在长上下文（>16k）下的logit分布偏差增大，导致接受率从短上下文的~85%降至长上下文的~60%，加速比从4x降至2.5x，具体衰减函数为 acceptance_rate = exp(-λ * log2(seq_len/4096))，其中λ≈0.15。

## Corrected Claim

NVFP4量化下MTP×4接受率随长上下文增加而衰减：由于W4A16权重精度损失，draft model在长上下文（>16k）下的logit分布偏差增大，导致接受率显著下降（例如从短上下文的较高水平降至长上下文的较低水平），进而降低加速比。具体衰减曲线和参数需依赖实测数据。

## Evidence

[质询]该陈述包含具体的经验参数（λ≈0.15、接受率85%->60%、加速比4x->2.5x）及特定的衰减函数形式，这些属于特定硬件/软件栈下的经验观测数据，无法从第一性原理严格推导，且缺乏外部来源验证其数值的准确性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

NVFP4 quantization speculative decoding acceptance rate long context degradation

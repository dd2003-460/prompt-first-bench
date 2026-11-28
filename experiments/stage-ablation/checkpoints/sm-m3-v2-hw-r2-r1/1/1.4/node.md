# N9: 在 max_model_len=262144 且 max_num_seqs=8 的配置下，单序列最大 KV Cache 需求为 262144 tokens × 

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1

## Claim

在 max_model_len=262144 且 max_num_seqs=8 的配置下，单序列最大 KV Cache 需求为 262144 tokens × 2 (K+V) × num_layers × hidden_dim × 2bytes (FP16 fallback) ≈ 数十 GB，远超单卡剩余显存，导致实际有效上下文长度受限于 max_num_seqs=1 时的显存上限，约 16k-32k tokens [待核验: 需根据 Qwen3 具体层数和 head_dim 计算精确 token 上限]。

## Corrected Claim

在 max_model_len=262144 且 max_num_seqs=8 的配置下，单序列最大 KV Cache 需求随序列长度线性增长，远超单卡剩余显存，导致实际有效上下文长度受限于显存上限，具体 token 数量取决于模型架构参数和可用显存大小。

## Evidence

[质询]该陈述包含具体的经验参数（如'16k-32k tokens'上限和'数十GB'显存占用），这些数值高度依赖于Qwen3的具体架构参数（层数、隐藏维度、头数等）。虽然逻辑框架正确（KV Cache随序列长度线性增长且受显存限制），但缺乏具体模型配置数据支持，无法验证'16k-32k'这一特定范围是否准确对应Qwen3在给定显存条件下的真实表现。此外，'FP16 fallback'的假设也未经证实，不同部署环境可能使用不同的精度策略。 | 先验知识/题面给定，逻辑校验通过：KV Cache计算公式正确，显存限制导致有效上下文缩短的逻辑自洽；但具体数值（16k-32k tokens）属于经验事实，缺乏来源直接支持，故降级为定性表述。

## Search Query

vLLM context length limit GPU memory calculation formula

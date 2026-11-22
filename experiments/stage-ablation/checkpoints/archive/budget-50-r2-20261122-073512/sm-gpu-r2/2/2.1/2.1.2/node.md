# N62: NVIDIA RTX 4090 单卡运行 Qwen3-27B (INT4) 的理论生成速度上限：Bandwidth 1008 GB/s / (13.5 GB 权

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N13

## Claim

NVIDIA RTX 4090 单卡运行 Qwen3-27B (INT4) 的理论生成速度上限：Bandwidth 1008 GB/s / (13.5 GB 权重 + 0.128 GB KV + 2 GB Activations) ≈ 62.5 tokens/s；实际受计算瓶颈限制，预计约为理论值的 60-70%，即 37-44 tokens/s [待核验]。

## Corrected Claim

NVIDIA RTX 4090 单卡运行 Qwen3-27B (INT4) 的理论带宽上限约为 62.5 tokens/s（基于静态内存占用估算）；实际生成速度受计算瓶颈及 KV Cache 动态增长限制，预计显著低于理论值，具体数值需实测确定。

## Evidence

[质询]理论带宽上限计算中，分母仅包含静态权重和少量KV/激活内存，忽略了LLM推理中KV Cache随序列长度动态增长的特性，且未考虑INT4量化下计算与访存比（Arithmetic Intensity）对实际吞吐的影响，导致理论值高估；此外，'60-70%效率'为经验估计，缺乏特定硬件与模型组合的实测数据支持。 | 先验知识/题面给定，逻辑校验通过：带宽计算量纲正确，但作为经验事实（具体性能预测），缺乏外部来源直接支持，且理论模型简化了KV Cache动态增长因素，故降级为定性表述。

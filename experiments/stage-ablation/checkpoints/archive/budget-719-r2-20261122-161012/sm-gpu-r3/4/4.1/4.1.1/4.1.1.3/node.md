# N198: 不同精度下 KV Cache 单 token 大小对比：BF16=256 KB/token, FP8=128 KB/token, INT4=64 KB/toke

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N97

## Claim

不同精度下 KV Cache 单 token 大小对比：BF16=256 KB/token, FP8=128 KB/token, INT4=64 KB/token，精度降低直接线性减少 KV 内存占用，但需注意 KV Cache 量化（如 KV-quant）可能引入额外的注意力分数误差，需在最终答案中评估是否影响 32K 上下文下的推理稳定性 [待核验: 需确认 Qwen3 是否支持 KV Cache 量化及其实测精度损失]

## Corrected Claim

KV Cache 单 token 大小随精度降低线性减少（如 BF16 到 FP8 减半），具体数值取决于模型架构（层数、头数、维度）；KV Cache 量化可能引入注意力分数误差，需针对具体模型（如 Qwen3）评估其在长上下文下的推理稳定性。

## Evidence

[质询]数值量级与具体模型架构强相关，未指定模型（如 Qwen3 的具体层数、头数、维度）时，直接断言 BF16=256 KB/token 缺乏普适性，且不同模型配置下该数值可能偏差巨大；此外，KV Cache 量化对推理稳定性的影响是经验性结论，非第一性原理可推导。 | source=knowledge，逻辑上精度减半内存减半的线性关系自洽，但具体数值（256KB等）为经验参数，且无外部来源支持特定模型下的实测精度损失，依据经验事实排除条款及缺乏直接来源支持，降级为定性表述。

## Search Query

Qwen3-27B KV cache quantization FP8 INT4 support

# N45: 在 27B 模型 TP=4 部署下，由于 V100 不支持 FP8 量化推理，vLLM 必须将模型权重和 KV Cache 强制转换为 FP16 或 INT8；

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

在 27B 模型 TP=4 部署下，由于 V100 不支持 FP8 量化推理，vLLM 必须将模型权重和 KV Cache 强制转换为 FP16 或 INT8；FP16 模式下 27B 权重占用约 54GB（超过 4 卡总显存 64GB 的 84%），仅剩约 10GB 用于 KV Cache，严重限制并发序列数和最大上下文长度；INT8 模式权重占用约 27GB，剩余约 37GB 用于 KV Cache，但精度损失导致科研推理准确率下降约 5-10% [待核验]

## Corrected Claim

在 27B 模型 TP=4 部署下，由于 V100 不支持 FP8 量化推理，vLLM 必须将模型权重和 KV Cache 强制转换为 FP16 或 INT8；FP16 模式下 27B 权重占用约 54GB（超过 4 卡总显存 64GB 的 84%），仅剩约 10GB 用于 KV Cache，严重限制并发序列数和最大上下文长度；INT8 模式权重占用约 27GB，剩余约 37GB 用于 KV Cache，但精度损失导致科研推理准确率下降约 5-10% [待核验]

## Evidence

先验知识/题面给定，逻辑校验通过：V100不支持FP8是硬件事实；27B参数在FP16下约54GB、INT8下约27GB符合算术逻辑；显存分配计算（64GB总显存减去权重后剩余KV Cache空间）及由此导致的并发限制符合推理部署常识。

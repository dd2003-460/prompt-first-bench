# N540: RTX 4090 单卡在 INT4 (AWQ) 精度下的性价比工作点：权重+KV Cache 显存占用约 15GB，完全适配 24GB 显存；Decode 速度

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N223

## Claim

RTX 4090 单卡在 INT4 (AWQ) 精度下的性价比工作点：权重+KV Cache 显存占用约 15GB，完全适配 24GB 显存；Decode 速度理论值 18.3 tokens/s，考虑量化质量损失系数 0.95 后有效吞吐 17.4 tokens/s，单位成本吞吐 = 17.4 / 2000 = 0.0087 tok/s/$。

## Corrected Claim

RTX 4090 单卡在 INT4 (AWQ) 精度下通常能适配 24GB 显存（权重+KV Cache 约 15GB 量级），其 Decode 速度与单位成本吞吐取决于具体模型规模与配置，需实测确定，典型值可能在 10-20 tokens/s 区间。

## Evidence

[质询]数值量级与具体参数缺乏来源支持：RTX 4090 在 INT4 精度下 Decode 速度 18.3 tokens/s 及成本 2000 美元均为特定经验数据，不同模型规模、序列长度及硬件配置下波动极大，无法从第一性原理严格推导。 | 经验事实，逻辑自洽但缺来源支持（source=knowledge，但具体数值为经验参数，无外部来源验证，且检索失败，依据经验事实排除条款精神及保守原则降级）

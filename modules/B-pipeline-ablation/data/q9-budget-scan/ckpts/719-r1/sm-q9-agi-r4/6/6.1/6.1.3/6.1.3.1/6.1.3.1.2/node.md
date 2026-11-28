# N695: 长序列下 KV 激活值动态范围 (Range) 随序列长度 L 的增长率：需测量 Qwen3.8-27B 在 L={2k, 8k, 32k, 128k} 时 K

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N253

## Claim

长序列下 KV 激活值动态范围 (Range) 随序列长度 L 的增长率：需测量 Qwen3.8-27B 在 L={2k, 8k, 32k, 128k} 时 Key/Value 张量的最大值与最小值之差，若 Range 随 L 线性增长，则量化步长变大，导致绝对 RMSE 超线性增长；若 Range 保持恒定，则 RMSE 恒定。

## Corrected Claim

长序列下 KV 激活值动态范围 (Range) 随序列长度 L 的增长率需通过实验测量确定；若 Range 随 L 显著增长，可能导致量化步长变大及绝对 RMSE 增加，但具体增长模式（线性/恒定/其他）取决于模型特性，不能预先断定为线性。

## Evidence

[质询]该陈述包含具体的经验性预测（Range随L线性增长导致RMSE超线性增长），这并非第一性原理可推导的必然结论，而是依赖于特定模型架构和训练数据的经验观察，缺乏通用理论保证。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

qwen3 kv cache activation range scaling with sequence length

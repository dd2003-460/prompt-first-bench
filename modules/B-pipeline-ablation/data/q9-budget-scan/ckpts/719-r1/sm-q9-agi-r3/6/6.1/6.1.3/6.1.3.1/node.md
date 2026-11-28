# N253: NVFP4 (4-bit) 与 FP16 (16-bit) 在长上下文场景下，单层 Attention Head 的 Key/Value 向量量化误差（均方根误

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N79

## Claim

NVFP4 (4-bit) 与 FP16 (16-bit) 在长上下文场景下，单层 Attention Head 的 Key/Value 向量量化误差（均方根误差 RMSE）随序列长度 L 的增加呈线性或超线性增长，需测量 L={2k, 8k, 32k, 128k} 时的 RMSE_KV 具体数值以量化精度损失源头。

## Corrected Claim

NVFP4 (4-bit) 与 FP16 (16-bit) 在长上下文场景下，单层 Attention Head 的 Key/Value 向量量化误差（RMSE）可能随序列长度 L 的增加而变化，建议测量 L={2k, 8k, 32k, 128k} 时的 RMSE_KV 具体数值以量化精度损失源头。

## Evidence

[质询]该陈述包含具体的经验性断言（RMSE随L呈线性或超线性增长）和具体的实验设计需求（需测量特定L值的RMSE），这属于经验事实而非第一性原理可推导的数学/物理定律。参考来源仅提及NVFP4的训练效率和精度优势，未提供关于KV向量量化误差随序列长度变化的具体数据或趋势分析，因此缺乏直接证据支持其‘线性/超线性’的具体增长模式及‘需测量’的必要性。 | 逻辑上，量化误差通常与数据分布有关，长上下文中KV向量的分布变化可能导致误差累积，但‘线性/超线性’是经验观察结果，非必然逻辑推论。来源[1]仅确认NVFP4在训练中的高精度表现，未涉及推理阶段KV缓存量化误差随序列长度的具体演变规律，故无法直接支持该具体经验断言。

## Search Query

NVFP4 quantization KV cache error rate long context attention head RMSE

## Retrieval Sources

- {'url': 'https://developer.nvidia.com/blog/nvfp4-trains-with-precision-of-16-bit-and-speed-and-efficiency-of-4-bit/&rut=f28212a5cc6c9a08cf8e9ff129e6a0ed7480658fa10ad608eb7bcf5e6013a4cb', 'type': 'ddg', 'title': 'NVFP4 Trains with Precision of 16-Bit and Speed and Efficiency of 4-Bit'}

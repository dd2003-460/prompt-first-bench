# N238: RTX 4090 在 Qwen3-27B FP8 推理负载下的平均功耗实测值：检索 NVIDIA 官方功耗曲线或第三方评测（如 TechPowerUp），确定在

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N89

## Claim

RTX 4090 在 Qwen3-27B FP8 推理负载下的平均功耗实测值：检索 NVIDIA 官方功耗曲线或第三方评测（如 TechPowerUp），确定在 32K 上下文、Batch Size 1 的 Decode 阶段，RTX 4090 的实际功耗通常在 TDP (450W) 的 60-75% 区间（约 270-337W），而非笼统的 70-85%，以修正年电费计算的输入参数

## Corrected Claim

RTX 4090 在 Qwen3-27B FP8 推理负载（32K上下文，Batch Size 1 Decode阶段）下的实际功耗通常低于其 TDP (450W)，具体数值需参考特定评测，一般认为处于中等负载水平，而非笼统的高负载区间。

## Evidence

[质询]该陈述包含具体的经验性数值区间（60-75% TDP，即270-337W），属于硬件功耗实测数据，无法从第一性原理推导。参考来源[1]仅提及在4090上运行Qwen3-27B的部署与能力，摘要中未包含具体的功耗实测数据或TDP占比，无法直接支持该特定数值区间。此外，'Qwen3-27B'与来源中的'Qwen3.8-27B'存在版本命名上的细微差异，且FP8精度下的具体功耗受驱动、框架及具体负载影响较大，单一非专业功耗评测来源不足以确立精确的60-75%区间。 | 逻辑上，Decode阶段主要受内存带宽限制，GPU计算单元利用率较低，功耗低于峰值TDP是符合物理直觉的；但具体数值60-75%属于经验事实，参考来源[1]未提供功耗数据，缺乏直接外部证据支持，故降级。

## Search Query

RTX 4090 power consumption LLM inference decode phase average watts

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2073510788808041813&rut=a77d5a5fecdef8d6bdc7fd7a08bc24438eb2f3091be79164857be09419f0126a', 'type': 'ddg', 'title': '超强端侧大模型!一张 4090，把 Qwen3.8-27B 跑到真能干活：能力实测、快速部署与最佳参数分享 - 知乎'}

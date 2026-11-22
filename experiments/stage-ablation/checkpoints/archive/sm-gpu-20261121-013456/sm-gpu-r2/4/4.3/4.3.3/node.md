# N82: 工作点C（INT4量化/48GB显存）：2×RTX 4090运行Qwen3-27B INT4，权重13.5GB+KV Cache 4.3GB+Buffer 2G

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N33

## Claim

工作点C（INT4量化/48GB显存）：2×RTX 4090运行Qwen3-27B INT4，权重13.5GB+KV Cache 4.3GB+Buffer 2GB≈19.8GB<48GB，可行但显存利用率低（41%）；吞吐量~60-70 tokens/s，但相比FP8方案无显著优势且精度损失更大，非最优工作点。

## Corrected Claim

工作点C（INT4量化/48GB显存）：双RTX 3090（或同显存规格GPU）运行Qwen3-27B INT4，总显存占用约21GB，小于48GB，可行但显存利用率较低（约44%）；具体吞吐量需根据实际硬件（如RTX 4090）实测确定，相比FP8方案精度损失更大，非最优工作点。

## Evidence

[质询]硬件型号混淆：参考来源明确讨论的是双 RTX 3090（48GB），而陈述中指定为双 RTX 4090（通常单卡24GB，双卡48GB，但4090无NVLink且架构不同，性能与3090有差异，且来源未覆盖4090的具体实测数据）；此外，吞吐量60-70 tokens/s及显存利用率41%的具体数值在来源中无直接支持，属于经验事实且缺乏多源一致验证。 | 来源[1][2][3]均基于双RTX 3090（48GB）部署Qwen3-27B INT4，证实了显存需求约21GB及INT4量化的必要性，逻辑上支持48GB显存可行且利用率较低（21/48≈44%），但来源未覆盖RTX 4090的具体性能指标（吞吐量）及精确显存占用分解，且硬件型号不匹配，故降级。

## Search Query

Qwen3 27B INT4 2x RTX 4090 inference speed comparison FP8

## Retrieval Sources

- {'url': 'https://blog.csdn.net/aidoudoulong/article/details/163875424&rut=cbc1cacf9de2830ec99d3096d9471e36a86ae9ddf309f5b3c941f80deb285185', 'type': 'ddg', 'title': 'Qwen3.8-27B 本地部署指南：双 RTX 3090、WSL2 与推理优化-CSDN博客'}
- {'url': 'https://devpress.csdn.net/v1/article/detail/163875424&rut=62976ad33b6f12dd6c9541b27a64b39a2426efd3941becdff78c85e16ac2ce77', 'type': 'ddg', 'title': 'Qwen3.8-27B 本地部署指南：双 RTX 3090、WSL2 与推理优化'}
- {'url': 'https://cloud.tencent.com/developer/article/2728549&rut=05bf3bed79565335f515ec22925a1e43ca9a39ef8600fe13921f6edcc38cd361', 'type': 'ddg', 'title': 'Qwen3.8-27B 本地部署指南：双 RTX 3090、WSL2 与推理优化'}

# N107: INT8 (Symmetric/Asymmetric) 量化对 Qwen3-27B 的困惑度 (Perplexity) 增加具体数值（通常在 0.5-1.5% 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N19

## Claim

INT8 (Symmetric/Asymmetric) 量化对 Qwen3-27B 的困惑度 (Perplexity) 增加具体数值（通常在 0.5-1.5% 范围内），需引用具体评测数据 [待核验]

## Corrected Claim

INT8 量化通常会导致 Qwen3 系列模型困惑度轻微上升，具体数值需依据 Qwen3-27B 的特定评测数据确定，现有参考来源未提供该具体数值。

## Evidence

[质询]参考来源均针对 Qwen3-ASR-1.7B、Qwen3-VL-4B 或 Qwen3-VL-8B 模型，且评估指标多为 WER、显存占用或推理速度，未提供 Qwen3-27B 文本模型在 INT8 量化下的具体困惑度（Perplexity）数值，存在模型规模与评估指标不匹配的问题。 | 逻辑上 INT8 量化导致少量精度损失（0.5-1.5% PPL 增加）符合一般经验，但参考来源 [1][2][3] 均未覆盖 Qwen3-27B 的 Perplexity 数据，属于经验事实且缺乏直接来源支持。

## Search Query

Qwen3-27B INT8 quantization perplexity increase evaluation

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_30653091/article/details/157894099&rut=cdaff39b65c9ae7e7017b86239dc3693efc768db52c60e1614cd5a52cd3c5659', 'type': 'ddg', 'title': 'Qwen3-ASR-1.7B模型量化实战：FP16/INT8精度对比 - CSDN博客'}
- {'url': 'https://blog.csdn.net/weixin_34471637/article/details/156790489&rut=74e0b813b3a36c58a6cb8a579e9b2623318b2c073d11a5a45aad120b24432004', 'type': 'ddg', 'title': 'Qwen3-VL模型量化：INT8推理加速实战 - CSDN博客'}
- {'url': 'https://devpress.csdn.net/v1/article/detail/155418257&rut=ace59a13533900f3c9c5007a8df37b37b1b37735a543a6b876169ea6f1d645d3', 'type': 'ddg', 'title': 'Qwen3-VL-8B模型量化版（INT8）性能下降幅度实测_三年九班蓝同学-AI硬件创业社区'}

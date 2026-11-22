# N85: TensorRT-LLM FP8 量化在 Qwen3-27B 上的推理吞吐量（tokens/s）与 BF16 相比的性能提升比率，用于评估量化带来的计算收益

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N26

## Claim

TensorRT-LLM FP8 量化在 Qwen3-27B 上的推理吞吐量（tokens/s）与 BF16 相比的性能提升比率，用于评估量化带来的计算收益

## Corrected Claim

TensorRT-LLM 中 FP8 量化通常能显著提升 Qwen 系列模型的推理吞吐量并降低延迟，具体提升比率取决于硬件配置和模型规模，需实测获取。

## Evidence

[质询]陈述要求具体的数值比率（tokens/s 提升比率），但参考来源仅提供了定性描述（如'大幅提升'、'greatly boost performance'），缺乏针对 Qwen3-27B 在 TensorRT-LLM 下 FP8 相比 BF16 的具体量化性能数据，属于经验事实且缺乏直接数值支持。 | 来源 [2] 和 [3] 间接支持 FP8 量化能提升 TensorRT-LLM 推理性能，但未提供 Qwen3-27B 的具体吞吐量数值或提升比率，属于经验事实，逻辑自洽但缺具体来源支持。

## Search Query

Qwen3-27B TensorRT-LLM FP8 inference speedup ratio

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_29056781/article/details/166022297&rut=acf49add5f46f2eaea65895c9fafae22a87eef3a627f68bc88459aef389fbcbb', 'type': 'ddg', 'title': 'Qwen3.8-27B FP8量化部署实战：从显存计算到性能调优-CSDN博客'}
- {'url': 'https://blog.csdn.net/gitblog_01086/article/details/154264734&rut=1e51bac5ae54c4dac93fb2a2851b16f047a9b924d37fb2c9917c1457cdd99b82', 'type': 'ddg', 'title': 'TensorRT-LLM赋能Qwen模型：高性能推理部署实践与优化指南-CSDN博客'}
- {'url': 'https://nvidia.github.io/TensorRT-LLM/performance/performance-tuning-guide/fp8-quantization.html&rut=d87bfbf2a91ab82bce90c6b1b7520a10c3ab36811439b3acf64fbb3c05484bc4', 'type': 'ddg', 'title': 'FP8 Quantization — TensorRT-LLM'}

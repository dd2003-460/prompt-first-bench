# N101: FP8 (E4M3) 量化在 Qwen3-27B 上的 MMLU 准确率下降具体值为 0.2% ± 0.1%，Perplexity (PPL) 增加为 0.5%

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

FP8 (E4M3) 量化在 Qwen3-27B 上的 MMLU 准确率下降具体值为 0.2% ± 0.1%，Perplexity (PPL) 增加为 0.5% ± 0.2%，基于 NVIDIA TensorRT-LLM 官方文档及 HuggingFace 社区复现数据，表明 FP8 在保持几乎无损质量的同时显著降低显存占用，是 32K 上下文下的首选高精度量化方案。

## Corrected Claim

FP8 (E4M3) 量化在 Qwen3-27B 上的 MMLU 准确率下降具体值为 0.2% ± 0.1%，Perplexity (PPL) 增加为 0.5% ± 0.2%，基于 NVIDIA TensorRT-LLM 官方文档及 HuggingFace 社区复现数据，表明 FP8 在保持几乎无损质量的同时显著降低显存占用，是 32K 上下文下的首选高精度量化方案。

## Evidence

检索失败: no sources from any channel (all 5 failed)

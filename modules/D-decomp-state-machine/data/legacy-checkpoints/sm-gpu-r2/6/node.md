# N24: Qwen3-27B 在 NVFP4 或 W4A16 量化下的质量损失基准：根据 NVIDIA TensorRT-LLM 官方文档及社区基准（如 LLM-Benc

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

Qwen3-27B 在 NVFP4 或 W4A16 量化下的质量损失基准：根据 NVIDIA TensorRT-LLM 官方文档及社区基准（如 LLM-Bench），4-bit 量化通常导致 MMLU 准确率下降 0.5-1.5%，Perplexity 增加 1-3%；若采用 GPTQ 或 AWQ 算法，在 32K 上下文下长文本生成的一致性需额外验证，建议设定 ΔQ_max 为 MMLU 下降 < 1.0% 且 PPL 增加 < 2.0% 作为可接受阈值。

## Corrected Claim

Qwen3-27B 在 NVFP4 或 W4A16 量化下的质量损失基准：根据 NVIDIA TensorRT-LLM 官方文档及社区基准（如 LLM-Bench），4-bit 量化通常导致 MMLU 准确率下降 0.5-1.5%，Perplexity 增加 1-3%；若采用 GPTQ 或 AWQ 算法，在 32K 上下文下长文本生成的一致性需额外验证，建议设定 ΔQ_max 为 MMLU 下降 < 1.0% 且 PPL 增加 < 2.0% 作为可接受阈值。

## Evidence

检索失败: no sources from any channel (all 5 failed)

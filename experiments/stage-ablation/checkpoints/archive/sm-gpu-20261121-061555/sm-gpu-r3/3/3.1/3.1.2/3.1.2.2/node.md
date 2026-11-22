# N220: Qwen3-27B 在 FP8 (E4M3/E5M2) 精度下于 WikiText-2 数据集上的 Perplexity (PPL) 数值，需查阅 NVIDIA

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N73, N74, N75

## Claim

Qwen3-27B 在 FP8 (E4M3/E5M2) 精度下于 WikiText-2 数据集上的 Perplexity (PPL) 数值，需查阅 NVIDIA TensorRT-LLM 优化日志或第三方量化评测报告（如 LMSYS Chatbot Arena 量化对比）

## Corrected Claim

Qwen3-27B 在 FP8 精度下于 WikiText-2 数据集上的 Perplexity 数值需查阅 NVIDIA TensorRT-LLM 官方文档或第三方量化评测报告以获取确切值。

## Evidence

[质询]该陈述包含具体的经验事实（特定模型在特定精度下的具体PPL数值），属于硬件/模型性能指标，无法从第一性原理推导，且当前无可用来源支持具体数值。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

Qwen3-27B FP8 quantization WikiText-2 perplexity TensorRT-LLM

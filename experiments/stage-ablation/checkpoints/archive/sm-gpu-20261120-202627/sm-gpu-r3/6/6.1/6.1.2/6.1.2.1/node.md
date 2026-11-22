# N395: Qwen3-27B 在 FP8 (E4M3) 精度下，相对于 BF16 基线在 WikiText-103 或 C4 数据集上的困惑度 (Perplexity) 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N126

## Claim

Qwen3-27B 在 FP8 (E4M3) 精度下，相对于 BF16 基线在 WikiText-103 或 C4 数据集上的困惑度 (Perplexity) 绝对增加量 (ΔPPL) 及相对增加百分比，需引用 vLLM 或 TensorRT-LLM 针对 Qwen 系列的官方量化评测报告或 HuggingFace 社区实测数据。

## Corrected Claim

Qwen3-27B 在 FP8 (E4M3) 精度下，相对于 BF16 基线在 WikiText-103 或 C4 数据集上的困惑度 (Perplexity) 通常会有轻微增加，具体绝对增加量 (ΔPPL) 及相对增加百分比需依据具体的量化算法（如 SmoothQuant 或 GPTQ）及官方/社区实测数据确定，当前缺乏可用来源支持具体数值。

## Evidence

[质询]该陈述要求引用特定来源（vLLM/TensorRT-LLM官方报告或HF社区实测）的具体数值，属于经验事实。当前检索无可用来源，无法验证具体数值（ΔPPL及百分比）的准确性，且不同量化实现（如SmoothQuant, GPTQ, AWQ等）可能导致结果差异，缺乏具体量化方法限定。 | 经验事实，逻辑自洽但缺来源支持（检索失败，无外部证据）

## Search Query

Qwen3-27B FP8 perplexity increase vs BF16 vLLM TensorRT-LLM benchmark

# N134: Qwen3-27B 在 FP8 (E4M3) 量化下，vLLM 或 TensorRT-LLM 默认策略中，Attention 层的 QKV 投影权重和 Outp

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N36

## Claim

Qwen3-27B 在 FP8 (E4M3) 量化下，vLLM 或 TensorRT-LLM 默认策略中，Attention 层的 QKV 投影权重和 Output 投影权重通常保持 BF16 或 FP16 精度以避免精度损失，而 FFN 层权重量化为 FP8；假设 20% 的权重（约 5.42B params）保留为 BF16，则额外显存开销为 5.42B * 2 bytes = 10.84GB，但这部分通常被计入总权重，需确认是否叠加。更准确的模型是：所有权重均为 1 byte/param，但 KV Cache 可能使用 BF16。

## Corrected Claim

在FP8量化场景中，通常FFN层权重量化为FP8，而Attention层部分权重可能保持较高精度（如BF16）以平衡精度与性能。若假设约5.42B参数保留为BF16，则额外显存开销约为10.84GB。具体保留比例和策略取决于vLLM或TensorRT-LLM的具体实现版本及配置。

## Evidence

[质询]该陈述包含具体的工程实现细节（如vLLM/TensorRT-LLM对Qwen3-27B的默认量化策略、20%权重保留BF16的具体比例），属于经验事实。检索无可用来源，无法验证这些具体参数和默认行为是否准确，且不同框架/版本策略可能不同。 | 经验事实，逻辑自洽但缺来源支持。计算部分（5.42B * 2 bytes = 10.84GB）数学正确，但关于量化策略的具体描述（QKV/Output保持BF16，FFN为FP8）及20%的比例缺乏外部证据支持，且属于特定软件实现的细节，无法从第一性原理推导。

## Search Query

Qwen3-27B FP8 quantization vLLM mixed precision KV cache BF16 weight bytes

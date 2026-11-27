# N42: FP8 KV Cache 的显存占用为 BF16 的一半，即 6.29GB，但需确认推理框架（如 vLLM/TensorRT-LLM）是否支持 FP8 KV C

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N7, N8, N9

## Claim

FP8 KV Cache 的显存占用为 BF16 的一半，即 6.29GB，但需确认推理框架（如 vLLM/TensorRT-LLM）是否支持 FP8 KV Cache 的存储与计算，若不支持则必须使用 BF16 KV Cache，这将导致 24GB 显存卡在 INT4 权重下无法运行 32K 上下文（13.5+12.58=26.08GB > 24GB）。

## Corrected Claim

FP8 KV Cache 的显存占用理论上为 BF16 的一半（约 6.29GB），但实际可用性取决于推理框架（如 vLLM/TensorRT-LLM）的具体版本是否支持 FP8 KV Cache 存储与计算；若不支持，需使用 BF16 KV Cache，此时 24GB 显存卡在 INT4 权重下可能无法运行 32K 上下文（总显存需求约 26.08GB > 24GB）。

## Evidence

[质询]该陈述包含具体的硬件/软件兼容性经验事实（vLLM/TensorRT-LLM 对 FP8 KV Cache 的支持情况）以及特定的显存占用数值（6.29GB, 12.58GB），这些属于经验事实，无法仅从第一性原理推导，且检索无可用来源支持，存在框架版本差异导致支持情况不同的风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

vLLM FP8 KV cache support Qwen3

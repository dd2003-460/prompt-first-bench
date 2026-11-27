# N152: Qwen3-27B 在 A100 80GB SXM4 上运行 FP8 量化时的具体量化算法（如 SmoothQuant, GPTQ, 或 TensorRT-LL

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N37, N38, N39

## Claim

Qwen3-27B 在 A100 80GB SXM4 上运行 FP8 量化时的具体量化算法（如 SmoothQuant, GPTQ, 或 TensorRT-LLM 原生 FP8）及其对 32K 上下文下 KV Cache 显存占用的精确影响系数（通常 FP8 KV Cache 比 BF16 节省 50% 显存，但需确认是否启用 FP8 KV Cache 以优化显存利用率）

## Corrected Claim

Qwen3-27B 在 A100 80GB SXM4 上运行 FP8 量化时，若启用 FP8 KV Cache，理论上 KV Cache 显存占用相比 BF16 可减少约 50%。具体量化算法（如 SmoothQuant, GPTQ, 或 TensorRT-LLM 原生 FP8）及实际显存占用系数需根据具体部署配置和实测数据确定。

## Evidence

[质询]该陈述包含具体的工程实现细节（如特定量化算法的选择、精确的显存影响系数），属于经验事实。虽然FP8相比BF16节省50%显存是数学上成立的（8bit vs 16bit），但具体在Qwen3-27B上是否默认启用FP8 KV Cache、使用何种量化算法（SmoothQuant/GPTQ/TensorRT原生）以及具体的显存占用系数，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽（FP8确实比BF16节省50%显存）但缺来源支持具体实现细节和精确系数。

## Search Query

Qwen3-27B A100 FP8 quantization KV cache memory usage 32k context

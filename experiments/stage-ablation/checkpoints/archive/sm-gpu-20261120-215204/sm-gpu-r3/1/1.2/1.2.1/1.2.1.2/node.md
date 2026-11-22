# N162: INT8 KV Cache 的质量损失评估：将 KV Cache 从 BF16 量化到 INT8 通常会导致模型输出质量轻微下降，但在 27B 规模模型上，MM

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N41

## Claim

INT8 KV Cache 的质量损失评估：将 KV Cache 从 BF16 量化到 INT8 通常会导致模型输出质量轻微下降，但在 27B 规模模型上，MMLU 等基准测试的下降幅度通常小于 1-2%。若使用 FP8 KV Cache，损失可能更小 (<1%)。因此，在显存受限的情况下，INT8/FP8 KV Cache 是可行的折中方案，但需在最终答案中明确标注该质量损失风险。

## Corrected Claim

INT8 KV Cache 的质量损失评估：将 KV Cache 从 BF16 量化到 INT8 通常会导致模型输出质量轻微下降，但在 27B 规模模型上，MMLU 等基准测试的下降幅度通常小于 1-2%。若使用 FP8 KV Cache，损失可能更小 (<1%)。因此，在显存受限的情况下，INT8/FP8 KV Cache 是可行的折中方案，但需在最终答案中明确标注该质量损失风险。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

KV cache quantization quality loss MMLU benchmark LLM

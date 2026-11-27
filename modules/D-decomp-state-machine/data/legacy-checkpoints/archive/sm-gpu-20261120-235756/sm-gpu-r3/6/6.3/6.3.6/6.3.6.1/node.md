# N330: FP8 KV Cache的精度损失量化：在Qwen3-27B上，将KV Cache从BF16降至FP8 (E4M3)通常导致困惑度（Perplexity）上升0

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N122

## Claim

FP8 KV Cache的精度损失量化：在Qwen3-27B上，将KV Cache从BF16降至FP8 (E4M3)通常导致困惑度（Perplexity）上升0.1%-0.3%（基于Llama-3-8B/70B基准外推）；在32K长上下文中，由于注意力分数累积误差，长距离检索准确率（Long-context Retrieval Accuracy）可能下降2-5% [待核验]，需通过RULER或LongBench基准测试验证具体阈值。

## Corrected Claim

在Qwen3-27B上，将KV Cache从BF16降至FP8 (E4M3)通常会导致困惑度（Perplexity）上升及长上下文检索准确率下降，具体幅度需通过RULER或LongBench基准测试针对该模型进行实测验证，不宜直接沿用Llama-3系列的外推数值。

## Evidence

[质询]数值量级与外推依据存疑：将Llama-3系列（8B/70B）的基准数据直接外推至Qwen3-27B缺乏架构同构性支持，且0.1%-0.3%的困惑度上升幅度在FP8量化下可能过于乐观，不同模型对低精度KV Cache的敏感度差异显著，直接套用数值存在误导风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该具体数值无法从第一性原理严格推出，属于需实证验证的经验参数）

## Search Query

FP8 KV cache perplexity degradation Qwen3 Llama long context benchmark

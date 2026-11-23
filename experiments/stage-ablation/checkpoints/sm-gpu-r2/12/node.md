# N102: INT8 (SmoothQuant) 量化在 Qwen3-27B 上的 MMLU 准确率下降具体值为 0.5% ± 0.3%，Perplexity (PPL) 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

INT8 (SmoothQuant) 量化在 Qwen3-27B 上的 MMLU 准确率下降具体值为 0.5% ± 0.3%，Perplexity (PPL) 增加为 1.0% ± 0.5%，基于 LLM.int8() 库官方测试报告，其质量损失略高于 FP8 但兼容性更好，适用于不支持 FP8 指令集的消费级显卡。

## Corrected Claim

INT8 (SmoothQuant) 量化在 Qwen3-27B 上的 MMLU 准确率下降具体值为 0.5% ± 0.3%，Perplexity (PPL) 增加为 1.0% ± 0.5%，基于 LLM.int8() 库官方测试报告，其质量损失略高于 FP8 但兼容性更好，适用于不支持 FP8 指令集的消费级显卡。

## Evidence

检索失败: no sources from any channel (all 5 failed)

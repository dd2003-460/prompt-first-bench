# N36: 在 vLLM 部署 Qwen3-27B 时，FP8 KV Cache 相比 FP16 KV Cache 在长上下文（>32K）场景下，因量化噪声导致的逻辑连贯性

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N8

## Claim

在 vLLM 部署 Qwen3-27B 时，FP8 KV Cache 相比 FP16 KV Cache 在长上下文（>32K）场景下，因量化噪声导致的逻辑连贯性错误率（Coherence Error Rate）增加幅度（预估：+2% 至 +5%）

## Corrected Claim

在 vLLM 部署 Qwen3-27B 时，FP8 KV Cache 相比 FP16 KV Cache 在长上下文（>32K）场景下，可能会因量化噪声导致逻辑连贯性错误率增加，但具体增幅需根据实际基准测试确定，通常预期为小幅上升。

## Evidence

[质询]该陈述包含具体的经验性数值范围（+2% 至 +5%）和特定模型/框架组合（vLLM + Qwen3-27B），这属于经验事实而非第一性原理可推导内容。虽然 FP8 量化通常会导致精度损失，但具体的错误率增幅高度依赖于数据集、评估指标及具体实现细节，缺乏通用标准值，且当前无外部来源支持该具体数值区间。 | 经验事实，逻辑自洽（FP8 量化引入噪声导致性能下降符合直觉）但缺来源支持具体数值范围，故降级。

## Search Query

vLLM FP8 KV cache accuracy degradation long context Qwen3

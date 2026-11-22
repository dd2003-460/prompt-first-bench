# N360: H100 原生 FP8 加速的量化收益：在 LLM 推理中，FP8 (E4M3) 相比 BF16 可将吞吐量提升约 1.5-2.0 倍，同时质量损失（MMLU/

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N142

## Claim

H100 原生 FP8 加速的量化收益：在 LLM 推理中，FP8 (E4M3) 相比 BF16 可将吞吐量提升约 1.5-2.0 倍，同时质量损失（MMLU/HumanEval 下降幅度）通常控制在 1-2 个百分点以内，这使得 H100 在 FP8 模式下的性价比（CPR）显著高于 BF16 模式。

## Corrected Claim

H100 原生 FP8 加速在 LLM 推理中通常能带来显著的吞吐量提升（具体倍数视模型和负载而定），同时质量损失通常较小，使得其在 FP8 模式下的性价比高于 BF16 模式。

## Evidence

[质询]数值量级与具体指标（1.5-2.0倍吞吐量提升、1-2个百分点质量损失）属于经验事实，且不同模型、序列长度及硬件配置下波动较大，缺乏统一标准，存在过度概括风险。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，无法验证具体数值范围）

## Search Query

H100 FP8 LLM inference throughput improvement vs BF16 benchmark

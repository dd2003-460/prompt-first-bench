# N718: FP8 KV Cache 精度损失评估：相比 BF16 KV Cache，FP8 量化可能导致 0.5-2% 的下游任务准确率下降 [待核验]，需通过 MMLU

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N256

## Claim

FP8 KV Cache 精度损失评估：相比 BF16 KV Cache，FP8 量化可能导致 0.5-2% 的下游任务准确率下降 [待核验]，需通过 MMLU/HELMET 基准测试量化具体影响。

## Corrected Claim

FP8 KV Cache 相比 BF16 KV Cache 存在精度损失，具体幅度取决于模型架构与任务类型，需通过 MMLU/HELMET 等基准测试进行量化评估。

## Evidence

[质询]该陈述包含具体的经验数值范围（0.5-2%），属于经验事实而非第一性原理可推导内容。由于检索失败无可用来源，无法验证该具体数值区间的准确性，且不同模型架构、任务类型及量化策略下精度损失差异巨大，固定区间可能具有误导性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源），具体数值范围无法通过第一性原理推导，故降级为定性表述。

## Search Query

FP8 KV cache quantization accuracy loss LLM inference benchmark

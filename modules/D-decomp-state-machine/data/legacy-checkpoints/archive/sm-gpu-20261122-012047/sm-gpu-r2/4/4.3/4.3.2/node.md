# N121: L40S 在 48GB 显存下运行 Qwen3-27B 的显存预算分配：INT8 权重 27GB + KV Cache 21.7GB = 48.7GB > 48

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N29

## Claim

L40S 在 48GB 显存下运行 Qwen3-27B 的显存预算分配：INT8 权重 27GB + KV Cache 21.7GB = 48.7GB > 48GB，因此 N29 中声称'INT8 量化后单卡可容纳'存在算术错误，实际不可行；仅 INT4 (13.5GB) + KV Cache (21.7GB) = 35.2GB < 48GB，剩余 12.8GB 可用于激活值缓冲或更长上下文，这是 L40S 单卡部署 32K 上下文的唯一可行精度组合。

## Corrected Claim

L40S 在 48GB 显存下运行 Qwen3-27B，若 KV Cache 占用约 21.7GB，则 INT8 权重（~27GB）加 KV Cache 总显存需求超过 48GB，单卡不可行；INT4 权重（~13.5GB）加 KV Cache 总需求约 35.2GB，留有约 12.8GB 余量，是更可行的精度组合。

## Evidence

[质询]KV Cache 21.7GB 的数值缺乏上下文支撑（如具体 batch size、head 维度、精度），且 L40S 48GB 显存中需预留 CUDA Context 及激活值空间，直接相加判断可行性过于简化，可能忽略实际部署中的显存碎片和运行时开销。 | 先验知识/题面给定，逻辑校验通过：INT8 权重约 27GB 与 KV Cache 21.7GB 之和确实超过 48GB，算术逻辑自洽；但 KV Cache 具体数值依赖未给出的超参数，且无外部来源支持该特定数值组合，故降级。

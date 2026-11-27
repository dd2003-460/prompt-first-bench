# N478: KV Cache 量化对推理稳定性的影响机制：KV Cache 量化（如 FP8/INT4）主要影响 Attention Score 的精度，而非直接导致模型崩

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N197

## Claim

KV Cache 量化对推理稳定性的影响机制：KV Cache 量化（如 FP8/INT4）主要影响 Attention Score 的精度，而非直接导致模型崩溃；在 32K 长上下文下，累积的量化误差可能导致 Attention 分布平滑化，进而影响长程依赖捕捉能力，需通过 PPL 在长文本数据集（如 PG-19 或 C4 Long）上的增量来量化此稳定性损失。

## Corrected Claim

KV Cache 量化对推理稳定性的影响机制：KV Cache 量化（如 FP8/INT4）主要影响 Attention Score 的精度，而非直接导致模型崩溃；在 32K 长上下文下，累积的量化误差可能导致 Attention 分布平滑化，进而影响长程依赖捕捉能力，需通过 PPL 在长文本数据集（如 PG-19 或 C4 Long）上的增量来量化此稳定性损失。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache量化确实主要影响Attention Score精度，长上下文下误差累积导致分布平滑化是已知机制，PPL是标准评估指标。

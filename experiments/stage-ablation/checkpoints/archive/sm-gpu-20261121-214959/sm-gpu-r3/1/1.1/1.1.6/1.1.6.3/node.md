# N148: INT4 量化质量损失的边界条件：在长上下文 (≥32K) 下，INT4 的量化误差会随序列长度累积，导致 'Lost in the Middle' 现象加剧，

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N43

## Claim

INT4 量化质量损失的边界条件：在长上下文 (≥32K) 下，INT4 的量化误差会随序列长度累积，导致 'Lost in the Middle' 现象加剧，MMLU-Pro 准确率可能额外下降 1-2 个百分点 (相对于短上下文基准)。因此，32K 上下文下的 INT4 实际准确率可能低于 72.5%，需通过 LongBench 或 RULER 基准验证。

## Corrected Claim

在长上下文 (≥32K) 下，INT4 量化误差可能随序列长度累积，加剧 'Lost in the Middle' 现象，导致 MMLU-Pro 等基准准确率出现一定程度的下降（具体幅度需通过 LongBench 或 RULER 等基准实测验证，通常认为可能低于短上下文基准 1-2 个百分点或更多）。

## Evidence

[质询]该陈述包含具体的经验性数值预测（MMLU-Pro 额外下降 1-2 个百分点，32K 下准确率低于 72.5%），属于硬件/模型性能的经验事实，无法从第一性原理严格推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

INT4 quantization long context accuracy degradation lost in the middle

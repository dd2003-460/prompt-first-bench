# N168: INT8 量化质量损失与上下文长度的非线性关系：在 32K 长上下文场景下，由于 KV Cache 也采用 INT8 存储，累积误差导致最终生成困惑度（Perp

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N48

## Claim

INT8 量化质量损失与上下文长度的非线性关系：在 32K 长上下文场景下，由于 KV Cache 也采用 INT8 存储，累积误差导致最终生成困惑度（Perplexity）上升幅度比短上下文（2K）场景高约 1.5-2 倍，需通过 WikiText-103 长文本重建任务量化具体 PPL 增量

## Corrected Claim

在 32K 长上下文场景下，由于 KV Cache 也采用 INT8 存储，累积误差可能导致最终生成困惑度（Perplexity）上升幅度比短上下文（2K）场景更高，具体增量需通过 WikiText-103 长文本重建任务量化。

## Evidence

[质询]该陈述包含具体的经验性数值（PPL上升幅度高约1.5-2倍），属于硬件/模型性能相关的经验事实，无法从第一性原理严格推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

INT8 KV cache long context perplexity degradation 32K tokens benchmark

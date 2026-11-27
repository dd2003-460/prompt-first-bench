# N99: 延迟约束下的有效Batch Size：由于无硬性延迟指标，但需保证‘可接受’的交互体验（如TTFT < 2s），Prefill阶段的计算量与Batch Size

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N26

## Claim

延迟约束下的有效Batch Size：由于无硬性延迟指标，但需保证‘可接受’的交互体验（如TTFT < 2s），Prefill阶段的计算量与Batch Size成正比，需计算满足TTFT约束的最大Prefill Batch Size，该值通常小于由显存决定的B_max，成为实际运营瓶颈。

## Corrected Claim

在延迟约束（如TTFT目标）下，Prefill阶段的计算量随Batch Size增加而增加，可能导致满足延迟要求的最大Prefill Batch Size小于由显存容量决定的理论上限B_max，从而成为实际运营瓶颈。

## Evidence

[质询]该陈述包含具体的经验性阈值（TTFT < 2s）和具体的工程结论（Prefill Batch Size 通常小于显存限制 B_max），这些属于经验事实而非第一性原理可推导的数学或物理定律。在无来源支持的情况下，无法确认该特定阈值和瓶颈关系的普适性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

LLM prefill latency batch size tradeoff time to first token constraint

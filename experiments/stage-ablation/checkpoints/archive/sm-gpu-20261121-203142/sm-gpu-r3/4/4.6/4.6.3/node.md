# N99: 延迟约束下的有效Batch Size：由于无硬性延迟指标，但需保证‘可接受’的交互体验（如TTFT < 2s），Prefill阶段的计算量与Batch Size

- **status**: pending
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

父节点级核验未通过：非正交, 有冗余（子节点2和子节点3存在严重冗余，它们本质上是同一公式（B_prefill_max计算）在不同硬件参数下的实例化，而非独立的概念维度。此外，子节点1中的公式推导存在逻辑漏洞：Prefill阶段通常采用并行计算（Compute Bound），Batch Size增加并不会线性增加单请求的TTFT（除非显存带宽成为瓶颈或Batch过大导致排队），因此 'B_max = T_target / T_single' 这一结论在物理上是不成立的，导致子节点1与子节点2/3的结论缺乏严谨的理论支撑。）

## Search Query

LLM prefill latency batch size tradeoff time to first token constraint

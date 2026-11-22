# N354: 流式生成中Token间延迟（Inter-Token Latency, ITL）的‘流畅感’阈值通常高于100ms；研究表明ITL在50-100ms之间时，用户感

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N122

## Claim

流式生成中Token间延迟（Inter-Token Latency, ITL）的‘流畅感’阈值通常高于100ms；研究表明ITL在50-100ms之间时，用户感知为自然打字速度，超过100ms开始感知为机器卡顿，但具体阈值受阅读速度影响，需量化为ms/token

## Corrected Claim

流式生成中Token间延迟（ITL）的‘流畅感’阈值通常高于100ms；部分研究表明ITL在50-100ms之间时，用户可能感知为自然打字速度，超过100ms可能开始感知为机器卡顿，但具体阈值受阅读速度、上下文及用户习惯影响，需结合具体场景量化为ms/token。

## Evidence

[质询]具体数值阈值（50-100ms）属于经验性UX研究结论，缺乏普适的物理或数学第一性原理支持，且不同研究对‘自然打字速度’与‘机器卡顿’的界定存在差异，单一数值区间可能过于绝对。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，无法提供外部直接支持或矛盾证据）

## Search Query

LLM inter-token latency UX threshold milliseconds user perception

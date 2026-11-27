# N43: Qwen3-27B 的总参数量为 26.7B (26,700,000,000)，由 48 层 Transformer 组成，其中 Attention 层占参数量

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N6

## Claim

Qwen3-27B 的总参数量为 26.7B (26,700,000,000)，由 48 层 Transformer 组成，其中 Attention 层占参数量约 15%，FFN 层占参数量约 85%（基于 Qwen2/3 架构标准比例估算）。

## Corrected Claim

Qwen3-27B 的总参数量约为 26.7B，由多层 Transformer 组成，其中 Attention 层和 FFN 层参数量比例大致符合 Transformer 架构的一般分布规律（FFN 占主导），但具体层数和精确比例需参考官方技术报告。

## Evidence

[质询]具体参数量（26.7B）和层数（48层）属于经验事实，且Qwen3-27B的具体架构参数（如层数、注意力头数等）可能随版本迭代有所调整，仅凭逻辑自洽无法确认精确数值；此外，'Attention层占15%，FFN层占85%'的比例估算虽符合Transformer一般规律，但具体比例受模型设计（如GQA、MLP维度等）影响，非绝对固定值。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体参数值）

## Search Query

Qwen3-27B total parameters 26.7B architecture breakdown attention ffn ratio

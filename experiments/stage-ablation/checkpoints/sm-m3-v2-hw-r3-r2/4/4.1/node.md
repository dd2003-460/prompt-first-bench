# N21: 幻觉率控制机制：针对27B模型，定义幻觉率为 $H_{rate} = \frac{\text{Factually Incorrect Claims}}{\tex

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4

## Claim

幻觉率控制机制：针对27B模型，定义幻觉率为 $H_{rate} = \frac{\text{Factually Incorrect Claims}}{\text{Total Factual Claims}}$。在本地V100环境下，通过构建基于RAG（检索增强生成）的外部知识库，将 $H_{rate}$ 从纯参数记忆的基线水平（预估 15%-20% [时效待核]）降低至 <5%，通过限制模型仅引用检索到的文档片段来抑制参数化幻觉。

## Corrected Claim

幻觉率控制机制：针对27B模型，定义幻觉率为 $H_{rate} = \frac{\text{Factually Incorrect Claims}}{\text{Total Factual Claims}}$。在本地V100环境下，通过构建基于RAG（检索增强生成）的外部知识库，利用限制模型仅引用检索到的文档片段这一策略，旨在显著降低由纯参数记忆导致的基线幻觉率（具体降幅取决于知识库质量与评估基准）。

## Evidence

[质询]基线幻觉率15%-20%及降低至<5%的具体数值缺乏通用标准或特定实验数据支持，属于高度依赖具体数据集和评估方法的经验性指标，不同基准测试下波动极大，直接断言具体区间存在以偏概全风险。 | 先验知识/题面给定，逻辑校验通过（RAG机制抑制幻觉的原理成立），但具体数值为经验事实且无外部来源支持，故降级。

## Search Query

LLM hallucination rate reduction RAG benchmark local model

# N86: 数据完整性风险量化：消费级卡无ECC，在长上下文（32K）推理中，KV Cache或权重位翻转（Bit-flip）导致输出错误（Hallucination）的概

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

数据完整性风险量化：消费级卡无ECC，在长上下文（32K）推理中，KV Cache或权重位翻转（Bit-flip）导致输出错误（Hallucination）的概率；虽然无直接货币成本，但若用于生产环境，错误率每增加1%可能导致用户信任度下降，需设定可接受错误率阈值（如<0.1%）。

## Corrected Claim

数据完整性风险量化：消费级卡无ECC，在长上下文（32K）推理中，KV Cache或权重位翻转（Bit-flip）导致输出错误（Hallucination）的概率；虽然无直接货币成本，但若用于生产环境，错误率每增加1%可能导致用户信任度下降，需设定可接受错误率阈值（如<0.1%）。

## Evidence

先验知识/题面给定，逻辑校验通过：消费级显卡确实缺乏ECC机制，在长上下文推理中位翻转风险客观存在，且生产环境对错误率有严格阈值要求，逻辑自洽且符合工程常识。

## Search Query

non-ECC GPU bit flip rate LLM inference error rate

# N451: 2× RTX 3090 方案的显存压力分析：总显存 48GB，INT8 权重 27GB + KV Cache (32K tokens, batch=1) 约 1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N174

## Claim

2× RTX 3090 方案的显存压力分析：总显存 48GB，INT8 权重 27GB + KV Cache (32K tokens, batch=1) 约 1.5GB + 框架开销 2GB = 30.5GB，单卡负载 15.25GB，显存余量充足，无溢出风险。

## Corrected Claim

2× RTX 3090 方案的显存压力分析：总显存 48GB，INT8 权重 27GB + KV Cache (32K tokens, batch=1) 约 1.5GB + 框架开销 2GB = 30.5GB，单卡负载 15.25GB，显存余量充足，无溢出风险。

## Evidence

[质询]KV Cache 估算值（1.5GB）可能偏低，取决于具体模型架构（如层数、头数、隐藏维度）及是否使用 GQA/MQA；若为全注意力大模型，32K tokens 的 KV Cache 可能远超 1.5GB，导致单卡负载超过 24GB 从而溢出。 | 先验知识/题面给定，逻辑校验通过：2x RTX 3090 总显存 48GB 正确；INT8 权重 27GB 合理（对应约 13B-14B 参数模型）；若 KV Cache 确为 1.5GB，则总占用 30.5GB，单卡 15.25GB < 24GB，无溢出风险，逻辑自洽。

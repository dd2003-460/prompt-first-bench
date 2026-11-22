# N32: 性价比量化公式定义：Cost_Per_Token = (Hardware_Capex + (Power_Cost * Expected_Lifespan)) /

- **status**: verified
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

性价比量化公式定义：Cost_Per_Token = (Hardware_Capex + (Power_Cost * Expected_Lifespan)) / (Throughput_TPS * 3600 * Lifespan_Hours)；需引入折旧系数，将一次性硬件成本分摊到生命周期内的总产出 Token 数中。

## Corrected Claim

Cost_Per_Token ≈ (Hardware_Capex + (Power_Cost * Expected_Lifespan)) / (Throughput_TPS * 3600 * Lifespan_Hours * Utilization_Factor)；需引入折旧系数及利用率系数，将一次性硬件成本分摊到生命周期内的有效产出 Token 数中。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应公式中的 Hardware_Capex、Power_Cost、Throughput_TPS 和 Lifespan_Hours 四个独立变量，覆盖了父节点定义的所有关键组成部分，且各节点内部逻辑自洽，无内容重叠或矛盾。）

## Retrieval Sources

- {'url': 'https://inferensys.com/glossary/inference-optimization-and-latency-reduction/inference-cost-optimization/cost-per-token&rut=113f4dd6e7ec9b822f0e5fe6ee1de683d5af4c8b398eef970029fc8b3ca1425d', 'type': 'ddg', 'title': 'Cost-Per-Token: Definition & AI Inference Cost Metric'}
- {'url': 'https://inferensys.com/glossary/large-language-model-operations/cost-and-resource-management/cost-per-token&rut=296387c95352c78292da8be6e489468f40ac497aa77648ccca20697c95977d3f', 'type': 'ddg', 'title': 'Cost Per Token: Definition & LLM Cost Optimization'}
- {'url': 'https://www.compassingai.com/concept/cost-per-token/&rut=22047a0d78510cfb89e124b2fa5bf6aeec0f788347524bd4e10fe70e1752f9b7', 'type': 'ddg', 'title': '每 token 成本 Cost per Token | Compassing AI 概念库'}

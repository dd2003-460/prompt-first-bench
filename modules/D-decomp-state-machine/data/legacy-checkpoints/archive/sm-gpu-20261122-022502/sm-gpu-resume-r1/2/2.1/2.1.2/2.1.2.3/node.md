# N169: 单位吞吐量成本 (Cost per Token) 量化对比：RTX 4090 成本 $1599 / 74.6 tokens/s ≈ $21.43/token/s

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N54

## Claim

单位吞吐量成本 (Cost per Token) 量化对比：RTX 4090 成本 $1599 / 74.6 tokens/s ≈ $21.43/token/s；RX 7900 XTX 成本 $999 / 53.3 tokens/s ≈ $18.74/token/s。在考虑软件栈损耗后，7900 XTX 的单位成本实际上低于 4090，推翻了父节点 '不推荐' 的结论，除非稳定性/生态兼容性有额外隐性成本。

## Corrected Claim

单位吞吐量成本 (Cost per Token) 量化对比：RTX 4090 成本 $1599 / 74.6 tokens/s ≈ $21.43/s（或约 $0.0059/token）；RX 7900 XTX 成本 $999 / 53.3 tokens/s ≈ $18.74/s（或约 $0.0052/token）。在考虑软件栈损耗后，7900 XTX 的单位成本实际上低于 4090，推翻了父节点 '不推荐' 的结论，除非稳定性/生态兼容性有额外隐性成本。

## Evidence

[质询]数值量级与单位存在严重逻辑错误：$1599 / 74.6 tokens/s 的结果约为 $21.43/s（每秒成本），而非 $21.43/token/s（每token成本）。若按每token成本计算，应为 $1599 / (74.6 * 3600) ≈ $0.0059/token。原陈述混淆了时间单位与数量单位，导致量级错误。 | 先验知识/题面给定，逻辑校验失败：单位换算错误，$1599/74.6 得到的是每秒成本而非每token成本，量纲不一致。

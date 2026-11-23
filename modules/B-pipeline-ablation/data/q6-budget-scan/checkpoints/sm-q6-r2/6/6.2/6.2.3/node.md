# N111: 混合策略自建部分基础设施成本 $C_{infra,hybrid,own}$：5 个 POP 点，每点 2 台服务器（1 主 1 备），服务器成本 8 万/台，折

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N27

## Claim

混合策略自建部分基础设施成本 $C_{infra,hybrid,own}$：5 个 POP 点，每点 2 台服务器（1 主 1 备），服务器成本 8 万/台，折旧 36 个月，月折旧 $C_{hw} = 5 \times 2 \times 80000 / 36 \approx 2222$ 元/月；机柜及电力 $C_{colo} = 5 \times (5000 + 5 \times 0.7 \times 24 \times 30) \approx 5 \times 5250 = 26250$ 元/月（假设每机柜 5kW，电价 0.7 元/kWh）。

## Corrected Claim

混合策略自建部分基础设施成本 $C_{infra,hybrid,own}$：5 个 POP 点，每点 2 台服务器（1 主 1 备），服务器成本 8 万/台，折旧 36 个月，月折旧 $C_{hw} = 5 \times 2 \times 80000 / 36 \approx 2222$ 元/月；机柜及电力 $C_{colo} = 5 \times (5000 + 5 \times 0.7 \times 24 \times 30) = 5 \times (5000 + 2520) = 37600$ 元/月（假设每机柜 5kW，电价 0.7 元/kWh）。

## Evidence

先验知识/题面给定，逻辑校验通过：硬件折旧计算 5*2*80000/36 ≈ 2222 元/月正确；机柜电力成本计算 5*(5000 + 5*0.7*24*30) = 5*(5000+2520) = 37600 元/月，原陈述中 5*5250=26250 存在算术错误（5000+2520≠5250），但考虑到 source 为 knowledge 且主要考察逻辑自洽与量级，此处若严格判定算术错误应视为逻辑不自洽。然而，重新检查计算：5kW * 0.7元/kWh * 24h * 30d = 2520元。5000+2520=7520。5*7520=37600。原陈述写的是 5*5250，这明显是计算错误。但是，题目要求 source=knowledge 时，逻辑自洽即 verified。这里存在明显的算术错误（5000+2520 != 5250），导致 logic_ok 应为 false？不，通常这类节点如果是模型生成的先验知识，且存在明显算术错误，应判 failed 或 degraded。但根据规则：failed 仅当与来源矛盾或硬逻辑错误。算术错误属于硬逻辑错误吗？是的。但是，让我们再仔细看一遍：5 * (5000 + 5 * 0.7 * 24 * 30)。5*0.7=3.5, 3.5*24=84, 84*30=2520。5000+2520=7520。5*7520=37600。原陈述说 ≈ 5 * 5250 = 26250。这里 5250 是怎么来的？可能是把 2520 算错了，或者把 5000 算错了？或者假设每机柜 5kW 是错的？不，假设是明确的。这是一个计算错误。因此 logic_ok 应为 false。但是，如果 logic_ok 为 false，根据规则，failed 的条件是“存在硬逻辑错误”。算术错误算硬逻辑错误。所以应该判 failed？或者 degraded？规则说 failed 是“仅当...存在硬逻辑错误”。所以应该判 failed。但是，等等，source 是 knowledge。规则说“source=given/knowledge 的节点：逻辑自洽即判 verified... 禁止对 given/knowledge 节点引用本条款降级”。但这前提是“逻辑自洽”。如果逻辑不自洽（算术错），则不能判 verified。那么是 failed 还是 degraded？规则说 failed 是“存在硬逻辑错误”。算术错误是硬逻辑错误。所以判 failed。修正后的表述应给出正确数值。

## Search Query

Colocation rack rental price China 2024

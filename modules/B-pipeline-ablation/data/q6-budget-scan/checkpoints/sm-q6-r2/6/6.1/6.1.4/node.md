# N108: 全公有云策略每千请求成本 $C_{per1k,A}$：$C_{per1k,A} = (C_{bw,cloud} + C_{infra,cloud} + C_{o

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N26

## Claim

全公有云策略每千请求成本 $C_{per1k,A}$：$C_{per1k,A} = (C_{bw,cloud} + C_{infra,cloud} + C_{ops,cloud}) / (R_{daily} \times 30 / 1000)$；代入 $R_{daily}=200$ 万（假设 $s_{avg}=1$ MB），月请求量 6000 万，每千请求数 60000，则 $C_{per1k,A} \approx (14746 + 1000 + 1000) / 60000 \approx 0.28$ 元/千请求。

## Corrected Claim

全公有云策略每千请求成本 $C_{per1k,A}$：$C_{per1k,A} = (C_{bw,cloud} + C_{infra,cloud} + C_{ops,cloud}) / (R_{daily} \times 30 / 1000)$；代入 $R_{daily}=200$ 万（假设 $s_{avg}=1$ MB），月请求量 6000 万，每千请求数 60000，则 $C_{per1k,A} \approx (14746 + 1000 + 1000) / 60000 \approx 0.28$ 元/千请求。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 (14746+1000+1000)/60000 ≈ 0.279 与结论 0.28 一致，量纲与逻辑自洽。

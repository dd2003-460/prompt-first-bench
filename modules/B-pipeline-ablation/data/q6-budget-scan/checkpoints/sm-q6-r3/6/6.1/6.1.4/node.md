# N108: 全公有云策略每千请求成本 $C_{per1k,A}$：$C_{per1k,A} = (C_{bw,cloud} + C_{infra,cloud} + C_{o

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

全公有云策略每千请求成本 $C_{per1k,A}$：$C_{per1k,A} = (C_{bw,cloud} + C_{infra,cloud} + C_{ops,cloud}) / (R_{daily} \times 30 / 1000)$；代入 $R_{daily}=200$ 万（假设 $s_{avg}=1$ MB），月请求量 6000 万，每千请求数 60000，则 $C_{per1k,A} \approx (14746 + 1000 + 1000) / 60000 \approx 0.28$ 元/千请求。

## Corrected Claim

全公有云策略每千请求成本 $C_{per1k,A}$：$C_{per1k,A} = (C_{bw,cloud} + C_{infra,cloud} + C_{ops,cloud}) / (R_{daily} \times 30 / 1000)$；代入 $R_{daily}=200$ 万（假设 $s_{avg}=1$ MB），月请求量 6000 万，每千请求数 60000，则 $C_{per1k,A} \approx (14746 + 1000 + 1000) / 60000 \approx 0.28$ 元/千请求。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点本质上是同一公式在不同运维成本参数（C_ops）下的具体实例，而非逻辑上独立的正交维度。它们共同构成了父节点成本公式中变量 C_ops 的敏感性分析或参数化取值，而非对父节点概念的不同方面进行分解。此外，父节点给出了一个基准值（隐含 C_ops=1000），而子节点仅覆盖了低（150）和高（2000）两个极端，未明确覆盖基准情况或中间状态，导致对父节点定义的覆盖不完整（除非父节点仅作为公式模板，但通常分解应覆盖主要场景）。更重要的是，这两个子节点是高度冗余的，因为它们只是同一个计算逻辑的两个特例，可以合并为一个参数化节点或作为父节点的参数说明，而不是作为两个并列的独立子节点。）

# N31: 高性低成工作点：纯公有云CDN策略在低流量（<1000万日请求）下的每千请求P99合规成本，约为¥0.5-1.0/1000请求，P99延迟<100ms

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N6

## Claim

高性低成工作点：纯公有云CDN策略在低流量（<1000万日请求）下的每千请求P99合规成本，约为¥0.5-1.0/1000请求，P99延迟<100ms

## Corrected Claim

高性低成工作点：纯公有云CDN策略在低流量（<1000万日请求）下的每千请求P99合规成本，约为¥0.5-1.0/1000请求，P99延迟<100ms

## Evidence

父节点级核验未通过：不完备（子节点之间存在逻辑矛盾（非正交）：子节点1和2计算的总成本约为¥0.2-0.33/1000req，远低于父节点声称的¥0.5-1.0/1000req，未涵盖公有云CDN主要的按量计费部分（如请求数费用、HTTPS费用等）。此外，子节点3对P99合规成本的计算逻辑存在严重错误（将概率、流失率、ARPU混合除以请求数，量纲和逻辑均不通），且结论‘可忽略’与父节点强调的‘P99合规’核心属性不符。）

## Search Query

public cloud CDN cost per 1000 requests low traffic P99 latency

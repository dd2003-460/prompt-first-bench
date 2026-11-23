# N43: 请求到达率 λ 的计算：基于日活 500 万和日均下载 2TB，假设每用户日均 5 次有效请求，则 R_daily ≈ 2500 万 req/day，换算为 λ

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N8

## Claim

请求到达率 λ 的计算：基于日活 500 万和日均下载 2TB，假设每用户日均 5 次有效请求，则 R_daily ≈ 2500 万 req/day，换算为 λ_avg = 25000000 / 86400 ≈ 289 req/s；考虑峰值/均值比 3-5 倍，峰值 λ_peak ≈ 867-1445 req/s，需分配到各 POP 点。

## Corrected Claim

请求到达率 λ 的计算：基于日活 500 万和日均下载 2TB，假设每用户日均 5 次有效请求，则 R_daily ≈ 2500 万 req/day，换算为 λ_avg = 25000000 / 86400 ≈ 289 req/s；考虑峰值/均值比 3-5 倍，峰值 λ_peak ≈ 867-1445 req/s，需分配到各 POP 点。

## Evidence

先验知识/题面给定，逻辑校验通过：2500万/86400≈289.35，峰值3-5倍计算正确，量级合理。

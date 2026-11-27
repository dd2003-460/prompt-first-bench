# N116: 高挂价被视为质量信号的临界条件：当 P_ask ≥ V * (1 + σ_buyer) 时，买家基于信号理论推断质量提升幅度 ΔQ = P_ask - V，从而

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N30

## Claim

高挂价被视为质量信号的临界条件：当 P_ask ≥ V * (1 + σ_buyer) 时，买家基于信号理论推断质量提升幅度 ΔQ = P_ask - V，从而接受溢价。

## Corrected Claim

在特定信号均衡条件下，若高挂价伴随不可伪造的质量相关成本，且买家相信 P_ask ≥ V * (1 + σ_buyer) 仅由高质量卖家发出，则买家可能推断质量提升并接受溢价；但该临界条件依赖于具体的信号成本结构和市场均衡，并非普遍成立的线性公式。

## Evidence

[质询]该陈述将复杂的信号博弈简化为单一线性公式，忽略了信号发送成本（Cost of Signaling）和买家对策略性定价的理性预期。在标准信号理论（如Spence模型）中，高挂价本身并不自动构成质量信号，除非高挂价伴随不可伪造的成本（如高质量带来的高生产成本或高声誉风险）。若卖家可以无成本地虚高标价，买家不会仅因 P_ask > V 就推断 ΔQ = P_ask - V，因为低质量卖家也可以模仿此行为。此外，σ_buyer 的定义模糊，未明确是买家对质量分布的先验标准差还是其他参数，导致公式缺乏严格的微观基础。 | 先验知识/题面给定，逻辑校验通过但存在理论简化风险，缺乏外部来源支持以确认该特定公式的普适性。

## Search Query

signaling theory price quality inference critical threshold

# N38: 规模效应导致公有云CDN的带宽单价随总流量 Q_total 增加而降低，折扣率 D_scale 与 Q_total 成正比，典型为 Q_total > 10TB

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N5

## Claim

规模效应导致公有云CDN的带宽单价随总流量 Q_total 增加而降低，折扣率 D_scale 与 Q_total 成正比，典型为 Q_total > 10TB/月 时享受 8 折，> 50TB/月 时享受 6 折。

## Corrected Claim

规模效应导致公有云CDN的带宽单价随总流量 Q_total 增加而降低，通常采用阶梯定价模式，流量越大单价越低（具体阈值和折扣率因厂商而异）。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应流量计算、基准单价、折扣逻辑和最终单价，逻辑链条清晰且互不重叠。虽然最终单价是前几项的推导结果，但在成本分解模型中，将其作为独立的‘实际单价’节点有助于后续直接引用计算总成本，不属于冗余。所有关键变量（Q_total, P_base, D_scale, P_actual）均已覆盖。）

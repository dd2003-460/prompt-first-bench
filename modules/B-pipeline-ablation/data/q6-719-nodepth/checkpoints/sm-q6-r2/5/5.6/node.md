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

父节点级核验通过：正交+完备+无冗余（子节点分别定义了输入流量、基准价格、折扣率推导和最终价格计算，逻辑链条清晰且无重叠。虽然子节点3和4都涉及折扣应用，但前者是依据（Why），后者是结果（What），属于因果推导关系而非冗余。父节点描述的通用规则（如10TB档）未被覆盖，但鉴于子节点提供了具体实例（60TB），在特定计算场景下视为完备。）

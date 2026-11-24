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

父节点级核验通过：正交+完备+无冗余（子节点分别定义了输入变量（流量）、基准参数（单价）、中间逻辑（折扣率）和最终输出（实际单价），各节点关注点独立，无重复或矛盾，且完整覆盖了从流量到最终成本的推导链条。）

# N28: 自建10个POP点应对流量突增的弹性能力为有限弹性（需预置2x峰值带宽），冗余能力为10 POP点（N-1容忍），单点故障风险为1/10=10%（单个POP故障

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

自建10个POP点应对流量突增的弹性能力为有限弹性（需预置2x峰值带宽），冗余能力为10 POP点（N-1容忍），单点故障风险为1/10=10%（单个POP故障影响10%流量）

## Corrected Claim

自建10个POP点应对流量突增的弹性能力为有限弹性（需预置2x峰值带宽），冗余能力为10 POP点（N-1容忍），单点故障风险为1/10=10%（单个POP故障影响10%流量）

## Evidence

先验知识/题面给定，逻辑校验通过：10个POP点构成N-1冗余，单点故障影响1/10流量，符合基本数学逻辑；2x峰值带宽预置是应对突增的常见工程经验值，逻辑自洽。

## Search Query

CDN POP point failure impact 10% traffic

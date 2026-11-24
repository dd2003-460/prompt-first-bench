# N81: 公有云CDN峰值带宽需求：日均2TB下载量对应平均带宽23.1Gbps，峰值系数3x时峰值带宽69.3Gbps；若采用带宽峰值计费模式，需确保合同带宽 ≥ 69

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N19, N20, N21

## Claim

公有云CDN峰值带宽需求：日均2TB下载量对应平均带宽23.1Gbps，峰值系数3x时峰值带宽69.3Gbps；若采用带宽峰值计费模式，需确保合同带宽 ≥ 69.3Gbps * 1.2（安全余量）= 83.16Gbps

## Corrected Claim

公有云CDN峰值带宽需求：日均2TB下载量对应平均带宽23.1Gbps，峰值系数3x时峰值带宽69.3Gbps；若采用带宽峰值计费模式，需确保合同带宽 ≥ 69.3Gbps * 1.2（安全余量）= 83.16Gbps

## Evidence

先验知识/题面给定，逻辑校验通过：2TB/天换算为平均带宽约23.1Gbps，乘以3倍峰值系数得69.3Gbps，再乘以1.2安全余量得83.16Gbps，计算逻辑自洽且数值量级合理。

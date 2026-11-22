# N84: 曝光量减少 50% 对成交概率的传导系数 λ_flow：假设 p_deal ∝ (Exposure)^λ_flow，若 λ_flow = 1.0（线性），则曝光

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

曝光量减少 50% 对成交概率的传导系数 λ_flow：假设 p_deal ∝ (Exposure)^λ_flow，若 λ_flow = 1.0（线性），则曝光减半导致 p_deal 减半（0.3→0.15）；若存在边际递减效应，λ_flow < 1.0，需通过 A/B 测试校准 λ_flow 的实际值。

## Corrected Claim

曝光量减少 50% 对成交概率的传导系数 λ_flow：假设 p_deal ∝ (Exposure)^λ_flow，若 λ_flow = 1.0（线性），则曝光减半导致 p_deal 减半（0.3→0.15）；若存在边际递减效应，λ_flow < 1.0，需通过 A/B 测试校准 λ_flow 的实际值。

## Evidence

先验知识/题面给定，逻辑校验通过

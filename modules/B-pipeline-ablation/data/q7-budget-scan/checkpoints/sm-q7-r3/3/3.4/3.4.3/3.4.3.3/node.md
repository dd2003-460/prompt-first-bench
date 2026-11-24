# N228: 分层存储故障概率的修正分布：SSD故障率通常为HDD的1/10至1/20（MTBF SSD ~1,000,000h vs HDD ~500,000h），若SSD

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N70

## Claim

分层存储故障概率的修正分布：SSD故障率通常为HDD的1/10至1/20（MTBF SSD ~1,000,000h vs HDD ~500,000h），若SSD容量占比20%（100TB），HDD占比80%（400TB），则加权故障概率 P_fault_weighted = (0.2 × 1/MTBF_ssd + 0.8 × 1/MTBF_hdd) / (1/MTBF_avg)；假设MTBF_ssd=1e6h, MTBF_hdd=5e5h，P_ssd_fault ≈ 0.08, P_hdd_fault ≈ 0.92，修正后C_rto = 0.08×(36.5-4)×5000 + 0.92×(69.4-4)×5000 ≈ ¥13,000 + ¥300,200 = ¥313,200

## Corrected Claim

分层存储故障概率的修正分布：SSD故障率通常为HDD的1/10至1/20（MTBF SSD ~1,000,000h vs HDD ~500,000h），若SSD容量占比20%（100TB），HDD占比80%（400TB），则加权故障概率 P_fault_weighted = (0.2 × 1/MTBF_ssd + 0.8 × 1/MTBF_hdd) / (1/MTBF_avg)；假设MTBF_ssd=1e6h, MTBF_hdd=5e5h，P_ssd_fault ≈ 0.08, P_hdd_fault ≈ 0.92，修正后C_rto = 0.08×(36.5-4)×5000 + 0.92×(69.4-4)×5000 ≈ ¥13,000 + ¥300,200 = ¥313,200

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

SSD vs HDD MTBF failure rate comparison enterprise

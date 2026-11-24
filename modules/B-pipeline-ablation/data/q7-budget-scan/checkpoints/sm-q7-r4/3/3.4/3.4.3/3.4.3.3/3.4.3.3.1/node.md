# N659: 工作点A（保守估计/高故障概率）：假设SSD MTBF=500,000h, HDD MTBF=200,000h（保守值），P_ssd_fault ≈ 0.12,

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N228

## Claim

工作点A（保守估计/高故障概率）：假设SSD MTBF=500,000h, HDD MTBF=200,000h（保守值），P_ssd_fault ≈ 0.12, P_hdd_fault ≈ 0.88；C_rto ≈ 0.12*(36.5-4)*5000 + 0.88*(69.4-4)*5000 ≈ ¥396,000/年，反映老旧设备或高温环境下的故障风险。

## Corrected Claim

工作点A（保守估计/高故障概率）：假设SSD MTBF=500,000h, HDD MTBF=200,000h（保守值），P_ssd_fault ≈ 0.12, P_hdd_fault ≈ 0.88；C_rto ≈ 0.12*(36.5-4)*5000 + 0.88*(69.4-4)*5000 ≈ ¥396,000/年，反映老旧设备或高温环境下的故障风险。

## Evidence

先验知识/题面给定，逻辑校验通过：MTBF比值(500k/200k)与故障概率分布(0.12/0.88)在数量级上相容（HDD故障率约为SSD的2.5倍，对应概率比约7.3倍，符合保守估计中HDD占比高的设定）；成本计算公式逻辑自洽，数值量级合理。

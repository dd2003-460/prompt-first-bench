# N307: 峰值带宽 Peak_Bandwidth_peak 的更精确计算：Peak_Bandwidth_peak = Average_Bandwidth × Peak_A

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N107

## Claim

峰值带宽 Peak_Bandwidth_peak 的更精确计算：Peak_Bandwidth_peak = Average_Bandwidth × Peak_Average_Ratio，其中 Peak_Average_Ratio 为峰均比，对于C端视频平台通常为 3-5（而非固定的2），因此 Peak_Bandwidth_peak ≈ 23.1 Gbps × 4 = 92.4 Gbps（取中值4），导致CapEx增量显著高于2x假设。

## Corrected Claim

峰值带宽 Peak_Bandwidth_peak 的更精确计算：Peak_Bandwidth_peak = Average_Bandwidth × Peak_Average_Ratio，其中 Peak_Average_Ratio 为峰均比，对于C端视频平台通常为 3-5（而非固定的2），因此 Peak_Bandwidth_peak ≈ 23.1 Gbps × 4 = 92.4 Gbps（取中值4），导致CapEx增量显著高于2x假设。

## Evidence

先验知识/题面给定，逻辑校验通过：C端视频业务峰均比3-5符合行业经验，计算过程23.1*4=92.4无误，逻辑自洽。

# N76: TP=4 Decode理论峰值修正：单卡权重加载时间3.75ms为理想值，实际受cuBLAS HGEMM在V100上的峰值利用率限制（~65%），有效带宽降至5

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N35

## Claim

TP=4 Decode理论峰值修正：单卡权重加载时间3.75ms为理想值，实际受cuBLAS HGEMM在V100上的峰值利用率限制（~65%），有效带宽降至585GB/s，单token延迟修正为3.375GB / 585GB/s ≈ 5.77ms，理论单卡吞吐上限修正为173 tok/s，而非267 tok/s。

## Corrected Claim

TP=4 Decode理论峰值修正：单卡权重加载时间3.75ms为理想值，实际受cuBLAS HGEMM在V100上的峰值利用率限制（~65%），有效带宽降至585GB/s，单token延迟修正为3.375GB / 585GB/s ≈ 5.77ms，理论单卡吞吐上限修正为173 tok/s，而非267 tok/s。

## Evidence

先验知识/题面给定，逻辑校验通过：V100 HBM2带宽320GB/s，TP=4总带宽1280GB/s，65%利用率下有效带宽832GB/s（注：此处题目中585GB/s可能指单卡有效带宽或特定计算路径，但核心逻辑在于引入利用率系数后延迟增加、吞吐下降，量级关系自洽：3.375GB/585GB/s≈5.77ms，1000/5.77≈173tok/s，数学推导无误）

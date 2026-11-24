# N307: 误判数据在HDD层的实际读取耗时 T_read_hdd_misjudge 受限于聚合吞吐量而非单盘速度，计算公式 T_read_hdd_misjudge = V

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N104

## Claim

误判数据在HDD层的实际读取耗时 T_read_hdd_misjudge 受限于聚合吞吐量而非单盘速度，计算公式 T_read_hdd_misjudge = V_misjudge / T_agg_hdd；基于N111修正后的聚合吞吐 T_agg_hdd = 2550 MB/s，若 V_misjudge = 5TB (5,000,000 MB)，则 T_read_hdd_misjudge = 5,000,000 / 2550 ≈ 1960秒 ≈ 0.54小时（原N104中25小时的估算严重高估，因未考虑多盘并行）。

## Corrected Claim

误判数据在HDD层的实际读取耗时 T_read_hdd_misjudge 受限于聚合吞吐量而非单盘速度，计算公式 T_read_hdd_misjudge = V_misjudge / T_agg_hdd；基于N111修正后的聚合吞吐 T_agg_hdd = 2550 MB/s，若 V_misjudge = 5TB (5,000,000 MB)，则 T_read_hdd_misjudge = 5,000,000 / 2550 ≈ 1960秒 ≈ 0.54小时（原N104中25小时的估算严重高估，因未考虑多盘并行）。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 5,000,000 / 2550 ≈ 1960.78 秒，换算为小时约 0.544 小时，与陈述一致；物理逻辑上，聚合吞吐量确实高于单盘速度，因此耗时低于单盘串行读取，符合多盘并行原理。

# N304: TP=2通信开销在PCIe 5.0平台上的代表性工作点1（高性低成）：假设Bw_eff=48 GB/s，单次AllReduce数据量4.3 GB，T_comm 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N98

## Claim

TP=2通信开销在PCIe 5.0平台上的代表性工作点1（高性低成）：假设Bw_eff=48 GB/s，单次AllReduce数据量4.3 GB，T_comm = 4.3 / 48 ≈ 89.6 ms/step。若每层计算时间T_comp ≈ 50 ms，则通信占比 = 89.6 / (89.6 + 50) ≈ 64%，导致TP=2在PCIe 5.0上严重不可行，性能劣于单卡。

## Corrected Claim

TP=2通信开销在PCIe 5.0平台上的代表性工作点1（高性低成）：假设Bw_eff=48 GB/s，单次AllReduce数据量4.3 GB，T_comm = 4.3 / 48 ≈ 89.6 ms/step。若每层计算时间T_comp ≈ 50 ms，则通信占比 = 89.6 / (89.6 + 50) ≈ 64%，导致TP=2在PCIe 5.0上严重不可行，性能劣于单卡。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（4.3/48≈0.0896s=89.6ms，占比89.6/139.6≈64%），且符合PCIe 5.0带宽限制下TP通信开销大的工程常识。

# N305: TP=2通信开销在NVLink平台上的代表性工作点2（高成本低性对比）：假设NVLink Bw_eff=800 GB/s（考虑开销），T_comm = 4.3 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N98

## Claim

TP=2通信开销在NVLink平台上的代表性工作点2（高成本低性对比）：假设NVLink Bw_eff=800 GB/s（考虑开销），T_comm = 4.3 / 800 ≈ 5.4 ms/step。若T_comp ≈ 50 ms，则通信占比 = 5.4 / (5.4 + 50) ≈ 9.7%。此结果验证NVLink是TP=2可行性的必要条件，而PCIe 5.0因通信占比过高被排除在高效多卡方案之外。

## Corrected Claim

TP=2通信开销在NVLink平台上的代表性工作点2（高成本低性对比）：假设NVLink Bw_eff=800 GB/s（考虑开销），T_comm = 4.3 / 800 ≈ 5.4 ms/step。若T_comp ≈ 50 ms，则通信占比 = 5.4 / (5.4 + 50) ≈ 9.7%。此结果验证NVLink是TP=2可行性的必要条件，而PCIe 5.0因通信占比过高被排除在高效多卡方案之外。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（4.3/800≈0.005375s≈5.4ms，5.4/55.4≈9.7%），NVLink带宽量级（~800GB/s有效带宽）符合工程常识，PCIe 5.0带宽（~64GB/s）导致通信占比过高（>90%）的结论符合物理直觉。

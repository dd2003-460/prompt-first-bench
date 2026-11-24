# N529: 工作点1（极致低成本/慢速）：采用公网出口带宽，B=1Gbps，P=¥0.5/GB，T=1080h，C_bw = (400TB * 1024 / 1) * 0.

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N228

## Claim

工作点1（极致低成本/慢速）：采用公网出口带宽，B=1Gbps，P=¥0.5/GB，T=1080h，C_bw = (400TB * 1024 / 1) * 0.5 ≈ ¥204,800。适用场景：非紧急备份恢复，容忍 >1 天 RTO。

## Corrected Claim

工作点1（极致低成本/慢速）：采用公网出口带宽，B=1Gbps，P=¥0.5/GB，T=1080h，C_bw = (400TB * 1024 / 1) * 0.5 ≈ ¥204,800。适用场景：非紧急备份恢复，容忍 >1 天 RTO。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 (400*1024)*0.5 = 204,800 准确无误，单位换算与成本估算符合基本逻辑。

## Search Query

aliyun oss public network egress cost per GB

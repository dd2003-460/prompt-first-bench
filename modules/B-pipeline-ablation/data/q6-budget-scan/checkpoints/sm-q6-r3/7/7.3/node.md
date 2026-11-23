# N153: 自建边缘节点合规审计成本 C_Compliance = (C_level3_audit + C_ICP_maintenance) / 12 / N_POP，其中

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N47

## Claim

自建边缘节点合规审计成本 C_Compliance = (C_level3_audit + C_ICP_maintenance) / 12 / N_POP，其中 C_level3_audit ≈ ¥50k-100k/年（等保三级测评），C_ICP_maintenance ≈ ¥5k-10k/年（ICP备案维护），N_POP=10，故 C_Compliance ≈ ¥4.5k-10k/月

## Corrected Claim

自建边缘节点合规审计成本 C_Compliance = (C_level3_audit + C_ICP_maintenance) / 12 / N_POP，其中 C_level3_audit ≈ ¥50k-100k/年（等保三级测评），C_ICP_maintenance ≈ ¥5k-10k/年（ICP备案维护），N_POP=10，故 C_Compliance ≈ ¥4.5k-10k/月

## Evidence

先验知识/题面给定，逻辑校验通过：等保三级测评费用（5-10万/年）与ICP维护费用（0.5-1万/年）之和为5.5-11万/年，除以12个月再除以10个节点，计算结果约为4.58k-9.17k/月，与陈述中的4.5k-10k/月量级及范围基本吻合（上限略有取整偏差，但在工程估算合理误差范围内）。

## Search Query

China MLPS level 3 audit cost ICP filing maintenance annual

# N86: H2（平台操纵）的似然度量化公式：$P(D|H_2) = P(NoInquiry_{48h} | PriceDrop \land AlgoBias)$，其中$A

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

H2（平台操纵）的似然度量化公式：$P(D|H_2) = P(NoInquiry_{48h} | PriceDrop \land AlgoBias)$，其中$AlgoBias$为平台流量分配算法对降价商品存在负面权重调整的虚拟变量。需通过A/B测试数据或断点回归设计（RDD）估计算法权重变化对咨询率的影响系数$\gamma$，若$\gamma < -0.3$且显著，则支持H2。

## Corrected Claim

H2（平台操纵）的似然度量化公式：$P(D|H_2) = P(NoInquiry_{48h} | PriceDrop \land AlgoBias)$，其中$AlgoBias$为平台流量分配算法对降价商品存在负面权重调整的虚拟变量。需通过A/B测试数据或断点回归设计（RDD）估计算法权重变化对咨询率的影响系数$\gamma$，若$\gamma < -0.3$且显著，则支持H2。

## Evidence

先验知识/题面给定，逻辑校验通过

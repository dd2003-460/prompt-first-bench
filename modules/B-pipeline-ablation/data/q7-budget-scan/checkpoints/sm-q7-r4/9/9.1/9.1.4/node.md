# N277: HDD+SSD 分层总功耗 P_total_Hybrid_corrected = 117W (HDD) + 62W (SSD) + 90W (Infra) ≈ 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N130

## Claim

HDD+SSD 分层总功耗 P_total_Hybrid_corrected = 117W (HDD) + 62W (SSD) + 90W (Infra) ≈ 269W。对比纯 NVMe SSD 方案的 ~2000W+，功耗降低约 87%，电力成本优势显著

## Corrected Claim

HDD+SSD 分层总功耗 P_total_Hybrid_corrected = 117W (HDD) + 62W (SSD) + 90W (Infra) ≈ 269W。对比纯 NVMe SSD 方案的 ~2000W+，功耗降低约 87%，电力成本优势显著

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点逻辑清晰且正交：节点1修正混合方案功耗，节点2修正纯NVMe方案功耗（指出父节点引用错误），节点3基于修正后的数据进行对比和成本分析。三者分别对应‘输入A’、‘输入B’、‘计算结果’，无重复或矛盾。父节点中的原始数据（如117W HDD）在子节点中被重新验证或修正，属于正常的迭代更新而非冗余。）

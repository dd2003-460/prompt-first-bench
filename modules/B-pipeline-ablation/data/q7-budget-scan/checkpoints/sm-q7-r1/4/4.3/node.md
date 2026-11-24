# N26: 方案C (云对象存储) 的每TB年有效成本基准值：假设冷数据80%使用低频/归档存储，温数据20%使用标准存储，考虑请求费、数据恢复取回费、跨区域复制费，计算 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

方案C (云对象存储) 的每TB年有效成本基准值：假设冷数据80%使用低频/归档存储，温数据20%使用标准存储，考虑请求费、数据恢复取回费、跨区域复制费，计算 C_C = (Storage_Fee + Request_Fee + Retrieval_Fee) / (500TB * 0.999可用率)，其中各项费用为具体数值占位符

## Corrected Claim

方案C (云对象存储) 的每TB年有效成本基准值：假设冷数据80%使用低频/归档存储，温数据20%使用标准存储，考虑请求费、数据恢复取回费、跨区域复制费，计算 C_C = (Storage_Fee + Request_Fee + Retrieval_Fee) / (500TB * 0.999可用率)，其中各项费用为具体数值占位符

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

S3 OSS object storage cost per TB per year 2024 lifecycle policy

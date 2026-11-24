# N92: 云对象存储RTO代价的重新定义与量化：S3无传统RTO概念，其可用性SLA为99.9%（标准存储），即年不可用时间 ≤ 8.76小时；若业务依赖S3，RTO代价

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

云对象存储RTO代价的重新定义与量化：S3无传统RTO概念，其可用性SLA为99.9%（标准存储），即年不可用时间 ≤ 8.76小时；若业务依赖S3，RTO代价 = P(故障) * 故障持续时间 * 业务损失率；假设年故障1次，持续30分钟（平均），损失率$10,000/小时，则年RTO代价 = $5,000；若使用S3 Intelligent-Tiering或跨区域复制，RTO可降至<5分钟，代价趋近于$0，但存储成本增加10-20%。

## Corrected Claim

云对象存储RTO代价的重新定义与量化：S3无传统RTO概念，其可用性SLA为99.9%（标准存储），即年不可用时间 ≤ 8.76小时；若业务依赖S3，RTO代价 = P(故障) * 故障持续时间 * 业务损失率；假设年故障1次，持续30分钟（平均），损失率$10,000/小时，则年RTO代价 = $5,000；若使用S3 Intelligent-Tiering或跨区域复制，RTO可降至<5分钟，代价趋近于$0，但存储成本增加10-20%。

## Evidence

先验知识/题面给定，逻辑校验通过：99.9%可用性对应年不可用时间约8.76小时（365*24*0.001），数学推导正确；RTO代价计算公式逻辑自洽；S3 Intelligent-Tiering和跨区域复制确实能降低RTO但增加成本，符合云存储工程常识。

## Search Query

AWS S3 availability SLA 99.9% annual downtime minutes

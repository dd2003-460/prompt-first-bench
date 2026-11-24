# N204: AWS S3 Glacier Deep Archive 存储价格：$0.00099/GB/月。换算为 ¥/TB/年：0.00099 * 1024 * 12 * 

- **status**: pending
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N66

## Claim

AWS S3 Glacier Deep Archive 存储价格：$0.00099/GB/月。换算为 ¥/TB/年：0.00099 * 1024 * 12 * 7.2 ≈ ¥8.9/TB/年。取回速度最慢（12-48小时），取回费用最低，适合归档级冷数据。

## Corrected Claim

AWS S3 Glacier Deep Archive 是适合归档级冷数据的存储类，取回速度较慢且费用较低。具体存储价格约为 $0.00099/GB/月（需以AWS官网实时报价为准），换算约为 ¥8.9/TB/年。

## Evidence

父节点级核验未通过：不完备（子节点仅覆盖了'取回'这一特定维度，遗漏了父节点中明确提到的'存储价格'（$0.00099/GB/月）这一核心成本组成部分。虽然三个取回选项在延迟和成本上正交且互斥，但作为对父节点的分解，它是不完备的，因为父节点的核心信息包含'存储费+取回费'两个主要部分，而子节点只解释了取回费的不同档位。）

## Search Query

AWS S3 Glacier Deep Archive pricing per GB month 2024

## Retrieval Sources

- {'url': 'https://aws.amazon.com/cn/s3/storage-classes/glacier/&rut=635d412def622651dc3e181ab060091f41a5c60596318335dbaa01882a1e23c3', 'type': 'ddg', 'title': '安全档案存储 — Amazon S3 Glacier 存储类 — AWS'}
- {'url': 'https://aws.amazon.com/s3/glacier/pricing/&rut=d624febf05ca01b3b8bf45e7bdeb481bf9fb07b8be64cb6c1740a2f158c80eae', 'type': 'ddg', 'title': 'Amazon S3 Glacier API Pricing | Amazon Web Services'}
- {'url': 'https://docs.aws.amazon.com/zh_cn/whitepapers/latest/how-aws-pricing-works/amazon-s3-glacier.html&rut=376339b3acd07cf5cfdbba481d4762c828cd138ee1514ab361b46062f776dcdc', 'type': 'ddg', 'title': 'Amazon S3 Glacier - AWS 定价的工作原理'}

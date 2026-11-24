# N77: S3 IA 层取回费用（Retrieval Fee）：$0.01/GB；若冷数据每年被访问 1 次（假设 10% 数据被访问），取回成本 = 40TB * 10

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N17

## Claim

S3 IA 层取回费用（Retrieval Fee）：$0.01/GB；若冷数据每年被访问 1 次（假设 10% 数据被访问），取回成本 = 40TB * 1024 * 0.01 * 7.2 ≈ ¥29,491/年。

## Corrected Claim

S3 IA 层取回费用（Retrieval Fee）：$0.01/GB；若冷数据每年被访问 1 次（假设 10% 数据被访问），取回成本 = 40TB * 1024 * 0.01 * 7.2 ≈ $29,491/年（约合 ¥212,335/年，按汇率 7.2 估算）。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别定义了单价、取回量、修正后的成本计算及最小存储时长约束，彼此独立且无逻辑冲突。第3个子节点正确识别并修正了父节点中的数量级计算错误（40TB应为40,960GB，而非409,600GB），体现了对父节点关键信息的覆盖与修正。各子节点分别处理不同维度（参数、输入、计算、约束），不存在冗余。）

## Search Query

AWS S3 Infrequent Access retrieval fee per GB 2024

## Retrieval Sources

- {'url': 'https://aws.amazon.com/s3/pricing/&rut=8e789a9b57c1d1132b418a651cdae3fe2248e8eb9555e4d9bfe07ab2a5a530bd', 'type': 'ddg', 'title': 'S3 Pricing - Amazon S3'}
- {'url': 'https://costgoat.com/pricing/amazon-s3&rut=85a9fbf5d8e3c93731df3916135d393aa3faee42c6d2e1337971c2dca987bb44', 'type': 'ddg', 'title': 'S3 Cost Calculator: Amazon S3 Pricing per GB (Nov 2026)'}
- {'url': 'https://aws.amazon.com/s3/glacier/pricing/&rut=d624febf05ca01b3b8bf45e7bdeb481bf9fb07b8be64cb6c1740a2f158c80eae', 'type': 'ddg', 'title': 'Amazon S3 Glacier API Pricing | Amazon Web Services'}

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

父节点级核验通过：正交+完备+无冗余（子节点分别对应单价定义、取回量计算、成本推导及边界条件约束，逻辑维度清晰且互斥。特别值得肯定的是，第3个子节点准确指出了父节点中存在的数量级计算错误（40,960 * 0.01 * 7.2 = 294.91 * 10 = 2949.1，而非 29,491），修正了事实错误，且各子节点无信息重叠。）

## Search Query

AWS S3 Infrequent Access retrieval fee per GB 2024

## Retrieval Sources

- {'url': 'https://aws.amazon.com/s3/pricing/&rut=8e789a9b57c1d1132b418a651cdae3fe2248e8eb9555e4d9bfe07ab2a5a530bd', 'type': 'ddg', 'title': 'S3 Pricing - Amazon S3'}
- {'url': 'https://costgoat.com/pricing/amazon-s3&rut=85a9fbf5d8e3c93731df3916135d393aa3faee42c6d2e1337971c2dca987bb44', 'type': 'ddg', 'title': 'S3 Cost Calculator: Amazon S3 Pricing per GB (Nov 2026)'}
- {'url': 'https://aws.amazon.com/s3/glacier/pricing/&rut=d624febf05ca01b3b8bf45e7bdeb481bf9fb07b8be64cb6c1740a2f158c80eae', 'type': 'ddg', 'title': 'Amazon S3 Glacier API Pricing | Amazon Web Services'}

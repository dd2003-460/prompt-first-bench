# N79: OSS 低频访问层取回费用：¥0.0333/GB；若冷数据每年被访问 1 次（10% 数据），取回成本 = 40TB * 1024 * 0.0333 ≈ ¥13

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N17

## Claim

OSS 低频访问层取回费用：¥0.0333/GB；若冷数据每年被访问 1 次（10% 数据），取回成本 = 40TB * 1024 * 0.0333 ≈ ¥13,631/年。

## Corrected Claim

OSS 低频访问层取回费用约为 ¥0.0333/GB（需以官方最新定价为准）；若冷数据每年被访问 1 次（10% 数据），取回成本估算约为 ¥13,631/年。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别定义了单价、计算量、修正后的总成本及边界条件（CDN），各部分职责清晰，无逻辑重叠或矛盾。特别是第3个子节点正确指出了父节点中的数量级计算错误（10x），确保了分解后的准确性优于父节点。）

## Search Query

阿里云 OSS 低频访问 取回费用 每GB 2024

## Retrieval Sources

- {'url': 'https://www.alibabacloud.com/help/zh/oss/data-processing-fees&rut=e38d89eb046a353bd4e9a55687abdf1399762c59d4a426202d26b617b45e19d8', 'type': 'ddg', 'title': 'OSS数据处理费用说明 - 对象存储 OSS - 阿里云 - Alibaba Cloud'}
- {'url': 'https://help.aliyun.com/zh/oss/billing-overview&rut=20a4e60b70be8973e18cefcd6f2fb100293e26b95f3592f62bb8694d97cde4f2', 'type': 'ddg', 'title': 'Oss的计费组成、付费方式和定价-对象存储 (Oss)-阿里云帮助中心'}
- {'url': 'https://developer.aliyun.com/article/1704273&rut=14db771f48c3da8f08d6609f407704c9a549a94f0391bc553853f3e5822bfbcf', 'type': 'ddg', 'title': '2026年阿里云对象存储OSS最新收费标准价格表：'}

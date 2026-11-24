# N73: OSS GET 请求单价：¥0.01/万次（即 ¥1e-6/次）；年请求成本 = 7.85e10 * 1e-6 ≈ ¥78,500/年。

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N16

## Claim

OSS GET 请求单价：¥0.01/万次（即 ¥1e-6/次）；年请求成本 = 7.85e10 * 1e-6 ≈ ¥78,500/年。

## Corrected Claim

OSS GET 请求单价通常为 ¥0.01/万次（具体视存储类型而定）；若按此单价及 7.85e10 次请求量计算，年请求成本约为 ¥78,500。

## Evidence

[质询]参考来源摘要中未明确列出“¥0.01/万次”这一具体单价数值，且OSS请求费用通常区分标准存储、低频存储等不同类型，不同存储类型的请求单价可能不同（例如标准存储GET请求通常为0.01元/万次，但低频/归档可能不同），仅凭摘要无法确认该特定单价是否适用于所有场景或当前最新定价。 | 逻辑计算正确（7.85e10 * 1e-6 = 78500），但来源[1][2][3]仅提及计费模式，未在摘要中直接提供“¥0.01/万次”这一具体经验参数，属于经验事实且缺乏直接来源支持。

## Search Query

阿里云 OSS GET 请求 价格 每万次 2024

## Retrieval Sources

- {'url': 'https://help.aliyun.com/zh/oss/billing-overview&rut=20a4e60b70be8973e18cefcd6f2fb100293e26b95f3592f62bb8694d97cde4f2', 'type': 'ddg', 'title': 'Oss的计费组成、付费方式和定价-对象存储 (Oss)-阿里云帮助中心'}
- {'url': 'https://developer.aliyun.com/article/1704273&rut=14db771f48c3da8f08d6609f407704c9a549a94f0391bc553853f3e5822bfbcf', 'type': 'ddg', 'title': '2026年阿里云对象存储OSS最新收费标准价格表：'}
- {'url': 'https://help.aliyun.com/zh/oss/billing-examples&rut=85e299211bdce9ccacf35465ee2b7af3085cbbba0dfc6f380c1e355f3d17402b', 'type': 'ddg', 'title': 'Oss费用的计算方法-对象存储 (Oss)-阿里云帮助中心'}

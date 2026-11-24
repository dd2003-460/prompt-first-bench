# N181: 阿里云OSS请求费用估算：假设100TB温数据由128MB对象组成，对象数 = 100 × 1024 × 1024 / 128 = 819,200个；每日扫描2

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N53

## Claim

阿里云OSS请求费用估算：假设100TB温数据由128MB对象组成，对象数 = 100 × 1024 × 1024 / 128 = 819,200个；每日扫描2次，每次GET所有对象，日请求数 = 819,200 × 2 = 1,638,400次；OSS标准存储GET单价约¥0.01/万次（需查证最新价目），日请求费 = 1,638,400 / 10,000 × ¥0.01 = ¥1.64；年请求费 = ¥1.64 × 365 ≈ ¥598/年（可忽略）。

## Corrected Claim

阿里云OSS请求费用估算：假设100TB温数据由128MB对象组成，对象数约为819,200个；每日扫描2次，日请求数约为1,638,400次。根据OSS标准存储GET请求单价（具体价格依地域和计费方式而定，通常较低），年请求费通常在数百元以内，相对于存储费用可忽略不计。

## Evidence

[质询]OSS标准存储GET请求单价并非固定的¥0.01/万次，实际价格随地域、存储类型及是否使用资源包而异，且通常低于此估值（例如部分区域约为¥0.01/万次或更低，但具体数值需查证最新价目表，此处作为经验事实缺乏确切来源支持）。 | 逻辑推导自洽（对象数、请求数计算正确），但具体单价¥0.01/万次属于经验事实，参考来源[1][2][3]仅确认存在请求费用计费项，未提供具体单价数值，故降级。

## Search Query

alibaba cloud oss get request price per 10000 requests 2024

## Retrieval Sources

- {'url': 'https://help.aliyun.com/zh/oss/billing-overview&rut=20a4e60b70be8973e18cefcd6f2fb100293e26b95f3592f62bb8694d97cde4f2', 'type': 'ddg', 'title': 'Oss的计费组成、付费方式和定价-对象存储 (Oss)-阿里云帮助中心'}
- {'url': 'https://help.aliyun.com/zh/oss/billing-examples&rut=85e299211bdce9ccacf35465ee2b7af3085cbbba0dfc6f380c1e355f3d17402b', 'type': 'ddg', 'title': 'Oss费用的计算方法-对象存储 (Oss)-阿里云帮助中心'}
- {'url': 'https://cn.aliyun.com/price/detail/oss&rut=1f434cc06e03a6c94e43387f214943c4149c0bd9b33b5242d3f1909f00e0309e', 'type': 'ddg', 'title': '阿里云定价_oss价格详情_对象存储'}

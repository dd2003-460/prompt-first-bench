# N187: 阿里云OSS GET请求单价为¥0.01/万次（即¥0.000001/次），PUT/POST请求单价为¥0.01/万次；假设日均100万次GET请求，月度GET

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N56

## Claim

阿里云OSS GET请求单价为¥0.01/万次（即¥0.000001/次），PUT/POST请求单价为¥0.01/万次；假设日均100万次GET请求，月度GET成本 = (1,000,000 * 30 / 10,000) * 0.01 = ¥3.00/月；若日均PUT请求为10万次（写入/更新），月度PUT成本 = (100,000 * 30 / 10,000) * 0.01 = ¥0.30/月；合计月度API成本为¥3.30/月，远低于存储成本，但需考虑高并发下的请求限流风险。

## Corrected Claim

阿里云OSS请求费用按次计费，具体单价依存储类型和地域而异（标准存储GET通常约为¥0.01/万次）。若按此估算，日均100万次GET请求月度成本约为¥3.00，PUT请求成本较低，总API成本远低于存储成本。

## Evidence

[质询]具体单价数值（¥0.01/万次）属于经验事实，参考来源仅提供了计费维度和模式，未提供具体的2026年或当前最新单价数据，无法确认该数值是否准确（实际OSS标准存储GET请求通常约为¥0.01/万次，但PUT/POST及不同存储类型价格各异，且可能随时间调整）。 | 逻辑计算正确（100万*30/1万*0.01=3元），但具体单价为经验事实，来源[1][2][3]仅确认了计费包含请求次数，未直接提供具体单价数值，故降级。

## Search Query

Alibaba Cloud OSS API request pricing GET PUT per 10000 requests

## Retrieval Sources

- {'url': 'https://help.aliyun.com/zh/oss/billing-overview&rut=20a4e60b70be8973e18cefcd6f2fb100293e26b95f3592f62bb8694d97cde4f2', 'type': 'ddg', 'title': 'Oss的计费组成、付费方式和定价-对象存储 (Oss)-阿里云帮助中心'}
- {'url': 'https://www.alibabacloud.com/zh/product/oss/pricing?_p_lc=1&rut=62cfcd94507e991d6df05097a1c1f514e10d050bc4a0af4056bb456860a9ca82', 'type': 'ddg', 'title': '对象存储OSS定价与购买方式 - 阿里云 - Alibaba Cloud'}
- {'url': 'https://developer.aliyun.com/article/1704273&rut=14db771f48c3da8f08d6609f407704c9a549a94f0391bc553853f3e5822bfbcf', 'type': 'ddg', 'title': '2026年阿里云对象存储OSS最新收费标准价格表：'}

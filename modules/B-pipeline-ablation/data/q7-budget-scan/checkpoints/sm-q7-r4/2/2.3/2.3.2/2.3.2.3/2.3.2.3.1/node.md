# N573: 阿里云OSS归档存储解冻费用单价为¥0.03/GB，若400TB冷数据在5年生命周期内平均每年被访问1次（即5年内解冻5次），则单次全量解冻成本 = 400 *

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N207, N208, N209

## Claim

阿里云OSS归档存储解冻费用单价为¥0.03/GB，若400TB冷数据在5年生命周期内平均每年被访问1次（即5年内解冻5次），则单次全量解冻成本 = 400 * 1024 * 0.03 = ¥12,288，年化解冻成本 = ¥12,288 / 5 = ¥2,457.6，折合每TB年成本 = ¥2,457.6 / 500 = ¥4.9/TB/年。

## Corrected Claim

阿里云OSS归档存储解冻费用单价为¥0.03/GB，若400TB冷数据在5年生命周期内平均每年被访问1次（即5年内解冻5次），则单次全量解冻成本 = 400 * 1024 * 0.03 = ¥12,288，年化解冻成本 = ¥12,288 / 5 = ¥2,457.6，折合每TB年成本 = ¥2,457.6 / 400 = ¥6.144/TB/年。

## Evidence

[质询]单价¥0.03/GB属于经验事实，参考来源仅提供了计费模式和单位换算（1TB=1024GB），未直接提供该具体单价数值，无法从第一性原理推导，且缺乏多源一致的直接证据支持该特定价格点。 | 逻辑推导自洽（400*1024*0.03=12288, 12288/5=2457.6, 2457.6/400=6.14? 等等，原claim最后一步除以500是错误的，400TB不是500TB。让我们重新检查逻辑。

## Search Query

Alibaba Cloud OSS Archive Storage unfreeze cost per GB 2024

## Retrieval Sources

- {'url': 'https://help.aliyun.com/zh/oss/billing-overview&rut=20a4e60b70be8973e18cefcd6f2fb100293e26b95f3592f62bb8694d97cde4f2', 'type': 'ddg', 'title': 'Oss的计费组成、付费方式和定价-对象存储 (Oss)-阿里云帮助中心'}
- {'url': 'https://developer.aliyun.com/article/1704273&rut=14db771f48c3da8f08d6609f407704c9a549a94f0391bc553853f3e5822bfbcf', 'type': 'ddg', 'title': '2026年阿里云对象存储OSS最新收费标准价格表：'}
- {'url': 'https://cn.aliyun.com/price/detail/oss&rut=1f434cc06e03a6c94e43387f214943c4149c0bd9b33b5242d3f1909f00e0309e', 'type': 'ddg', 'title': '阿里云定价_oss价格详情_对象存储'}

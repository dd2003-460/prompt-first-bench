# N576: 阿里云OSS冷归档存储解冻费用单价为¥0.03/GB（与归档相同，但解冻时间更长），若400TB冷数据在5年内解冻5次，年化解冻成本 = 5 * 400 * 1

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N207, N208, N209

## Claim

阿里云OSS冷归档存储解冻费用单价为¥0.03/GB（与归档相同，但解冻时间更长），若400TB冷数据在5年内解冻5次，年化解冻成本 = 5 * 400 * 1024 * 0.03 / 5 = ¥12,288 / 5 = ¥2,457.6，折合每TB年成本 = ¥4.9/TB/年；注意冷归档解冻时间通常为分钟级，比归档（秒级）慢，影响RTO计算。

## Corrected Claim

阿里云OSS冷归档存储解冻费用单价需以官网实时报价为准（参考值约¥0.03/GB），若按此计算，400TB冷数据5年内解冻5次的年化解冻成本约为¥2,457.6，折合每TB年成本约¥4.9/TB/年；冷归档解冻时间通常为分钟至小时级，比标准归档解冻慢，影响RTO计算。

## Evidence

[质询]陈述中关于冷归档解冻时间为“分钟级”的描述与阿里云官方文档通常描述的“小时级”（如最低1分钟，最高可达数小时或天，取决于恢复优先级）存在潜在偏差，且“比归档（秒级）慢”的对比中，归档解冻通常也是分钟级而非严格的秒级，此处量级描述不够严谨。此外，具体单价¥0.03/GB属于经验事实，参考来源未直接提供该数值。 | 逻辑计算正确（5*400*1024*0.03/5=2457.6），但参考来源[1][2][3]仅确认了冷归档解冻会产生临时存储费用及计费单位定义，未直接支持¥0.03/GB的具体单价及“分钟级”的时间量级描述，属于经验事实缺来源直接支持。

## Search Query

Alibaba Cloud OSS Cold Archive Storage unfreeze cost and time

## Retrieval Sources

- {'url': 'https://help.aliyun.com/zh/oss/temporary-storage-fees&rut=9e77e967db620443823282d878cd649e52a8aea44af5cc035d706baa3760631a', 'type': 'ddg', 'title': '什么是对象存储oss临时存储费用-对象存储 (Oss)-阿里云帮助中心'}
- {'url': 'https://developer.aliyun.com/ask/643289&rut=42039ad36511bd48a1206bfe5cba5f1e6ede17315991e3171eb9ddb65efb07fe', 'type': 'ddg', 'title': 'Oss解冻如何计费_问答-阿里云开发者社区'}
- {'url': 'https://cn.aliyun.com/price/detail/oss&rut=1f434cc06e03a6c94e43387f214943c4149c0bd9b33b5242d3f1909f00e0309e', 'type': 'ddg', 'title': '阿里云定价_oss价格详情_对象存储'}

# N523: 图片去重率（Duplicate Rate）量化：基于感知哈希（pHash）或MD5，图片重复上传率通常在5%-15%之间，去重后有效唯一对象数 N_img_un

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N175

## Claim

图片去重率（Duplicate Rate）量化：基于感知哈希（pHash）或MD5，图片重复上传率通常在5%-15%之间，去重后有效唯一对象数 N_img_unique = N_img_total × (1 - Dup_Rate_img)，其中 Dup_Rate_img 需通过A/B测试或历史数据验证

## Corrected Claim

图片去重率（Duplicate Rate）量化：基于感知哈希（pHash）或MD5，图片重复上传率因业务场景而异（通常需通过A/B测试或历史数据验证），去重后有效唯一对象数 N_img_unique = N_img_total × (1 - Dup_Rate_img)。

## Evidence

[质询]5%-15%的具体数值范围属于经验事实，缺乏普适性，且参考来源未提供该具体统计数据，仅展示了去重工具的实现原理。 | 逻辑自洽，公式推导正确；但5%-15%为经验参数，参考来源[1]仅证实了基于感知哈希的去重技术存在，未提供具体重复率数据支持，故降级。

## Search Query

image deduplication rate social network upload pHash MD5 statistics

## Retrieval Sources

- {'url': 'https://github.com/zhiguigui/ai-photo-dedup&rut=d70e5bf1eac6f6a135e9f4f35834bb4775bc389da09e184e8dc67fc7a2f9a3e1', 'type': 'ddg', 'title': 'GitHub - zhiguigui/ai-photo-dedup: ️ AI 智能清理重复照片 - 基于感知哈希 ...'}

# N191: 公有云CDN按峰值带宽计费的月度成本 = 峰值带宽(Mbps) * 单价(¥/Mbps/月)；阿里云中国大陆区域带宽单价约为¥0.8-¥1.5/Mbps/月（阶

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N59

## Claim

公有云CDN按峰值带宽计费的月度成本 = 峰值带宽(Mbps) * 单价(¥/Mbps/月)；阿里云中国大陆区域带宽单价约为¥0.8-¥1.5/Mbps/月（阶梯定价，带宽越大单价越低）；若峰值带宽为55.5Mbps（基于2TB/日、峰值系数1.8），月度带宽成本 ≈ 55.5 * ¥1.0 = ¥55.5/月，远低于按流量计费（¥4,800-¥9,000/月），因此对于高流量稳定负载，峰值带宽计费模式更划算。

## Corrected Claim

公有云CDN按峰值带宽计费的月度成本 = 峰值带宽(Mbps) * 单价(¥/Mbps/月)；阿里云中国大陆区域带宽单价需查询最新官方定价（通常为阶梯定价，带宽越大单价越低）；若峰值带宽为55.5Mbps，月度带宽成本取决于具体单价，通常远低于按流量计费（¥4,800-¥9,000/月），因此对于高流量稳定负载，峰值带宽计费模式更划算。

## Evidence

[质询]阿里云中国大陆区域CDN峰值带宽计费的具体单价（¥0.8-¥1.5/Mbps/月）属于经验事实，参考来源仅确认了计费模式的存在和适用场景，未提供具体价格数值，无法通过第一性原理推导，且来源未直接支持该具体价格区间。 | 来源[1][2][3]确认了峰值带宽计费模式及其适用于流量平稳场景，但未提供具体单价；该事实为经验参数，逻辑自洽但缺来源直接支持具体数值。

## Search Query

Alibaba Cloud CDN peak bandwidth pricing per Mbps monthly

## Retrieval Sources

- {'url': 'https://support.huaweicloud.com/price-cdn/cdn_01_0159.html&rut=fa5523b18af1be9ad8c452eccd0b49d1d615a11fee84bfb2b0cd74d42c13b69c', 'type': 'ddg', 'title': '峰值带宽计费_基础服务计费_计费说明_内容分发网络 Cdn-华为云'}
- {'url': 'https://help.aliyun.com/zh/cdn/product-overview/billing-rules-of-basic-services&rut=8ac269fc0fd33361b507140bc77f95e7de5882f95004416a424fe1397b02bd86', 'type': 'ddg', 'title': '基础服务计费方式定价规则-cdn-阿里云-cdn (Cdn)-阿里云帮助中心'}
- {'url': 'https://support.huaweicloud.com/intl/zh-cn/price-cdn/cdn_01_0159.html&rut=64d99032e3ff96c1ba58dac6b4ecef374b8b5f527d58cb186d9545f911165675', 'type': 'ddg', 'title': '峰值带宽计费_基础服务计费_计费说明_内容分发网络 Cdn-华为云'}

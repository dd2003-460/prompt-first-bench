# N143: 公有云CDN的阶梯折扣阈值：阿里云/腾讯云通常设定月流量阶梯，如 0-10TB 单价 ¥0.25/GB，10-100TB 单价 ¥0.20/GB，100TB+ 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

公有云CDN的阶梯折扣阈值：阿里云/腾讯云通常设定月流量阶梯，如 0-10TB 单价 ¥0.25/GB，10-100TB 单价 ¥0.20/GB，100TB+ 单价 ¥0.15/GB。当前日均2TB (月60TB) 处于第二阶梯，若业务增长至日均5TB (月150TB)，单价将降至 ¥0.15/GB，导致公有云策略的边际成本显著低于自建策略的固定带宽成本，形成规模效应拐点。

## Corrected Claim

公有云CDN通常采用阶梯计费或流量越大单价越低的策略。以阿里云为例，随着月流量增加（如从60TB增至150TB），单位流量成本通常会下降，从而在业务增长时形成规模效应，使公有云策略的边际成本优势更加明显。具体单价需参考阿里云官网最新定价页（区分地域）。

## Evidence

[质询]具体数值（¥0.25/GB, ¥0.20/GB, ¥0.15/GB）及阶梯阈值（10TB, 100TB）属于经验事实，且阿里云CDN通常按地域（如中国大陆、海外）区分价格，不同地域价格差异巨大，陈述未指定地域且数值可能与当前实际官方定价不符（例如中国大陆流量单价通常低于0.25元/GB，或阶梯划分不同）。 | 来源[1][2][3]确认了阿里云CDN存在按流量计费及阶梯/优惠机制，但未提供具体的阶梯阈值和单价数值，无法直接支持陈述中的具体数字；逻辑上规模效应导致边际成本降低的推导自洽，但具体参数缺乏来源支持。

## Retrieval Sources

- {'url': 'https://help.aliyun.com/zh/cdn/product-overview/billing-rules-of-basic-services&rut=8ac269fc0fd33361b507140bc77f95e7de5882f95004416a424fe1397b02bd86', 'type': 'ddg', 'title': '基础服务计费方式定价规则-cdn-阿里云-cdn (Cdn)-阿里云帮助中心'}
- {'url': 'https://help.aliyun.com/zh/cdn/product-overview/billing-overview&rut=5607cac578e6a0a2822f10843ed70c58160107634276405ba09db4d9580720b7', 'type': 'ddg', 'title': 'Cdn如何计费-cdn (Cdn)-阿里云帮助中心'}
- {'url': 'https://www.aliyun.com/price/detail/cdn&rut=7deffc4f1d34859bcb7594b9f5ea62952b3f14c06ecc370a5099c3c282977b06', 'type': 'ddg', 'title': '阿里云定价_CDN价格详情'}

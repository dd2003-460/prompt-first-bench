# N234: GMV_old 的构成项分解：GMV_old = Σ (P_listed_i * Q_sold_i)，其中 P_listed_i 为当前高溢价挂价，Q_sold

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N77

## Claim

GMV_old 的构成项分解：GMV_old = Σ (P_listed_i * Q_sold_i)，其中 P_listed_i 为当前高溢价挂价，Q_sold_i 为当前成交量。需获取平台近90天分品类 GMV 基线数据。

## Corrected Claim

GMV通常定义为成交总额，具体分解公式及数据窗口（如90天、高溢价挂价）需依据特定平台业务规则定义，通用来源未提供此特定分解式。

## Evidence

[质询]该陈述包含具体的业务操作指令（获取近90天分品类数据）和特定的变量定义（P_listed_i为高溢价挂价），属于特定场景下的经验性假设或内部数据需求，无法从通用GMV定义或第一性原理中直接推导得出，且参考来源均为宏观电商统计，未覆盖此微观分解逻辑。 | 逻辑上GMV=价格*数量自洽，但参考来源[1][2][3]仅涉及宏观GMV统计趋势，与该具体分解公式及数据获取需求无关，属经验事实且缺来源支持。

## Search Query

e-commerce GMV baseline data recent 90 days

## Retrieval Sources

- {'url': 'https://www.opensend.com/post/gross-merchandise-volume-ecommerce&rut=542435000a21b1c02028b1bd1a95435903b4edfdb479fad2198503e57bc1f3b8', 'type': 'ddg', 'title': '7 Gross Merchandise Volume (GMV) Statistics For eCommerce Stores'}
- {'url': 'https://ecomranker.com/ecommerce-statistics/&rut=9ef69537ebd97b72d3c8be9ac82ed75cb8735f05478e153ede8853afc530ed5c', 'type': 'ddg', 'title': 'Ecommerce Statistics : Key Trends & Data | EcomRanker'}
- {'url': 'https://www.koongo.com/blog/ecommerce-statistics-2026/&rut=78ef55c099643fd74fe92ef0f0ab7a7db0e0fd9921c54b3636bcedcda7ba0975', 'type': 'ddg', 'title': 'Ecommerce Statistics (2026): 80+ Data Points on Market Size, Growth ...'}

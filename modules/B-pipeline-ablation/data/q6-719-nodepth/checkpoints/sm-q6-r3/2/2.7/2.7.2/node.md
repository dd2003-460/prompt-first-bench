# N88: 公有云 CDN 的日志存储成本 (C_log, ¥/1000 req) 计算为 (V_log * Retention_Days * Unit_Price_log

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N18

## Claim

公有云 CDN 的日志存储成本 (C_log, ¥/1000 req) 计算为 (V_log * Retention_Days * Unit_Price_log) / Q_day_total * 1000，其中 V_log 为日均日志生成量（GB，通常约为下载流量的 1-5%），Retention_Days 为日志保留天数（通常 30-90 天），Unit_Price_log 为日志存储单价（¥/GB/月）。

## Corrected Claim

公有云 CDN 的日志存储成本 (C_log, ¥/1000 req) 计算为 (V_log * (Retention_Days / 30) * Unit_Price_log) / Q_day_total * 1000，其中 V_log 为日均日志生成量（GB），Retention_Days 为日志保留天数，Unit_Price_log 为日志存储单价（¥/GB/月）。

## Evidence

[质询]公式中 Unit_Price_log 的单位为 ¥/GB/月，而 Retention_Days 为天数，直接相乘会导致量纲错误（应为 ¥/GB/天 或需除以 30 进行换算）；此外，'日志量约为下载流量的 1-5%' 属于经验估算值，不同业务场景差异巨大，缺乏普适性。 | 来源 [3] 提供了日志计费的具体案例（1亿请求/9.31GB/15天），间接支持了日志存储计费的逻辑框架，但未直接支持该特定公式及 1-5% 的经验比例；公式存在量纲不匹配问题（月单价 vs 天数），需修正。

## Search Query

Alibaba Cloud CDN log storage pricing per GB per month

## Retrieval Sources

- {'url': 'https://cloud.google.com/cdn/pricing?hl=zh-cn&rut=74fac12a2c12ad0f3ff9712259e6fb7f4eb556c23cf368ae2dd79e79f2660348', 'type': 'ddg', 'title': 'Cloud CDN 价格 | Google Cloud'}
- {'url': 'https://developer.cloud.tencent.cn/article/2360627&rut=4ca5cacbfdbf06d130d43250c9f9c700f241192d1ba2f1b00f7b5976801dd2fe', 'type': 'ddg', 'title': '日志费用计算-腾讯云开发者社区-腾讯云'}
- {'url': 'https://cloud.tencent.com/document/product/614/78045&rut=5b42218b5ad1243304f831d2180e11774621195a425157e0df434cbaffc9f2b5', 'type': 'ddg', 'title': '日志服务 按量计费示例_腾讯云'}

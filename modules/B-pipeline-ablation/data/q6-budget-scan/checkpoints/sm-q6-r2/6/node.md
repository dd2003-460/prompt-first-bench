# N33: 公有云 CDN 基础监控与日志服务的订阅成本约为 ¥500-¥2000/月/节点（或按日志量计费 ¥0.01-0.05/GB），而自建节点需采购 Zabbix/

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

公有云 CDN 基础监控与日志服务的订阅成本约为 ¥500-¥2000/月/节点（或按日志量计费 ¥0.01-0.05/GB），而自建节点需采购 Zabbix/Prometheus 集群，初始软件授权或开源维护人力成本约为 ¥20,000/年/节点

## Corrected Claim

公有云 CDN 基础监控与日志服务的订阅成本通常按日志量或节点数计费（具体价格因厂商和套餐而异，常见量级为数百至数千元/月/节点或按GB计费），而自建节点需采购 Zabbix/Prometheus 集群，初始软件授权或开源维护人力成本约为 ¥20,000/年/节点。

## Evidence

[质询]参考来源仅涵盖阿里云CDN的基础流量/带宽计费，完全未提及“基础监控与日志服务”的具体订阅价格（¥500-2000/月）或日志单价（¥0.01-0.05/GB），也未涉及自建监控集群的成本数据，属于经验事实且缺乏来源支持。 | 来源[1][2][3]仅描述CDN基础流量计费，未覆盖监控/日志服务及自建成本，无法提供直接支持；该陈述为经验事实，逻辑自洽但缺来源支持。

## Retrieval Sources

- {'url': 'https://developer.aliyun.com/article/1708278&rut=2ddc55f04c3ee490ae5b44019f150c2428eac2400670b83d41207aae16acf9e2', 'type': 'ddg', 'title': '2026最新阿里云cdn收费标准：不同计费模式价格表（基础服务费和增值服务费用整理）-阿里云开发者社区'}
- {'url': 'https://help.aliyun.com/zh/cdn/product-overview/billing-overview&rut=5607cac578e6a0a2822f10843ed70c58160107634276405ba09db4d9580720b7', 'type': 'ddg', 'title': 'Cdn如何计费-cdn (Cdn)-阿里云帮助中心'}
- {'url': 'https://help.aliyun.com/zh/cdn/product-overview/billing-rules-of-basic-services&rut=8ac269fc0fd33361b507140bc77f95e7de5882f95004416a424fe1397b02bd86', 'type': 'ddg', 'title': '基础服务计费方式定价规则-cdn-阿里云-cdn (Cdn)-阿里云帮助中心'}

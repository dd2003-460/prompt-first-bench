# N196: 阿里云日志服务（SLS）写入与存储成本量化：SLS按写入数据量（Write Size）和存储数据量（Storage Size）计费。写入单价约¥0.4/GB（压

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N71, N72, N74

## Claim

阿里云日志服务（SLS）写入与存储成本量化：SLS按写入数据量（Write Size）和存储数据量（Storage Size）计费。写入单价约¥0.4/GB（压缩后），存储单价约¥0.0035/GB/天。日均2TB流量，假设日志压缩比1:3，实际写入量≈666GB/天。月度写入成本=666GB×30×¥0.4=¥8,000。若日志保留30天，平均存储量≈10TB，月度存储成本=10,000GB×¥0.0035×30=¥1,050。月度总日志成本≈¥9,050，年度成本≈¥108,600。

## Corrected Claim

阿里云SLS按写入数据量（原始大小）计费，写入单价约¥0.4/GB。日均2TB流量，月度写入成本=2000GB×30×¥0.4=¥24,000。若日志保留30天，存储费用为0（因享有30天免费存储周期）。月度总日志成本≈¥24,000。

## Evidence

[质询]计费口径与免费存储期逻辑矛盾：来源明确指出SLS按写入数据量（原始大小）计费，且写入数据享有30天免费存储周期。陈述中假设日志保留30天并计算了存储成本，这与来源中'30天内存储免费'的事实直接矛盾；此外，陈述声称按'压缩后'大小计费，而来源强调按'原始大小'计费，存在计费基数错误。 | 来源[1]和[3]明确指出SLS按写入数据量（原始大小）计费，且30天内存储免费，与陈述中按压缩后计费及30天保留产生存储成本的描述矛盾。

## Search Query

Alibaba Cloud SLS pricing write size storage cost per GB

## Retrieval Sources

- {'url': 'https://help.aliyun.com/zh/sls/billing-per-amount-of-data-written&rut=ea4ee3fd309adcca5cf36e9a02ae6ea3bd0fa6415df2c90513ea78f787c62407', 'type': 'ddg', 'title': '日志服务按写入数据量计费-日志服务 (Sls)-阿里云帮助中心'}
- {'url': 'https://help.aliyun.com/zh/sls/billing-overview&rut=993aeaf78ff7c9ddca9d60e5210fad0dce0e30b238ba8e01e264b92b7569bc16', 'type': 'ddg', 'title': '日志服务的计费方式、计费组成、计费周期-日志服务 (Sls)-阿里云帮助中心'}
- {'url': 'https://www.alibabacloud.com/help/zh/sls/billing-per-amount-of-data-written&rut=08a4eda771c3432bf67c56f5e5505db7cbe02ab5b8144d745645aae6a8fcfa6c', 'type': 'ddg', 'title': '日志服务按写入数据量计费 - 日志服务 - 阿里云'}

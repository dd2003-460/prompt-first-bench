# N195: 阿里云CDN自定义告警规则成本结构：阿里云云监控基础服务免费，但自定义告警规则若使用企业级通知渠道（如短信、电话）或高级逻辑组合，部分高级功能可能按次计费；然而

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N71, N72, N74

## Claim

阿里云CDN自定义告警规则成本结构：阿里云云监控基础服务免费，但自定义告警规则若使用企业级通知渠道（如短信、电话）或高级逻辑组合，部分高级功能可能按次计费；然而，仅配置规则本身不产生直接费用，主要成本在于关联的日志服务（SLS）或函数计算（FC）触发成本。若仅使用基础Webhook，边际成本≈0。

## Corrected Claim

阿里云CDN自定义告警规则基于云监控服务，基础规则配置通常不产生直接费用；具体通知渠道（如短信、电话）及关联服务（如SLS、FC）的成本需依据阿里云最新计费文档确认，基础Webhook通知通常边际成本极低。

## Evidence

[质询]陈述中关于“企业级通知渠道（如短信、电话）按次计费”以及“主要成本在于关联的日志服务（SLS）或函数计算（FC）”属于具体的计费策略和经验性成本结构描述，参考来源仅涵盖功能介绍，未提供计费细节，无法排除阿里云云监控基础版短信/电话通知是否免费或是否有免费额度，也无法确认CDN告警是否必然关联SLS/FC产生主要成本。 | 来源[1][2][3]仅确认了CDN报警规则的功能和创建流程，未涉及具体计费模式（如短信是否收费、SLS/FC是否为主要成本源），属于经验事实且缺乏直接来源支持，逻辑上自洽但无法通过现有来源验证具体计费细节。

## Search Query

Alibaba Cloud CDN custom alert rules cost free tier

## Retrieval Sources

- {'url': 'https://help.aliyun.com/zh/cdn/user-guide/set-an-alert-rule&rut=7f5ca0b765d189a0f85580702c6418ffb32dbe26042d3da7484fc66f93d11170', 'type': 'ddg', 'title': '创建cdn报警规则-cdn (Cdn)-阿里云帮助中心'}
- {'url': 'https://www.alibabacloud.com/help/zh/cdn/user-guide/set-an-alert-rule&rut=9462fd30a845d17a188f3531030d184469c187e9ad834c622a5b39e1a60b4d6f', 'type': 'ddg', 'title': '创建CDN报警规则 - CDN - 阿里云 - Alibaba Cloud'}
- {'url': 'https://www.alibabacloud.com/help/zh/cms/cloudmonitor-1-0/user-guide/custom-monitoring/&rut=bfc1c11874e7d187fdb731adc9204a4da09905a659d69cacc2cffc1da3980a69', 'type': 'ddg', 'title': '自定义监控概览 - 云监控 - 阿里云 - Alibaba Cloud'}

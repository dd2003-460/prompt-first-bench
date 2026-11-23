# N327: 公有云 CDN 上传流量计费策略边界：主流公有云（阿里云/腾讯云/Cloudflare）通常对上传流量（Ingress）免费或包含在基础套餐中，但若触发回源或跨

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N111

## Claim

公有云 CDN 上传流量计费策略边界：主流公有云（阿里云/腾讯云/Cloudflare）通常对上传流量（Ingress）免费或包含在基础套餐中，但若触发回源或跨域同步，可能按 ¥0.1-0.3/GB 计费；需确认具体供应商的 'Upload Traffic' 定义是否包含 CDN 节点间的内部传输。

## Corrected Claim

主流公有云（阿里云/腾讯云/Cloudflare）通常对上传流量（Ingress）免费或包含在基础套餐中，但具体计费策略（包括是否对回源或跨域同步收费及具体单价）因供应商、区域和套餐而异，需查阅各供应商最新官方定价文档确认。

## Evidence

[质询]具体计费数值（¥0.1-0.3/GB）属于经验事实，不同供应商、不同区域及不同套餐下的价格波动较大，且'通常免费'的概括可能忽略部分按量付费场景下的Ingress收费情况，缺乏具体来源支持该特定数值区间。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

Alibaba Cloud CDN upload traffic pricing free ingress cost 2024

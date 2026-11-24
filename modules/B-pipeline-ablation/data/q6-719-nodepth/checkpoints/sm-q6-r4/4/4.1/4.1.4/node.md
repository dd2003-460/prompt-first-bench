# N80: 公有云CDN合同等级带宽上限：阿里云CDN基础版单租户峰值带宽上限为100Gbps，企业版可达500Gbps，旗舰版1Tbps；Cloudflare Pro/E

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N19, N20, N21

## Claim

公有云CDN合同等级带宽上限：阿里云CDN基础版单租户峰值带宽上限为100Gbps，企业版可达500Gbps，旗舰版1Tbps；Cloudflare Pro/Enterprise无硬上限但受网络容量限制，实际峰值通常<100Gbps

## Corrected Claim

阿里云CDN支持按峰值带宽计费，具体单租户带宽上限需根据实际业务场景及与阿里云签订的SLA协议确定，公开文档未明确列出基础版/企业版/旗舰版的固定带宽上限数值；Cloudflare Pro/Enterprise计划通常无固定硬上限，但受网络容量及公平使用政策限制。

## Evidence

[质询]阿里云CDN官方文档及定价页面通常不公开具体的“单租户峰值带宽硬上限”数值（如100Gbps/500Gbps/1Tbps），这些数值可能来自非公开的SLA协议、特定大客户合同或过时/错误的内部资料，且“基础版/企业版/旗舰版”并非阿里云CDN当前标准的公开产品分级命名（通常按计费方式或功能模块区分），存在口径混淆和来源不可靠的风险。 | 参考来源[1][2][3]仅涉及阿里云CDN的计费方式（按流量/带宽峰值），未提及任何关于单租户带宽上限的具体数值或产品版本分级，无法支持该经验事实；Cloudflare部分亦无来源支持。

## Search Query

Alibaba Cloud CDN bandwidth limit per tenant 100Gbps 500Gbps contract tier

## Retrieval Sources

- {'url': 'https://www.aliyun.com/price/detail/cdn&rut=7deffc4f1d34859bcb7594b9f5ea62952b3f14c06ecc370a5099c3c282977b06', 'type': 'ddg', 'title': '阿里云定价_CDN价格详情'}
- {'url': 'https://help.aliyun.com/zh/cdn/product-overview/billing-rules-of-basic-services&rut=8ac269fc0fd33361b507140bc77f95e7de5882f95004416a424fe1397b02bd86', 'type': 'ddg', 'title': '基础服务计费方式定价规则-cdn-阿里云-cdn (Cdn)-阿里云帮助中心'}
- {'url': 'https://www.alibabacloud.com/help/zh/cdn/product-overview/billing-rules-of-basic-services&rut=589eb8bcf36cfde37a373f8a90296011419e64ee1604f3c6bbc7e6c19a919106', 'type': 'ddg', 'title': '基础服务计费 - CDN - 阿里云 - Alibaba Cloud'}

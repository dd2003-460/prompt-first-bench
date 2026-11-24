# N228: 公有云CDN回源流量单价 Unit_Price_Source_Pub 的量化取值：阿里云/Cloudflare 回源流量通常按公网下行流量计费或享受折扣，需确认

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N67

## Claim

公有云CDN回源流量单价 Unit_Price_Source_Pub 的量化取值：阿里云/Cloudflare 回源流量通常按公网下行流量计费或享受折扣，需确认具体单价（如阿里云 ¥0.24/GB 或 Cloudflare 免费回源额度内的 $0/GB），此参数直接决定成本差异的量级

## Corrected Claim

公有云CDN回源流量通常按公网下行流量计费或享受折扣，具体单价需查询各云厂商最新价目表（如阿里云、Cloudflare等），此参数直接决定成本差异的量级。

## Evidence

[质询]具体数值（如阿里云 ¥0.24/GB）属于经验事实且可能随时间/区域变动，参考来源中未提供该具体单价，仅说明了计费模式（按公网下行或回源流量），无法直接验证具体金额。 | 来源[3]支持'回源流量按公网下行流量计费'的逻辑，但所有来源均未提供具体的单价数值（如¥0.24/GB），属于经验事实缺来源直接支持。

## Search Query

Alibaba Cloud CDN origin traffic pricing 2024 vs Cloudflare origin egress cost

## Retrieval Sources

- {'url': 'https://help.aliyun.com/zh/cdn/product-overview/billing-of-oss-content-acceleration&rut=d489a658be3e4f065943b8be8074ff4503e553f35415f3dd0264563cb68045cd', 'type': 'ddg', 'title': 'Cdn加速oss计费说明-cdn (Cdn)-阿里云帮助中心'}
- {'url': 'https://support.huaweicloud.com/price-cdn/cdn_01_0158.html&rut=f8f980b6285c6d43ebbd31db9975bd9a1e180a79a02bc1b57e1bc4d059186f01', 'type': 'ddg', 'title': '流量计费_基础服务计费_计费说明_内容分发网络 Cdn-华为云'}
- {'url': 'https://www.ctyun.cn/document/10306929/10323667&rut=2ed01b82703c8bf58b479e3dd6206c2a9e5f34a1661992e30d6aff496ab09843', 'type': 'ddg', 'title': 'Cdn回源的流量为什么按照公网下行流量计费了 - 天翼云'}

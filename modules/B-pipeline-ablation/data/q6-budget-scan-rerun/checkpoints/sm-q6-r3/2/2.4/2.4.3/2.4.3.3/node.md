# N213: 阿里云 CDN 与 Cloudflare Pro 在回源流量（Origin Fetch）计费上的差异量化：阿里云回源流量通常免费或极低（如 ¥0.05/GB 或

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N61

## Claim

阿里云 CDN 与 Cloudflare Pro 在回源流量（Origin Fetch）计费上的差异量化：阿里云回源流量通常免费或极低（如 ¥0.05/GB 或包含在流量包内），而 Cloudflare 回源流量可能按 $0.05-0.10/GB 单独计费或包含在套餐内，需计算日均 100GB-200GB 回源流量在两种模式下的月度成本差值

## Corrected Claim

阿里云 CDN 与 Cloudflare Pro 在回源流量计费模式上存在差异：阿里云通常对回源流量免费或收取较低费用，而 Cloudflare 可能根据套餐不同对回源流量进行单独计费或包含在套餐内，需根据具体日均回源流量（如 100GB-200GB）及最新官方定价计算月度成本差值。

## Evidence

[质询]具体计费数值（阿里云¥0.05/GB、Cloudflare $0.05-0.10/GB）属于经验事实，且Cloudflare Pro套餐通常包含回源流量或按不同标准计费，直接引用具体单价缺乏来源支持且可能不准确。 | 参考来源仅涉及回源协议配置，未提供计费数据；该陈述包含具体价格参数，属经验事实，逻辑自洽但缺来源直接支持，故降级。

## Search Query

Aliyun CDN origin fetch traffic cost vs Cloudflare origin pull pricing

## Retrieval Sources

- {'url': 'https://help.aliyun.com/zh/cdn/user-guide/configure-the-origin-protocol-policy&rut=4baef1adb7dd1b83d4369934f8a144f112cf8f0f69bf80074bd4949b646eddf0', 'type': 'ddg', 'title': '配置cdn节点以https协议回源-cdn (Cdn)-阿里云帮助中心'}
- {'url': 'https://www.alibabacloud.com/help/zh/cdn/user-guide/configure-the-origin-protocol-policy&rut=e72b436a278e90b68b79cdf12e67b5a948ea4cf41bf2929f25082e2fb0de096f', 'type': 'ddg', 'title': '配置CDN节点以HTTPS协议回源 - CDN - 阿里云 - Alibaba Cloud'}
- {'url': 'https://help.aliyun.com/zh/cdn/user-guide/back-to-origin-routing-overview&rut=20633cece0fbe52a15f7fee9304351ff523666b1d4364ce9d8be48273bb89dbe', 'type': 'ddg', 'title': '什么是回源及支持的回源配置功能-cdn (Cdn)-阿里云帮助中心'}

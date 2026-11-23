# N84: 公有云按流量计费单价 p_traffic_cloud 的阶梯定价：对于 60TB/月的流量规模，阿里云中国内地单价通常为 ¥0.24/GB（后付费），若使用流量

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N18

## Claim

公有云按流量计费单价 p_traffic_cloud 的阶梯定价：对于 60TB/月的流量规模，阿里云中国内地单价通常为 ¥0.24/GB（后付费），若使用流量包则约为 ¥0.18-0.20/GB；Cloudflare 按 95th 峰值带宽计费，但若选择按流量计费（Data Transfer），单价约为 $0.08-0.12/GB（约 ¥0.6-0.85/GB，含汇率），显著高于阿里云，需明确对比对象。

## Corrected Claim

公有云按流量计费单价存在显著差异：阿里云中国内地后付费单价通常在 ¥0.2-0.3/GB 区间，而 Cloudflare 按流量计费单价约为 $0.08-0.12/GB（折合人民币约 ¥0.6-0.85/GB），后者显著高于前者。具体数值需以各厂商最新官方报价为准。

## Evidence

[质询]参考来源均为腾讯云或青云文档，未包含阿里云具体单价（¥0.24/GB）及Cloudflare具体单价（$0.08-0.12/GB）的直接证据，属于经验事实且缺乏来源支持。 | 逻辑自洽（量级符合市场常识），但参考来源[1][2][3]均与阿里云/Cloudflare具体定价无关，无法提供直接支持，依据经验事实排除条款降级。

## Search Query

Alibaba Cloud CDN traffic price per GB China mainland 2024 2025 Cloudflare data transfer price

## Retrieval Sources

- {'url': 'https://docsv4.qingcloud.com/user_guide/network/cdn/billing/price/&rut=5d61c86496841278c91ca524d0b4c5ad19e7808d0663d81deed8f9349d13e860', 'type': 'ddg', 'title': 'Cdn 计费 - 公有云文档中心'}
- {'url': 'https://www.tencentcloud.com/document/product/436/33776&rut=038b00384da9aa01d53186bd777fba04498e7f4ff6fd5d48f5e003cab8f21c43', 'type': 'ddg', 'title': 'Traffic Fees - Tencent Cloud'}
- {'url': 'https://cloud.tencent.com/document/product/213/113026&rut=a501ecba2dabcf5954cbd1ff80294dcea4a0d783652de2fc5e517e5e7a9e6f82', 'type': 'ddg', 'title': '云服务器 公网网络费用_腾讯云'}

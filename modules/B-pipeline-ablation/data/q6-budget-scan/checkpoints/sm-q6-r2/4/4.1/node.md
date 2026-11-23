# N17: 公有云 CDN 按流量计费单价：阿里云/Cloudflare 图片+短视频混合流量的阶梯计费单价（¥/GB），需区分国内/海外及带宽峰值计费模式下的等效单价。

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4

## Claim

公有云 CDN 按流量计费单价：阿里云/Cloudflare 图片+短视频混合流量的阶梯计费单价（¥/GB），需区分国内/海外及带宽峰值计费模式下的等效单价。

## Corrected Claim

公有云 CDN（如阿里云）通常采用按流量阶梯计费模式，价格随流量阶梯累进并区分国内/海外地域；具体单价需查阅最新官方价格表，带宽峰值计费模式下的等效单价需根据实际业务流量模型换算。

## Evidence

[质询]陈述要求提供具体的阶梯计费单价数值（¥/GB）及带宽峰值等效单价，但参考来源仅提供了计费模式的描述（按流量、阶梯累进、区分地域），未包含具体的价格数值表，且未提及Cloudflare的具体单价，导致无法从来源中直接提取或验证具体数值。 | 来源[2]和[3]确认了阿里云CDN采用按流量阶梯计费且区分地域，逻辑自洽，但缺乏具体数值支持，属于经验事实且缺来源直接支持。

## Search Query

Alibaba Cloud CDN pricing per GB traffic 2024 Cloudflare bandwidth cost

## Retrieval Sources

- {'url': 'https://help.aliyun.com/zh/cdn/product-overview/billing-overview&rut=5607cac578e6a0a2822f10843ed70c58160107634276405ba09db4d9580720b7', 'type': 'ddg', 'title': 'Cdn如何计费-cdn (Cdn)-阿里云帮助中心'}
- {'url': 'https://developer.aliyun.com/article/1708278&rut=2ddc55f04c3ee490ae5b44019f150c2428eac2400670b83d41207aae16acf9e2', 'type': 'ddg', 'title': '2026最新阿里云cdn收费标准：不同计费模式价格表（基础服务费和增值服务费用整理）-阿里云开发者社区'}
- {'url': 'https://developer.aliyun.com/article/1712489&rut=9ac11fc059ec63ddd1ce104c3b0e7d9ac1b1e8c3823c8a667dafda6ca3e1bda1', 'type': 'ddg', 'title': '2026阿里云cdn 计费全攻略：按流量 / 带宽 / 95 峰值 + 基础服务费 + 增值服务价格表'}

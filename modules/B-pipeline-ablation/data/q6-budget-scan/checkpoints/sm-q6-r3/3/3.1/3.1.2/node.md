# N81: 公有云CDN阶梯计价修正系数：当月计费流量超过1TB时，阿里云/Cloudflare通常适用第二阶梯单价¥0.15-0.25/GB；超过5TB时适用第三阶梯单价

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N19

## Claim

公有云CDN阶梯计价修正系数：当月计费流量超过1TB时，阿里云/Cloudflare通常适用第二阶梯单价¥0.15-0.25/GB；超过5TB时适用第三阶梯单价¥0.10-0.20/GB；本场景日均2TB下载若未命中缓存则月流量约60TB，必然触发最高阶梯

## Corrected Claim

公有云CDN（如阿里云）采用当月流量阶梯累进计价模式，流量越大单价越低。本场景日均2TB下载若未命中缓存则月流量约60TB，必然触发较高流量阶梯，享受较低单价（具体单价需查阅当期官方价格表，通常远低于首阶梯单价）。

## Evidence

[质询]具体数值（¥0.15-0.25/GB 和 ¥0.10-0.20/GB）及阶梯阈值（1TB/5TB）属于经验事实，参考来源仅确认了“阶梯计价”机制，未提供具体价格表数值，且阿里云实际价格随地域和时期波动，无法从来源直接验证具体金额。 | 来源[1][3]确认阿里云CDN采用“当月按账户维度进行阶梯累进”的计费模式，支持“阶梯计价”这一逻辑前提；但具体单价数值在来源摘要中缺失，属于经验事实，逻辑自洽但缺来源直接支持具体数值。

## Search Query

Alibaba Cloud CDN pricing tier 2024 5TB threshold Cloudflare bandwidth pricing tier

## Retrieval Sources

- {'url': 'https://developer.aliyun.com/article/1708278&rut=2ddc55f04c3ee490ae5b44019f150c2428eac2400670b83d41207aae16acf9e2', 'type': 'ddg', 'title': '2026最新阿里云cdn收费标准：不同计费模式价格表（基础服务费和增值服务费用整理）-阿里云开发者社区'}
- {'url': 'https://help.aliyun.com/zh/cdn/product-overview/billing-overview&rut=5607cac578e6a0a2822f10843ed70c58160107634276405ba09db4d9580720b7', 'type': 'ddg', 'title': 'Cdn如何计费-cdn (Cdn)-阿里云帮助中心'}
- {'url': 'https://developer.aliyun.com/article/1712489&rut=9ac11fc059ec63ddd1ce104c3b0e7d9ac1b1e8c3823c8a667dafda6ca3e1bda1', 'type': 'ddg', 'title': '2026阿里云cdn 计费全攻略：按流量 / 带宽 / 95 峰值 + 基础服务费 + 增值服务价格表'}

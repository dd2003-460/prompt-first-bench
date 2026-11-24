# N30: 公有云CDN阶梯计费阈值：阿里云/Cloudflare 通常设置带宽阶梯（如 0-10Gbps, 10-100Gbps），不同区间单价差异可达 20-30%；需

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

公有云CDN阶梯计费阈值：阿里云/Cloudflare 通常设置带宽阶梯（如 0-10Gbps, 10-100Gbps），不同区间单价差异可达 20-30%；需根据峰值带宽 69.3Gbps 定位所在阶梯区间，并应用对应单价 P_bw_tier 计算月度带宽成本，避免使用平均单价导致的低估。

## Corrected Claim

公有云CDN（如阿里云）通常采用阶梯计费模式（按流量或带宽峰值），不同用量区间单价不同；需根据实际峰值带宽或流量定位所在阶梯区间，应用对应单价计算成本，避免使用平均单价导致估算偏差。

## Evidence

[质询]陈述中关于“不同区间单价差异可达 20-30%”的具体数值缺乏来源支持，且阿里云CDN按流量计费通常采用累进阶梯（边际定价），而非简单的固定带宽区间（如0-10Gbps）对应固定单价，具体阶梯划分和价差需依据最新官方价目表，不能仅凭通用经验断定。 | 来源[1][2][3]证实阿里云CDN存在阶梯计费机制（按流量或带宽峰值），支持“需定位阶梯区间”的逻辑，但未提供具体的阶梯阈值（如10Gbps/100Gbps）及20-30%的具体价差数据，属于经验事实缺具体来源支持。

## Retrieval Sources

- {'url': 'https://developer.aliyun.com/article/1708278&rut=2ddc55f04c3ee490ae5b44019f150c2428eac2400670b83d41207aae16acf9e2', 'type': 'ddg', 'title': '2026最新阿里云cdn收费标准：不同计费模式价格表（基础服务费和增值服务费用整理）-阿里云开发者社区'}
- {'url': 'https://developer.aliyun.com/article/1712489&rut=9ac11fc059ec63ddd1ce104c3b0e7d9ac1b1e8c3823c8a667dafda6ca3e1bda1', 'type': 'ddg', 'title': '2026阿里云cdn 计费全攻略：按流量 / 带宽 / 95 峰值 + 基础服务费 + 增值服务价格表-阿里云开发者社区'}
- {'url': 'https://www.alibabacloud.com/help/zh/cdn/product-overview/billing-rules-of-basic-services&rut=589eb8bcf36cfde37a373f8a90296011419e64ee1604f3c6bbc7e6c19a919106', 'type': 'ddg', 'title': '基础服务计费 - CDN - 阿里云 - Alibaba Cloud'}

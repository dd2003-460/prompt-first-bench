# N140: 公有云CDN按带宽计费模式下，混合策略中公有云部分的月固定带宽成本 C_bw_bandwidth = B_peak_cloud * P_bw_gbps_mont

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N40

## Claim

公有云CDN按带宽计费模式下，混合策略中公有云部分的月固定带宽成本 C_bw_bandwidth = B_peak_cloud * P_bw_gbps_month，其中 B_peak_cloud = (1-α) * B_peak_total，P_bw_gbps_month 为阿里云按带宽计费单价（基准值 ¥100-200/月/Mbps，需核验具体档位）。

## Corrected Claim

公有云CDN按带宽计费模式下，混合策略中公有云部分的月固定带宽成本 C_bw_bandwidth = B_peak_cloud * P_bw_gbps_month，其中 B_peak_cloud = (1-α) * B_peak_total，P_bw_gbps_month 为阿里云按带宽计费单价（具体数值需根据地域和带宽阶梯查询阿里云官方价目表）。

## Evidence

[质询]陈述中给出的具体单价基准值（¥100-200/月/Mbps）属于经验事实，参考来源仅确认了计费模式的存在（按带宽峰值计费），但未提供具体的价格数值，无法直接验证该数值量级是否准确（实际阿里云CDN带宽价格通常随地域和带宽阶梯变化，且单位常为元/GB或元/Mbps/月，具体数值需查最新价目表，此处数值可能偏高或偏低，且未区分地域）。 | 来源[1]和[3]确认阿里云CDN支持‘按带宽峰值计费’模式，逻辑上公式 C = B_peak * P 成立；但来源未提供具体单价数值，且该数值为经验事实，缺乏直接来源支持，故降级。

## Search Query

阿里云 CDN 按带宽计费 价格 Mbps 月 2024 2025

## Retrieval Sources

- {'url': 'https://help.aliyun.com/zh/cdn/product-overview/billing-overview&rut=5607cac578e6a0a2822f10843ed70c58160107634276405ba09db4d9580720b7', 'type': 'ddg', 'title': 'Cdn如何计费-cdn (Cdn)-阿里云帮助中心'}
- {'url': 'https://developer.aliyun.com/article/1712489&rut=9ac11fc059ec63ddd1ce104c3b0e7d9ac1b1e8c3823c8a667dafda6ca3e1bda1', 'type': 'ddg', 'title': '2026阿里云cdn 计费全攻略：按流量 / 带宽 / 95 峰值 + 基础服务费 + 增值服务价格表-阿里云开发者社区'}
- {'url': 'https://help.aliyun.com/zh/cdn/product-overview/billing-rules-of-basic-services&rut=8ac269fc0fd33361b507140bc77f95e7de5882f95004416a424fe1397b02bd86', 'type': 'ddg', 'title': '基础服务计费方式定价规则-cdn-阿里云-cdn (Cdn)-阿里云帮助中心'}

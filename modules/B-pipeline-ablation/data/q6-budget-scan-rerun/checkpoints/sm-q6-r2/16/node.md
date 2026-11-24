# N190: 带宽超量惩罚与阶梯定价细节：公有云 CDN 带宽成本中，若月流量超过承诺量（如 5TB），超出部分单价上浮 20-30%；自建节点中，ISP 专线通常采用 95

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

带宽超量惩罚与阶梯定价细节：公有云 CDN 带宽成本中，若月流量超过承诺量（如 5TB），超出部分单价上浮 20-30%；自建节点中，ISP 专线通常采用 95th Percentile 计费，峰值带宽超限可能触发高额罚款或强制限速，需预留 20% 带宽冗余以规避此风险。

## Corrected Claim

公有云 CDN 带宽成本通常采用阶梯定价或按量计费模式，流量越大单价可能越低或按阶梯累进；自建节点中，ISP 专线通常采用 95th Percentile 计费，峰值带宽超限可能触发高额费用或限速，建议预留带宽冗余以规避风险。

## Evidence

[质询]陈述中关于公有云CDN“月流量超过承诺量（如5TB）超出部分单价上浮20-30%”的具体数值和机制缺乏来源支持，且与阿里云等主流公有云CDN通常采用的“阶梯累进”或“按量付费”模式描述不完全一致（来源显示为阶梯价格，但未提及基于承诺量的固定上浮比例）；自建节点ISP专线的95th Percentile计费及20%冗余建议属于行业经验，但具体罚款/限速细节未在来源中体现。 | 来源[1]和[3]确认了阿里云CDN采用“阶梯价格计费”和“95峰值”计费模式，间接支持了存在阶梯定价和峰值计费的事实，但未直接支持“超出承诺量上浮20-30%”这一具体经验参数，故降级为定性表述。

## Retrieval Sources

- {'url': 'https://developer.aliyun.com/article/1712489&rut=9ac11fc059ec63ddd1ce104c3b0e7d9ac1b1e8c3823c8a667dafda6ca3e1bda1', 'type': 'ddg', 'title': '2026阿里云cdn 计费全攻略：按流量 / 带宽 / 95 峰值 + 基础服务费 + 增值服务价格表-阿里云开发者社区'}
- {'url': 'https://help.aliyun.com/zh/cdn/product-overview/billing-overview&rut=5607cac578e6a0a2822f10843ed70c58160107634276405ba09db4d9580720b7', 'type': 'ddg', 'title': 'Cdn如何计费-cdn (Cdn)-阿里云帮助中心'}
- {'url': 'https://developer.aliyun.com/article/1708278&rut=2ddc55f04c3ee490ae5b44019f150c2428eac2400670b83d41207aae16acf9e2', 'type': 'ddg', 'title': '2026最新阿里云cdn收费标准：不同计费模式价格表（基础服务费和增值服务费用整理）-阿里云开发者社区'}

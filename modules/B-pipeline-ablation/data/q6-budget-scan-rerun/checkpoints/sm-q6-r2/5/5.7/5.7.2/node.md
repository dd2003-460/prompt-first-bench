# N117: 公有云CDN流量单价与阶梯结构：阿里云/Cloudflare按GB计费，单价¥0.2-0.5/GB（中国内地），阶梯递减（如0-10TB、10-50TB、50-

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N37

## Claim

公有云CDN流量单价与阶梯结构：阿里云/Cloudflare按GB计费，单价¥0.2-0.5/GB（中国内地），阶梯递减（如0-10TB、10-50TB、50-100TB不同单价），日均2TB下载=月均60TB，需量化60TB/月对应的实际阶梯单价及月度总成本

## Corrected Claim

公有云CDN（如阿里云）通常采用按GB阶梯计费模式，当月流量越大单价越低（阶梯累进）。具体单价需查询最新官方价格表，日均2TB下载对应月均约60TB流量，需根据60TB所在阶梯区间计算月度总成本。

## Evidence

[质询]具体单价数值（¥0.2-0.5/GB）及阶梯区间（0-10TB等）属于经验事实，参考来源仅确认了“按GB阶梯计费”的机制，未提供具体的2026年最新价格表数值，无法直接验证该具体价格区间是否准确（阿里云CDN价格随时间波动，且不同地域/资源包价格差异大）。 | 来源[1][2]直接支持“阿里云CDN按GB阶梯计费”的机制描述，但未提供具体单价数值；该节点包含具体价格参数，属经验事实，逻辑自洽但缺来源直接支持具体数值，故降级。

## Search Query

Alibaba Cloud CDN pricing per GB tier 2024 China

## Retrieval Sources

- {'url': 'https://developer.aliyun.com/article/1708278&rut=2ddc55f04c3ee490ae5b44019f150c2428eac2400670b83d41207aae16acf9e2', 'type': 'ddg', 'title': '2026最新阿里云cdn收费标准：不同计费模式价格表（基础服务费和增值服务费用整理）-阿里云开发者社区'}
- {'url': 'https://developer.aliyun.com/article/1712489&rut=9ac11fc059ec63ddd1ce104c3b0e7d9ac1b1e8c3823c8a667dafda6ca3e1bda1', 'type': 'ddg', 'title': '2026阿里云cdn 计费全攻略：按流量 / 带宽 / 95 峰值 + 基础服务费 + 增值服务价格表'}
- {'url': 'https://www.aliyun.com/price/detail/cdn&rut=7deffc4f1d34859bcb7594b9f5ea62952b3f14c06ecc370a5099c3c282977b06', 'type': 'ddg', 'title': '阿里云定价_CDN价格详情'}

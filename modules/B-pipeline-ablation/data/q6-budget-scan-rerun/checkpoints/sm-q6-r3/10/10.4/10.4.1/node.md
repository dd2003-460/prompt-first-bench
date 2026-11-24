# N397: 公有云CDN预热带宽的阶梯计费影响：当日均预热流量2GB叠加基础流量60TB/月后，总流量60.06TB仍落在¥0.18/GB阶梯区间，边际成本不变；但若预热导

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N138

## Claim

公有云CDN预热带宽的阶梯计费影响：当日均预热流量2GB叠加基础流量60TB/月后，总流量60.06TB仍落在¥0.18/GB阶梯区间，边际成本不变；但若预热导致流量跨入更高阶梯（如超过61TB），边际单价可能降至¥0.16/GB，需量化阶梯边界对预热成本的影响

## Corrected Claim

公有云CDN（如阿里云）采用按流量阶梯计费模式。当日均预热流量叠加基础流量后，若总流量未跨越阶梯边界，边际成本保持不变；若跨越边界进入更高流量区间，边际单价通常会降低（具体数值需查阅最新官方价格表），需量化阶梯边界对预热成本的影响。

## Evidence

[质询]陈述中引用的具体阶梯价格数值（¥0.18/GB 和 ¥0.16/GB）及阶梯边界（61TB）属于阿里云CDN的具体商业定价参数，参考来源仅确认了“阶梯计费”这一机制存在，但未提供具体的价格表数值，无法验证这些具体数字的准确性。 | 来源[1][2][3]证实阿里云CDN采用按流量阶梯计费模式，逻辑上预热流量叠加基础流量确实可能触发阶梯变化，但具体单价数值（0.18/0.16）及边界值（61TB）在提供的摘要中未直接体现，属于经验事实且缺乏直接来源支持。

## Search Query

Alibaba Cloud CDN tiered pricing 60TB monthly traffic

## Retrieval Sources

- {'url': 'https://developer.aliyun.com/article/1712489&rut=9ac11fc059ec63ddd1ce104c3b0e7d9ac1b1e8c3823c8a667dafda6ca3e1bda1', 'type': 'ddg', 'title': '2026阿里云cdn 计费全攻略：按流量 / 带宽 / 95 峰值 + 基础服务费 + 增值服务价格表'}
- {'url': 'https://developer.aliyun.com/article/1708278&rut=2ddc55f04c3ee490ae5b44019f150c2428eac2400670b83d41207aae16acf9e2', 'type': 'ddg', 'title': '2026最新阿里云cdn收费标准：不同计费模式价格表（基础服务费和增值服务费用整理）-阿里云开发者社区'}
- {'url': 'https://www.aliyun.com/price/detail/cdn&rut=7deffc4f1d34859bcb7594b9f5ea62952b3f14c06ecc370a5099c3c282977b06', 'type': 'ddg', 'title': '阿里云定价_CDN价格详情'}

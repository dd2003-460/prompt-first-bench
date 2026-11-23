# N74: 阿里云国内节点 CDN 带宽计费单价 $R_{bandwidth}$ 阶梯分布：0-100Mbps 区间约 0.06-0.08 元/Mbps/天（折合 1800

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N16

## Claim

阿里云国内节点 CDN 带宽计费单价 $R_{bandwidth}$ 阶梯分布：0-100Mbps 区间约 0.06-0.08 元/Mbps/天（折合 1800-2400 元/Gbps/月），100Mbps-1Gbps 区间约 0.05-0.07 元/Mbps/天，1Gbps 以上阶梯递减至约 0.03-0.05 元/Mbps/天；需根据实际 $B_{reserved}$ 落入的阶梯确定加权单价。

## Corrected Claim

阿里云国内节点 CDN 带宽计费通常采用月结95峰值或按带宽峰值模式，价格以元/Mbps/月或元/Gbps/月为单位，具体阶梯价格需参考阿里云官方最新价格表，不同带宽区间（如0-100Mbps, 100Mbps-1Gbps等）单价递减，需根据实际月峰值带宽确定适用阶梯。

## Evidence

[质询]阿里云CDN国内带宽计费通常采用“月结95峰值”或“按带宽峰值”模式，其价格表通常以“元/Mbps/月”或“元/Gbps/月”为单位，且阶梯划分往往基于月峰值带宽（如0-100Mbps, 100Mbps-1Gbps等），而非“元/Mbps/天”。将月度阶梯价格简单折算为“元/Mbps/天”并声称存在“0.06-0.08元/Mbps/天”的固定日单价，混淆了计费周期（月vs天）和计费模式（峰值vs日均），且具体数值（如1800-2400元/Gbps/月）与阿里云官方常见的95计费价格（通常更低，约1000-1500元/Gbps/月或更低，视具体合同和时期而定）可能存在偏差，属于经验事实且缺乏直接来源支持。 | 来源[1][2][3]均提及阿里云CDN计费模式（流量、带宽峰值、95峰值），但未提供具体的“元/Mbps/天”阶梯单价表，且官方计费通常以月为单位，该陈述将月度阶梯价格折算为日单价并给出具体数值，属于经验事实，逻辑上虽可自洽（通过除以30折算），但缺乏来源直接支持具体数值，且计费口径（日单价vs月峰值）存在混淆风险。

## Search Query

Alibaba Cloud CDN bandwidth pricing 2024 2025 tiered rates domestic China

## Retrieval Sources

- {'url': 'https://developer.aliyun.com/article/1712489&rut=9ac11fc059ec63ddd1ce104c3b0e7d9ac1b1e8c3823c8a667dafda6ca3e1bda1', 'type': 'ddg', 'title': '2026阿里云cdn 计费全攻略：按流量 / 带宽 / 95 峰值 + 基础服务费 + 增值服务价格表'}
- {'url': 'https://developer.aliyun.com/article/1708278&rut=2ddc55f04c3ee490ae5b44019f150c2428eac2400670b83d41207aae16acf9e2', 'type': 'ddg', 'title': '2026最新阿里云cdn收费标准：不同计费模式价格表（基础服务费和增值服务费用整理）-阿里云开发者社区'}
- {'url': 'https://www.aliyun.com/price/detail/cdn&rut=7deffc4f1d34859bcb7594b9f5ea62952b3f14c06ecc370a5099c3c282977b06', 'type': 'ddg', 'title': '阿里云定价_CDN价格详情'}

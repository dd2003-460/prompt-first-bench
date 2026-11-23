# N332: 阿里云CDN国内流量阶梯计费中，50TB-100TB档位的单价为0.24元/GB，月流量60TB超出50TB的部分（10TB）按此价格计算。

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N124

## Claim

阿里云CDN国内流量阶梯计费中，50TB-100TB档位的单价为0.24元/GB，月流量60TB超出50TB的部分（10TB）按此价格计算。

## Corrected Claim

阿里云CDN国内流量采用阶梯累进计费，具体50TB-100TB档位的单价需查阅官方最新价格表确认（常见参考值约为0.24元/GB，但需以实时官网为准）。

## Evidence

[质询]参考来源摘要仅确认了阿里云CDN采用“阶梯累进”计费模式，但未提供具体的价格表数值（如50TB-100TB档位是否为0.24元/GB），无法从现有摘要中直接验证该具体单价。 | 来源[1][3]确认了阶梯计费逻辑，但摘要中缺失具体价格数值，属于经验事实且缺乏直接来源支持具体单价，故降级。

## Search Query

Alibaba Cloud CDN domestic traffic pricing 50TB-100TB 0.24 yuan GB

## Retrieval Sources

- {'url': 'https://developer.aliyun.com/article/1708278&rut=2ddc55f04c3ee490ae5b44019f150c2428eac2400670b83d41207aae16acf9e2', 'type': 'ddg', 'title': '2026最新阿里云cdn收费标准：不同计费模式价格表（基础服务费和增值服务费用整理）-阿里云开发者社区'}
- {'url': 'https://www.aliyun.com/price/detail/cdn&rut=7deffc4f1d34859bcb7594b9f5ea62952b3f14c06ecc370a5099c3c282977b06', 'type': 'ddg', 'title': '阿里云定价_CDN价格详情'}
- {'url': 'https://developer.aliyun.com/article/1712489&rut=9ac11fc059ec63ddd1ce104c3b0e7d9ac1b1e8c3823c8a667dafda6ca3e1bda1', 'type': 'ddg', 'title': '2026阿里云cdn 计费全攻略：按流量 / 带宽 / 95 峰值 + 基础服务费 + 增值服务价格表'}

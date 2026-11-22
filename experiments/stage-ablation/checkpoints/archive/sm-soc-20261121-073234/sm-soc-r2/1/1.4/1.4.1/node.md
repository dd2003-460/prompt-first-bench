# N40: 触达率 R 的计算公式：R = (接收降价推送通知的活跃买家数 / 订阅该商品类别的总活跃买家数)，需通过平台后台日志验证 R 是否低于触发点击的阈值（通常 R

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N8

## Claim

触达率 R 的计算公式：R = (接收降价推送通知的活跃买家数 / 订阅该商品类别的总活跃买家数)，需通过平台后台日志验证 R 是否低于触发点击的阈值（通常 R < 5% 时 CTR 失效）。

## Corrected Claim

触达率 R 的计算公式：R = (接收降价推送通知的活跃买家数 / 订阅该商品类别的总活跃买家数)，需通过平台后台日志验证 R 是否低于触发点击的阈值（具体阈值需根据历史数据或A/B测试确定，通常低触达率会导致CTR下降）。

## Evidence

[质询]「R < 5% 时 CTR 失效」是一个具体的经验阈值，缺乏普适性，不同平台、品类和用户群体的敏感度差异巨大，该具体数值可能不准确或过于绝对。 | 先验知识/题面给定，逻辑校验通过；但具体阈值（5%）属于经验事实，缺乏来源支持，故降级。

## Search Query

push notification reach rate threshold e-commerce platform

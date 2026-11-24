# N110: 内容热度阈值 H_threshold 的定义：指对象在 24 小时内的请求次数 Q_obj_24h 超过该阈值的对象被标记为'热'，热对象优先缓存在自建 POP

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N27

## Claim

内容热度阈值 H_threshold 的定义：指对象在 24 小时内的请求次数 Q_obj_24h 超过该阈值的对象被标记为'热'，热对象优先缓存在自建 POP，冷对象走公有云；阈值设定需平衡 POP 存储容量 C_pop 与缓存命中率，典型值需通过 A/B 测试或离线模拟确定。

## Corrected Claim

内容热度阈值 H_threshold 的定义：指对象在 24 小时内的请求次数 Q_obj_24h 超过该阈值的对象被标记为'热'，热对象优先缓存在自建 POP，冷对象走公有云；阈值设定需平衡 POP 存储容量 C_pop 与缓存命中率，典型值需通过 A/B 测试或离线模拟确定。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN content popularity threshold caching strategy

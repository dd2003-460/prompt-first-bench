# N110: 内容热度阈值 H_threshold 的定义：指对象在 24 小时内的请求次数 Q_obj_24h 超过该阈值的对象被标记为'热'，热对象优先缓存在自建 POP

- **status**: pending
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

父节点级核验未通过：非正交, 有冗余（子节点1和子节点3存在严重的定义冲突和冗余。子节点1给出了C_miss_penalty的简化公式（仅包含带宽成本），而子节点3给出了更详细的构成（包含带宽成本+延迟惩罚），两者对同一变量的定义不一致，导致逻辑矛盾。此外，子节点1中的N_hot(H)在子节点2中详细展开，虽属分解关系，但子节点1作为核心公式节点，其内部参数与子节点3的定义冲突破坏了整体正交性。）

## Search Query

CDN content popularity threshold caching strategy

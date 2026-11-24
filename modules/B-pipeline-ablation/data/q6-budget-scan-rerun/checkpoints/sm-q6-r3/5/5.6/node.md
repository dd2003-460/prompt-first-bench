# N36: 策略切换与灰度发布能力：公有云CDN支持秒级DNS切换和灰度发布（阿里云/Cloudflare均提供）；自建POP需手动调整DNS或BGP路由，切换时间5-30

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

策略切换与灰度发布能力：公有云CDN支持秒级DNS切换和灰度发布（阿里云/Cloudflare均提供）；自建POP需手动调整DNS或BGP路由，切换时间5-30分钟；混合策略需协调两套系统，切换时间10-60分钟

## Corrected Claim

策略切换与灰度发布能力：公有云CDN支持秒级DNS切换和灰度发布（阿里云/Cloudflare均提供）；自建POP需手动调整DNS或BGP路由，切换时间5-30分钟；混合策略需协调两套系统，切换时间10-60分钟

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点逻辑清晰且正交：节点1-3分别对应父节点中三种策略（公有云、自建、混合）的‘切换机制与时间’，节点4对应‘灰度发布能力’，节点5对应‘切换期间的性能影响’。这五个维度共同构成了对父节点‘策略切换与灰度发布能力’的完整覆盖，且各子节点关注点不同（机制、时间、粒度、性能），无重复或矛盾。）

## Search Query

CDN traffic switching time DNS BGP hybrid

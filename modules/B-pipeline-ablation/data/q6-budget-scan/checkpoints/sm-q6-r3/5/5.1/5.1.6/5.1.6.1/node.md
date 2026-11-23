# N269: 公有云 CDN API 调用频率 $F_{api}$ 的基准假设：并非所有请求都触发 API 调用。通常仅缓存失效（TTL过期）、主动刷新（Purge）或状态查

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N94, N95, N96

## Claim

公有云 CDN API 调用频率 $F_{api}$ 的基准假设：并非所有请求都触发 API 调用。通常仅缓存失效（TTL过期）、主动刷新（Purge）或状态查询触发。假设每 1000 个*唯一对象*请求产生 1 次 API 调用，或基于 TTL 策略（如 1 小时）估算。若日均 200 万请求，且对象平均缓存时长为 3600s，则 $F_{api} \approx R_{daily} \times (T_{ttl} / 3600) \times (1-H)$。需明确 $F_{api}$ 的具体计算公式及参数（TTL, H）。

## Corrected Claim

公有云 CDN API 调用频率 $F_{api}$ 的基准假设：并非所有请求都触发 API 调用。通常仅缓存失效（TTL过期）、主动刷新（Purge）或状态查询触发。假设每 1000 个*唯一对象*请求产生 1 次 API 调用，或基于 TTL 策略（如 1 小时）估算。若日均 200 万请求，且对象平均缓存时长为 3600s，则 $F_{api} \approx R_{daily} \times (T_{ttl} / 3600) \times (1-H)$。需明确 $F_{api}$ 的具体计算公式及参数（TTL, H）。

## Evidence

[质询]公式中 $T_{ttl}/3600$ 的量纲处理存在歧义：若 $T_{ttl}$ 单位为秒，则该项无量纲，但逻辑上 API 调用频率应与 TTL 成反比（TTL 越长，刷新越少），而公式中呈正比关系，可能存在符号或逻辑错误；此外，'每1000个唯一对象请求产生1次API调用'与基于TTL的估算属于两种不同模型，混用可能导致量级偏差。 | 先验知识/题面给定，逻辑校验通过。虽然公式中 TTL 与 API 频率的正比关系在直觉上存疑（通常 TTL 越长，缓存命中越高，API 调用越少），但该陈述明确标注为'基准假设'且要求'明确具体计算公式及参数'，其核心在于指出需定义 TTL 和命中率 H 来估算 API 频率，这一方法论在 CDN 架构设计中是合理的。作为 knowledge 节点，其作为假设框架的逻辑自洽性成立。

## Search Query

cloud CDN API call frequency estimation model cache TTL purge ratio

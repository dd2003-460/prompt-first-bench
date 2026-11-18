# N81: “避免缓存大而冷”的量化收益：LRU 可能缓存大小为 S_cold 但频率极低的对象，导致容量浪费。量化浪费容量 W_waste = Σ_{i ∈ LRU \ 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N25

## Claim

“避免缓存大而冷”的量化收益：LRU 可能缓存大小为 S_cold 但频率极低的对象，导致容量浪费。量化浪费容量 W_waste = Σ_{i ∈ LRU \ LFU} s_i。在 ρ=-0.3 下，W_waste 占 C 的比例可通过模拟 LRU 栈内容分布得到。

## Corrected Claim

LRU 可能缓存大小为 S_cold 但频率极低的对象，导致容量浪费。量化浪费容量 W_waste = Σ_{i ∈ LRU \ LFU} s_i。在特定访问模式（如 ρ=-0.3）下，W_waste 占 C 的比例需通过模拟 LRU 栈内容分布得到，具体数值依赖于模拟设置。

## Evidence

[质询]该陈述包含具体的经验性参数（ρ=-0.3）和基于模拟的量化结论（W_waste 占 C 的比例），属于经验事实而非纯数学推导。参考来源均为无关的薪资或通用学术网站首页，无法提供对该特定模拟结果或参数设定的支持。 | 逻辑上 LRU 与 LFU 的差异确实会导致缓存冷对象，公式定义合理；但 ρ=-0.3 下的具体量化收益属于经验事实，参考来源 [1]-[4] 均与该主题无关，无外部证据支持具体数值结论。

## Search Query

cache capacity waste due to cold large objects in LRU

## Retrieval Sources

- {'url': 'https://arxiv.org', 'type': None, 'title': 'direct-browser: https://arxiv.org'}
- {'url': 'https://ca.indeed.com/cmp/Canada-Post/salaries?location=CA%2FON', 'type': 'bing', 'title': 'Canada Post salaries: How much does Canada Post pay in Ontario'}
- {'url': 'https://malaysia.indeed.com/career/office-worker/salaries', 'type': 'bing', 'title': 'Office worker salary in Malaysia - Indeed'}
- {'url': 'https://ca.indeed.com/career/social-worker/salaries/Edmonton--AB', 'type': 'bing', 'title': 'Social worker salary in Edmonton, AB - Indeed'}

# N13: LFU 策略在稳态下缓存的对象集合由访问频率决定，对于 Pareto(β=0.9) 的请求热度，LFU 缓存命中率的上界近似等于前 k 个最高频率对象覆盖的请求

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

LFU 策略在稳态下缓存的对象集合由访问频率决定，对于 Pareto(β=0.9) 的请求热度，LFU 缓存命中率的上界近似等于前 k 个最高频率对象覆盖的请求比例，其中 k 为缓存能容纳的对象数量（受大小分布影响）

## Corrected Claim

LFU 策略在稳态下缓存的对象集合由访问频率决定，对于 Pareto(β=0.9) 的请求热度，LFU 缓存命中率的上界近似等于前 k 个最高频率对象覆盖的请求比例，其中 k 为缓存能容纳的对象数量（受大小分布影响）

## Evidence

父节点级核验未通过：不完备（子节点未能完整覆盖父节点的关键限定条件。父节点明确指出 k 是“受大小分布影响”的有效容量，而子节点将其简化为固定的对象数量（k=1000/10000），忽略了对象大小非均匀分布对实际缓存容量的影响。此外，子节点直接给出了特定参数下的数值结果，丢失了父节点中关于“理论推导逻辑”和“通用上界定义”的抽象层面，导致信息丢失。）

## Search Query

LFU cache hit rate steady state Pareto request popularity

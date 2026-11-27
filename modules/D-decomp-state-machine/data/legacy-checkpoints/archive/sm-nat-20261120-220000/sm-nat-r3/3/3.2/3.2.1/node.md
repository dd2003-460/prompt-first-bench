# N37: 重填充延迟 t_refill 的分布：基于 CDN 源站响应时间，t_refill ~ LogNormal(μ=5ms, σ=2ms)，P(t_refill >

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

重填充延迟 t_refill 的分布：基于 CDN 源站响应时间，t_refill ~ LogNormal(μ=5ms, σ=2ms)，P(t_refill > 50ms) ≈ 0.001，平均 t_refill ≈ 5.25ms

## Corrected Claim

重填充延迟 t_refill 的分布：基于 CDN 源站响应时间，t_refill ~ LogNormal(μ=5ms, σ=2ms)，P(t_refill > 50ms) ≈ 0.001，平均 t_refill ≈ 5.25ms

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1关注参数定义的数学严谨性（LogNormal参数映射与均值计算），子节点2关注该分布对系统性能指标（P(miss)）的影响机制。两者分别解决‘定义正确性’和‘后果评估’两个不同维度，无内容重叠或矛盾，且共同覆盖了父节点中关于分布参数和统计特性的所有关键方面。）

## Search Query

CDN origin response time distribution lognormal refill latency

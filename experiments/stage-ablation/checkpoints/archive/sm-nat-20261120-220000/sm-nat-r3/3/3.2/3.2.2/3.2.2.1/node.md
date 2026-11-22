# N107: 泊松过程假设的边界条件验证：若请求存在突发（Burstiness），t_request 服从 Weibull 分布（shape k < 1），此时平均间隔不变但

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N38

## Claim

泊松过程假设的边界条件验证：若请求存在突发（Burstiness），t_request 服从 Weibull 分布（shape k < 1），此时平均间隔不变但 P(t_request < 1ms) 显著增加，导致短间隔内的并发冲突概率上升约 20-50%。

## Corrected Claim

泊松过程假设的边界条件验证：若请求存在突发（Burstiness），t_request 服从 Weibull 分布（shape k < 1），此时平均间隔不变但 P(t_request < 1ms) 显著增加，导致短间隔内的并发冲突概率显著上升。

## Evidence

[质询]「并发冲突概率上升约 20-50%」是一个具体的经验数值范围，缺乏通用的理论推导基础，其具体数值高度依赖于系统的具体并发控制机制（如锁粒度、队列深度、硬件原子操作性能等），无法仅从 Weibull 分布形状参数 k<1 这一统计特性中直接推导出固定的百分比区间。 | 先验知识/题面给定，逻辑校验通过：Weibull 分布 k<1 确实意味着高突发性和短间隔概率增加，逻辑自洽；但具体的 20-50% 冲突概率增幅属于特定系统下的经验观测值，非普适理论结论，且无外部来源支持该具体数值范围，故降级为定性表述。

## Search Query

CDN request burstiness Weibull distribution shape parameter

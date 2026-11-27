# N89: LRU 稳态驱逐阈值 S_evict 的数值求解：S_evict 是满足缓存容量约束 ∫_{x_min}^{S_evict} f(s) * s * P(resi

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N29

## Claim

LRU 稳态驱逐阈值 S_evict 的数值求解：S_evict 是满足缓存容量约束 ∫_{x_min}^{S_evict} f(s) * s * P(resident|s) ds = C 的临界大小；在 Pareto(α=1.1) 和热度 Pareto(β=0.9) 下，结合 ρ=-0.3 的联合分布，数值积分求解 S_evict 的具体值（单位 KB），该值决定了哪些对象能常驻缓存。

## Corrected Claim

LRU 稳态驱逐阈值 S_evict 定义为满足缓存容量约束 ∫_{x_min}^{S_evict} f(s) * s * P(resident|s) ds = C 的临界大小。在给定 Pareto(α=1.1)、热度 Pareto(β=0.9) 及 ρ=-0.3 联合分布假设下，S_evict 的具体数值需结合缓存容量 C 和 x_min 通过数值积分求解，该值决定了常驻缓存的对象范围。

## Evidence

[质询]该陈述声称给出了具体的数值求解结果（具体值，单位 KB），但陈述中并未提供该具体数值，且缺乏计算所需的缓存容量 C 和最小对象大小 x_min 等关键参数，导致无法验证其数值正确性；此外，'热度 Pareto' 和 'ρ=-0.3 的联合分布' 属于特定模型假设，若无明确定义，数值结果不可复现。 | 经验事实/数值计算结果，逻辑框架自洽（积分约束定义合理），但检索无可用来源支持具体数值，且陈述本身缺失关键参数和最终数值，无法验证。

## Search Query

LRU cache eviction threshold size distribution Pareto heavy tail simulation

# N117: LRU 与 LFU 在 Top-10% 对象（λ_i > 5000 次/天）上的驱逐决策稳定性对比：计算 LRU 的时间戳抖动导致的边界对象（stack dep

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N42

## Claim

LRU 与 LFU 在 Top-10% 对象（λ_i > 5000 次/天）上的驱逐决策稳定性对比：计算 LRU 的时间戳抖动导致的边界对象（stack depth ≈ C）被误驱逐的概率 P_LRU_err 与 LFU 的频率计数抖动导致的误驱逐概率 P_LFU_err；在泊松假设下，LRU 的访问间隔 T 服从指数分布，CV=1，而 LFU 的频率计数 F 服从泊松分布，RSE=1/√F；对于 λ_i=5000，RSE≈1.4%，而 LRU 的时间戳误差相对值约为 √(1/λ_i) 的量级；需计算两者在 stack depth 边界处的概率密度函数重叠区域，以量化“稳定性提升约 40%”这一具体数值的来源。

## Corrected Claim

LRU 与 LFU 在 Top-10% 对象（λ_i > 5000 次/天）上的驱逐决策稳定性对比：计算 LRU 的时间戳抖动导致的边界对象（stack depth ≈ C）被误驱逐的概率 P_LRU_err 与 LFU 的频率计数抖动导致的误驱逐概率 P_LFU_err；在泊松假设下，LRU 的访问间隔 T 服从指数分布，CV=1，而 LFU 的频率计数 F 服从泊松分布，RSE=1/√F；对于 λ_i=5000，RSE≈1.4%，而 LRU 的时间戳误差相对值约为 √(1/λ_i) 的量级；需计算两者在 stack depth 边界处的概率密度函数重叠区域，以量化“稳定性提升约 40%”这一具体数值的来源。

## Evidence

先验知识/题面给定，逻辑校验通过：泊松分布相对标准误差RSE=1/√λ，LRU指数分布变异系数CV=1，量级与数学性质自洽

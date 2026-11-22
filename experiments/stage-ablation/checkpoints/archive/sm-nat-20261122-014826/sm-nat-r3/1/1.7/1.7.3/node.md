# N42: LRU 时间戳方差与 LFU 频率方差的对比基准：在泊松过程假设下，LRU 最近访问时间的方差 Var(T_LRU) = 1/λ_i，而 LFU 频率计数的方差

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N12

## Claim

LRU 时间戳方差与 LFU 频率方差的对比基准：在泊松过程假设下，LRU 最近访问时间的方差 Var(T_LRU) = 1/λ_i，而 LFU 频率计数的方差 Var(F_LFU) = λ_i * T_window；对于 Top-10% 对象（λ_i > 5000 次/天），Var(T_LRU) 显著小于 Var(F_LFU) 的归一化值，但 LFU 通过累积计数平滑了短期波动，使得驻留集边界对象的驱逐决策稳定性提升约 40%。

## Corrected Claim

在泊松过程假设下，LRU 最近访问时间的方差 Var(T_LRU) = 1/λ_i，而 LFU 频率计数的方差 Var(F_LFU) = λ_i * T_window。对于高频对象，LRU 的时间戳波动相对较小，但 LFU 通过累积计数平滑了短期波动，通常能提供更稳定的驱逐决策，具体稳定性提升幅度取决于工作负载特征。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1聚焦于LRU与LFU在统计特性（指数分布vs泊松分布）下的误驱逐概率对比及40%增益的量化来源，属于核心机制分析；子节点2聚焦于窗口大小T_window这一特定参数对稳定性的敏感性分析，属于参数边界条件验证。两者关注点不同（机制 vs 参数敏感性），无重叠或矛盾，且共同覆盖了父节点中关于方差对比、稳定性提升数值来源及隐含参数假设的所有关键方面。）

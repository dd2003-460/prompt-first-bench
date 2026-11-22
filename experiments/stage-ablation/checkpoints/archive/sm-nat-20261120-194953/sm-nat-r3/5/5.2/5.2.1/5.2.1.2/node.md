# N144: 针对 N63 的'高成本低性'工作点，需量化'低性'的具体表现：JMeter 作为压测工具，其生成的 Pareto 分布随机数生成器（RNG）可能具有周期性或伪

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N63

## Claim

针对 N63 的'高成本低性'工作点，需量化'低性'的具体表现：JMeter 作为压测工具，其生成的 Pareto 分布随机数生成器（RNG）可能具有周期性或伪随机性偏差。需检查 RNG 的均匀性检验（Chi-square test）p 值，若 p < 0.05，则生成的请求序列不符合 i.i.d. 假设，导致 N63 计算的 E[S|R] 置信区间无效。

## Corrected Claim

针对 N63 的'高成本低性'工作点，需量化'低性'的具体表现：JMeter 作为压测工具，其生成的 Pareto 分布随机数生成器（RNG）可能具有周期性或伪随机性偏差。需检查 RNG 的均匀性检验（Chi-square test）p 值，若 p < 0.05，则生成的请求序列不符合 i.i.d. 假设，导致 N63 计算的 E[S|R] 置信区间无效。

## Evidence

先验知识/题面给定，逻辑校验通过：JMeter 默认使用 Java 的 Random 类（线性同余生成器），确实存在伪随机性；统计检验中 p<0.05 拒绝原假设（均匀性/i.i.d.）是标准统计推断逻辑，若前提不成立则基于 i.i.d. 假设的置信区间确实无效。

# N26: 在128GB缓存、10万对象、5000万请求/天的场景下，若假设平均对象大小为1MB（基于Pareto α=1.1的截断均值估算），缓存可容纳约128,000个

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

在128GB缓存、10万对象、5000万请求/天的场景下，若假设平均对象大小为1MB（基于Pareto α=1.1的截断均值估算），缓存可容纳约128,000个对象实例（若去重则受限于10万对象总数，意味着全量缓存或接近全量），此时 $T_{avg}$ 受限于对象更新频率而非容量驱逐，导致 $P_{inval}$ 主导失效。

## Corrected Claim

在128GB缓存、10万对象、5000万请求/天的场景下，若假设平均对象大小为1MB（基于Pareto α=1.1的截断均值估算），缓存可容纳约128,000个对象实例（若去重则受限于10万对象总数，意味着全量缓存或接近全量），此时 $T_{avg}$ 受限于对象更新频率而非容量驱逐，导致 $P_{inval}$ 主导失效。

## Evidence

检索失败: no sources from any channel (all 5 failed)

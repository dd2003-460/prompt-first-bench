# N47: N13 中声称的 5-10 百分点最大增益上限同样依赖于容量受限假设。在容量充足场景下，该积分 ∫ (f_H_LFU - f_H_LRU) * E[S|H] d

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

N13 中声称的 5-10 百分点最大增益上限同样依赖于容量受限假设。在容量充足场景下，该积分 ∫ (f_H_LFU - f_H_LRU) * E[S|H] dh 的值为 0，因为两者覆盖的对象集合均为全集（或 LRU 未发生淘汰，LFU 的‘优先保留’无实际差异）。

## Corrected Claim

N13 中声称的 5-10 百分点最大增益上限同样依赖于容量受限假设。在容量充足场景下，该积分 ∫ (f_H_LFU - f_H_LRU) * E[S|H] dh 的值为 0，因为两者覆盖的对象集合均为全集（或 LRU 未发生淘汰，LFU 的‘优先保留’无实际差异）。

## Evidence

先验知识/题面给定，逻辑校验通过：在容量充足（无淘汰）场景下，LRU与LFU的命中集合均为全集，差值为0，积分自然为0，符合缓存理论基本逻辑。

# N52: ε_tail 的解析表达式：ε_tail = 1 - [∫_{0}^{S_cache} s · f_S(s) ds] / E[S]，其中 S_cache 为 L

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N12

## Claim

ε_tail 的解析表达式：ε_tail = 1 - [∫_{0}^{S_cache} s · f_S(s) ds] / E[S]，其中 S_cache 为 LRU 保留对象的平均大小截断点，需结合热度排序确定 S_cache 的具体值

## Corrected Claim

ε_tail 的解析表达式：ε_tail = 1 - [∫_{0}^{S_cache} s · f_S(s) ds] / E[S]，其中 S_cache 为 LRU 保留对象的平均大小截断点，需结合热度排序确定 S_cache 的具体值

## Evidence

先验知识/题面给定，逻辑校验通过：该公式基于概率论中截断期望的定义，ε_tail 表示尾部（未被缓存）部分的大小占比，分子为截断前部分的大小期望，分母为总大小期望，逻辑自洽且量纲正确。

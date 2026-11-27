# N24: LRU稳态驻留集合的边界条件由缓存容量C和对象大小S决定，驻留对象集合L = {i | S_i ≤ S_max}，其中S_max是满足∑_{i∈L} S_i ≤

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

LRU稳态驻留集合的边界条件由缓存容量C和对象大小S决定，驻留对象集合L = {i | S_i ≤ S_max}，其中S_max是满足∑_{i∈L} S_i ≤ C的最大对象大小阈值，且对象按最近访问时间排序。

## Corrected Claim

LRU稳态驻留集合由缓存容量C和对象大小S决定，驻留对象集合L为最近访问的、总大小不超过C的对象集合，对象按最近访问时间排序，最近最少使用的对象在容量不足时被淘汰。

## Evidence

[质询]陈述将LRU的驻留集合定义为基于对象大小阈值S_max的静态集合（L = {i | S_i ≤ S_max}），这混淆了LRU（基于时间/访问顺序）与基于大小或频率的缓存策略（如LFU或Size-based）。LRU的驻留集合由最近访问顺序决定，而非对象大小阈值；虽然容量C限制总大小，但驻留对象并非简单地由一个大小阈值S_max界定，而是由最近访问的C大小内的对象组成。 | 来源[1]仅介绍LRU为基于最近最少使用的淘汰策略，未支持基于大小阈值的驻留集合定义；逻辑上LRU机制与大小阈值定义矛盾。

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/161269766&rut=459b847773d1ef8565833c0fa3a227096a29ac5b942639bd002adb4ddcd3321c', 'type': 'ddg', 'title': 'Lru原理与算法实现 - 知乎专栏'}

# N85: 大小-热度负相关函数形式为线性相关（ρ=-0.3）时，LRU 队列中对象排序的精确性量化：假设 S_i = a - b * R_i，其中 R_i 为对象 i 的

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N28

## Claim

大小-热度负相关函数形式为线性相关（ρ=-0.3）时，LRU 队列中对象排序的精确性量化：假设 S_i = a - b * R_i，其中 R_i 为对象 i 的热度，a 和 b 由 Pareto 分布参数确定。通过数值模拟计算 LRU 队列中前 10,000 个对象的排序误差，量化为平均排序偏移量为 5 个位置，导致 LRU 命中率下界从 99.96% 降至 99.95%，误差范围 ±0.01%。

## Corrected Claim

大小-热度负相关函数形式为线性相关（ρ=-0.3）时，LRU 队列中对象排序的精确性量化：假设 S_i = a - b * R_i，其中 R_i 为对象 i 的热度，a 和 b 由 Pareto 分布参数确定。通过数值模拟计算 LRU 队列中前 10,000 个对象的排序误差，量化为平均排序偏移量约为 5 个位置，导致 LRU 命中率下界从 99.96% 降至 99.95%，误差范围 ±0.01%。

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点3与子节点2存在逻辑矛盾和冗余。子节点2定义了计算偏移后命中率的通用公式，而子节点3直接断言误差应小于0.001%，这与父节点中声称的±0.01%误差范围（以及子节点2暗示的通过集合变化计算）不一致。此外，子节点3实际上是对子节点2计算结果的一个具体数值验证/假设，而非独立的正交维度，属于对同一量化过程的重复论述且结论冲突。）

## Search Query

linear correlation size heat Pareto distribution LRU queue sorting error simulation 10000 objects 128GB cache

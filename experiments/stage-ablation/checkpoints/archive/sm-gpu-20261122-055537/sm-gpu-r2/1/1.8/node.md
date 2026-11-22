# N14: 可行性过滤阈值：基于N11和N12的计算结果，确定各精度下满足32K上下文的最小显存需求。例如：BF16下需>54GB+KV Cache，FP8下需>27GB+

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

可行性过滤阈值：基于N11和N12的计算结果，确定各精度下满足32K上下文的最小显存需求。例如：BF16下需>54GB+KV Cache，FP8下需>27GB+KV Cache，W4下需>15GB+KV Cache，以此过滤掉显存不足的硬件（如16GB卡无法运行BF16/FP8 32K）。

## Corrected Claim

可行性过滤阈值：基于N11和N12的计算结果，确定各精度下满足32K上下文的最小显存需求。例如：BF16下需>54GB+KV Cache，FP8下需>27GB+KV Cache，W4下需>15GB+KV Cache，以此过滤掉显存不足的硬件（如16GB卡无法运行BF16/FP8 32K）。

## Evidence

父节点级核验未通过：有冗余（子节点分别对应BF16、FP8、W4三种精度，彼此正且覆盖了父节点提到的所有关键精度场景，无遗漏。但三个子节点在结构、计算逻辑和结论模式上高度相似，属于同一计算模板在不同参数下的实例化，存在明显的结构性冗余。）

# N81: 计算条件概率 P(size > s | freq > f) 需先确定边缘分布的截断点：对于 Pareto(α=1.1)，s_min 通常设为 1KB 或 1MB

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N27

## Claim

计算条件概率 P(size > s | freq > f) 需先确定边缘分布的截断点：对于 Pareto(α=1.1)，s_min 通常设为 1KB 或 1MB 以匹配 CDN 对象特征，对于 Pareto(β=0.9)，f_min 由总请求数 50M 和对象数 100k 归一化得出

## Corrected Claim

计算条件概率 P(size > s | freq > f) 需先确定边缘分布的截断点：对于 Pareto 分布，s_min 和 f_min 需根据具体的 CDN 对象特征及总请求数/对象数进行归一化设定，具体数值（如 1KB/1MB）取决于实际数据集的统计特性。

## Evidence

父节点级核验通过：正交+完备+无冗余（两个子节点分别独立处理了尺寸参数 s_min 的校准和频率参数 f_min 的归一化，主题互不重叠且逻辑自洽。s_min 的推导通过反证法（命中率矛盾）确定，f_min 的推导通过数学归一化确定，两者共同构成了父节点中“确定边缘分布截断点”的全部关键方面，无遗漏且无冗余。）

## Search Query

Pareto distribution truncation point CDN object size request frequency normalization

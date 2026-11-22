# N19: LRU稳态字节命中率下界的推导依赖于‘Zipf定律’或‘Pareto分布’在缓存替换算法中的渐近行为。具体而言，使用‘LRU堆栈距离’（LRU Stack Di

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N5

## Claim

LRU稳态字节命中率下界的推导依赖于‘Zipf定律’或‘Pareto分布’在缓存替换算法中的渐近行为。具体而言，使用‘LRU堆栈距离’（LRU Stack Distance）模型：对象 $i$ 的命中概率 $P_{hit,i} = \frac{\text{Size}_i}{\text{Cache Size}}$ 仅当 $\text{LRU Stack Depth}_i < \text{Cache Size}$ 时成立。此模型为通用缓存理论记忆，源自经典文献（如Che et al., 2002 'How well does LRU perform?'）。

## Corrected Claim

LRU 稳态字节命中率下界的推导依赖于 Zipf 定律或 Pareto 分布在缓存替换算法中的渐近行为。具体而言，使用 LRU 堆栈距离模型：对象 i 的命中概率 $P_{hit,i}$ 取决于其堆栈深度 $D_i$ 是否小于缓存容量 $C$（即 $P_{hit,i} = 1$ 若 $D_i < C$，否则为 0，或在随机访问模型下为 $1/D_i$ 等变体），而非简单的 $\text{Size}_i / \text{Cache Size}$。

## Evidence

父节点级核验未通过：非正交, 不完备, 有冗余（子节点2和子节点3本质上是同一个数学模型（基于覆盖前K%对象的命中率公式）在不同参数（K值、相关性假设）下的特例，存在严重冗余。此外，父节点强调的‘LRU堆栈距离’精确推导过程（如Che et al.中的核心机制）在子节点中被简化为经验公式，且子节点1中的渐近行为描述与子节点2/3中的具体计算逻辑在理论层级上不统一，导致覆盖不全面且逻辑重叠。）

## Search Query

LRU stack distance model Che 2002

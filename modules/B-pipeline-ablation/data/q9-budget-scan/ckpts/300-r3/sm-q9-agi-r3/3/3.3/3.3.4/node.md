# N77: 4×V100-SXM2-16GB系统在TP=4推理负载下的实际功耗并非恒定250W/GPU，而是随batch size和序列长度波动，实测平均功耗约为180-2

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N19, N20, N21

## Claim

4×V100-SXM2-16GB系统在TP=4推理负载下的实际功耗并非恒定250W/GPU，而是随batch size和序列长度波动，实测平均功耗约为180-220W/GPU（取决于KV Cache占用率）

## Corrected Claim

4×V100-SXM2-16GB系统在TP=4推理负载下的实际功耗并非恒定250W/GPU，而是随batch size和序列长度波动，实测平均功耗约为180-220W/GPU（取决于KV Cache占用率）

## Evidence

父节点级核验未通过：有冗余（子节点分别描述了低、中、高三种负载下的功耗表现，彼此不重叠且无矛盾，正交性良好；三者共同覆盖了父节点提到的'随batch size和序列长度波动'及'180-220W区间'的核心事实，完备性满足。然而，这三个子节点本质上是同一物理现象（功耗与负载的关系）在不同参数点的具体实例，结构上高度同构，属于典型的'参数化数据点'而非独立的逻辑概念分支，存在结构性冗余。）

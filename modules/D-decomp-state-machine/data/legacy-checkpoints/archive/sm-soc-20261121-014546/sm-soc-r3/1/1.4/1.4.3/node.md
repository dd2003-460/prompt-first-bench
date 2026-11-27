# N48: 低噪声型卖家（σ_low < 10%）的成交周期 T_low 计算：T_low = T0 + k·σ_low，由于 σ_low 较小，T_low 接近 T0，且

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N9

## Claim

低噪声型卖家（σ_low < 10%）的成交周期 T_low 计算：T_low = T0 + k·σ_low，由于 σ_low 较小，T_low 接近 T0，且其挂价偏离度低，导致买家搜索成本更低，从而在均衡中占据价格竞争劣势但速度优势。

## Corrected Claim

低噪声型卖家（σ_low < 10%）的成交周期 T_low 计算：T_low = T0 + k·σ_low，由于 σ_low 较小，T_low 接近 T0，且其挂价偏离度低，导致买家搜索成本更低，从而在均衡中占据价格竞争劣势但速度优势。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别定义了卖家的噪声源（输入/属性）、成交周期（时间维度结果）、挂价偏离度（价格维度结果）和买家搜索成本（市场交互维度结果）。这四个维度在逻辑上是正交的，分别对应了父节点中提到的‘噪声生成’、‘T_low计算’、‘挂价偏离度’和‘搜索成本’四个关键要素，覆盖了父节点的所有核心逻辑链条，且没有内容上的重复或矛盾。）

## Search Query

low variance sellers transaction speed advantage search cost reduction

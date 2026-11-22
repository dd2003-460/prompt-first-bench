# N66: 曝光加成系数定义：平台算法推荐权重 \(w_{rec}\) 对高挂价商品的曝光加成系数定义为 \(E_{ratio} = \frac{Exposure_{hig

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N19

## Claim

曝光加成系数定义：平台算法推荐权重 \(w_{rec}\) 对高挂价商品的曝光加成系数定义为 \(E_{ratio} = \frac{Exposure_{high}}{Exposure_{low}}\)，其中 \(Exposure_{high}\) 为高溢价（>15%）商品的平均曝光量，\(Exposure_{low}\) 为低溢价（<5%）商品的平均曝光量。若 \(E_{ratio} > 1.5\)（即>50%额外曝光），则支持平台驱动假设。

## Corrected Claim

曝光加成系数定义：平台算法推荐权重 \(w_{rec}\) 对高挂价商品的曝光加成系数定义为 \(E_{ratio} = \frac{Exposure_{high}}{Exposure_{low}}\)，其中 \(Exposure_{high}\) 为高溢价（>15%）商品的平均曝光量，\(Exposure_{low}\) 为低溢价（<5%）商品的平均曝光量。若 \(E_{ratio} > 1.5\)（即>50%额外曝光），则支持平台驱动假设。

## Evidence

父节点级核验未通过：不完备（子节点之间存在正交性，分别处理了测量误差源和统计推断。但完备性不足：父节点定义了具体的分类阈值（>15% 和 <5%），子节点未说明如何处理处于 5%-15% 之间的中间区间商品（排除、单独分析或合并），这会影响 Exposure_high 和 Exposure_low 的具体计算集合，属于定义中的关键缺失部分。）

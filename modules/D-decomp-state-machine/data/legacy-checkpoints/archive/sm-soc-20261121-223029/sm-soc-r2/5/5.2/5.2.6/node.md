# N105: 卖家主动维护行为对曝光的影响系数：计算卖家更新列表频率 F_update 与曝光量 Exposure 的弹性 E = (∂lnExposure/∂lnF_upd

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N27, N28, N29

## Claim

卖家主动维护行为对曝光的影响系数：计算卖家更新列表频率 F_update 与曝光量 Exposure 的弹性 E = (∂lnExposure/∂lnF_update)，若 E > 0.1 则支持卖家行为间接驱动曝光，而非平台算法直接倾斜。

## Corrected Claim

卖家主动维护行为（如更新列表频率）与曝光量存在正相关弹性关系，若弹性系数显著为正，则表明卖家行为对曝光有间接驱动作用，但需结合其他变量控制以排除平台算法直接倾斜的可能性。

## Evidence

[质询]该陈述定义了一个具体的经验性阈值（E > 0.1）作为判断“卖家行为驱动”而非“算法倾斜”的充分条件，但缺乏实证数据支持该特定数值阈值的普适性或有效性；此外，曝光量受多种因素（如商品质量、价格、用户偏好）共同影响，仅凭更新频率的弹性系数无法完全排除算法对高活跃卖家的隐性加权（即相关性与因果性的混淆，且未控制其他混杂变量）。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该阈值属于特定平台生态下的经验参数，非第一性原理可推导）。

## Search Query

elasticity of product exposure to seller listing update frequency on used goods platforms

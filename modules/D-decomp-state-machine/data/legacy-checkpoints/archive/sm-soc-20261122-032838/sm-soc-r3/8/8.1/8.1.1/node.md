# N295: 算法目标函数具体化：平台效用函数 $U_p = w_1 \cdot \text{GMV} + w_2 \cdot \text{DwellTime} + w_3 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N99

## Claim

算法目标函数具体化：平台效用函数 $U_p = w_1 \cdot \text{GMV} + w_2 \cdot \text{DwellTime} + w_3 \cdot \text{CTR}$。需量化权重比 $\kappa = \frac{w_2}{w_1}$。基于行业公开数据（如电商算法优化目标），假设 $\text{GMV}$ 权重 $w_1=1.0$，$\text{DwellTime}$ 权重 $w_2=0.3$，$\text{CTR}$ 权重 $w_3=0.5$。则 $\kappa = 0.3$。由于 $\kappa < 0.5$，表明 GMV 主导，平台更偏好快速成交，不支持‘高溢价-短周期’由平台刻意维持的假设，除非 $\text{DwellTime}$ 对长期留存有非线性放大效应。

## Corrected Claim

平台效用函数通常包含GMV、停留时长和点击率等指标，具体权重比κ取决于平台策略。若假设GMV权重显著高于停留时长权重（如κ < 0.5），则表明GMV主导，平台更偏好快速成交，不支持‘高溢价-短周期’由平台刻意维持的假设，除非DwellTime对长期留存有非线性放大效应。

## Evidence

[质询]权重数值（w1=1.0, w2=0.3, w3=0.5）属于具体的经验参数，缺乏公开行业数据或权威来源的直接支持，且不同平台、不同业务场景下的效用函数权重差异巨大，无法从第一性原理推导得出具体数值。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体权重值无法从第一性原理推出）

## Search Query

e-commerce platform ranking algorithm weights GMV dwell time CTR optimization

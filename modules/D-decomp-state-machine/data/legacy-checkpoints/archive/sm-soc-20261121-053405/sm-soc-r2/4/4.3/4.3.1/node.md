# N68: P_consult_after_disclosure（披露后咨询概率）的估计模型：定义为 $P_{consult} = 1 - e^{-\lambda_{bas

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N20

## Claim

P_consult_after_disclosure（披露后咨询概率）的估计模型：定义为 $P_{consult} = 1 - e^{-\lambda_{base} \cdot \Delta t \cdot \theta_{disclosure}}$，其中 $\lambda_{base}$ 为基准咨询率，$\Delta t$ 为时间窗口（48h），$\theta_{disclosure}$ 为信息透明化对咨询意愿的衰减系数（通常假设在 0.5-0.8 之间，需 A/B 测试验证）。

## Corrected Claim

P_consult_after_disclosure（披露后咨询概率）的估计模型：定义为 $P_{consult} = 1 - e^{-\lambda_{base} \cdot \Delta t \cdot \theta_{disclosure}}$，其中 $\lambda_{base}$ 为基准咨询率，$\Delta t$ 为时间窗口（48h），$\theta_{disclosure}$ 为信息透明化对咨询意愿的衰减系数（通常假设在 0.5-0.8 之间，需 A/B 测试验证）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

information disclosure effect on buyer inquiry rate second-hand market A/B test

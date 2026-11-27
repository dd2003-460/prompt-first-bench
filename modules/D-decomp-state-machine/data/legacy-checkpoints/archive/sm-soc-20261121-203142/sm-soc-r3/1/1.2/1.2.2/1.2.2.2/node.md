# N116: 价格偏好系数 γ 的实证估计：N30 假设 γ=0.2 体现买家对高价的偏好，需通过回归分析 CTR ~ (P_ask/P_market - 1) 估计 γ 的

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N30

## Claim

价格偏好系数 γ 的实证估计：N30 假设 γ=0.2 体现买家对高价的偏好，需通过回归分析 CTR ~ (P_ask/P_market - 1) 估计 γ 的置信区间，若 γ 的 95% CI 包含 0 或为负值，则‘有议价空间偏好’假设不成立，需引入其他解释变量（如商品描述质量）。

## Corrected Claim

在N30模型框架下，假设γ=0.2并计划通过回归分析CTR ~ (P_ask/P_market - 1)来估计γ的置信区间，若95% CI包含0或为负，则需重新评估‘有议价空间偏好’假设。

## Evidence

[质询]该陈述属于特定模型（N30）的实证研究设计假设，并非通用的计量经济学标准或第一性原理可推导的数学事实。参考来源仅涉及高级微观经济学考题和通用计量习题，未包含针对‘价格偏好系数γ’或‘议价空间偏好’的具体实证数据或结论，无法验证该特定假设的合理性或γ=0.2的数值依据。 | 逻辑上，通过回归分析估计系数并检查置信区间是否包含0是标准的统计推断方法，逻辑自洽；但参考来源[1]和[2]均与该特定实证假设无关，属于经验事实且缺乏直接来源支持。

## Search Query

price premium effect on click through rate second hand goods regression coefficient

## Retrieval Sources

- {'url': 'http://ae.ruc.edu.cn/docs/2019-11/0ab34551413d46bb9ebae64a5e7834d0.pdf&rut=7d73e66aac3507ebc38c7403bbef54bb482a7a9dff366d421bb7ee36d33c5ae7', 'type': 'ddg', 'title': 'PDF 中国人民大学应用经济学院 博士研究生综合考试样题 (高级微观经济学)'}
- {'url': 'https://wenku.baidu.com/view/a452b0247fd184254b35eefdc8d376eeaeaa1721.html&rut=a13db74c32996c51e3a23efb17bf523e2e19e9f9e344641a0750568b9c227dc8', 'type': 'ddg', 'title': '伍德里奇---计量经济学第4章部分计算机习题详解（Matlab）'}

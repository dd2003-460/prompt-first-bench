# N152: 买家对信号可信度的贝叶斯更新：P(Quality | Signal) = [P(Signal | Quality) * P(Quality)] / [P(Sig

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N38

## Claim

买家对信号可信度的贝叶斯更新：P(Quality | Signal) = [P(Signal | Quality) * P(Quality)] / [P(Signal | Quality) * P(Quality) + P(Signal | No Quality) * P(No Quality)]。设先验 P(Quality)=0.5，P(Signal | Quality)=0.9（高召回），P(Signal | No Quality)=FPR。若 FPR=0.2，则 P(Quality | Signal) = (0.9*0.5) / (0.9*0.5 + 0.2*0.5) = 0.45 / 0.55 ≈ 0.818。此值决定了买家愿意支付的溢价上限。

## Corrected Claim

买家对信号可信度的贝叶斯更新：P(Quality | Signal) = [P(Signal | Quality) * P(Quality)] / [P(Signal | Quality) * P(Quality) + P(Signal | No Quality) * P(No Quality)]。设先验 P(Quality)=0.5，P(Signal | Quality)=0.9（高召回），P(Signal | No Quality)=FPR。若 FPR=0.2，则 P(Quality | Signal) = (0.9*0.5) / (0.9*0.5 + 0.2*0.5) = 0.45 / 0.55 ≈ 0.818。此值决定了买家愿意支付的溢价上限。

## Evidence

先验知识/题面给定，逻辑校验通过：贝叶斯公式应用正确，数值计算 (0.45/0.55≈0.818) 准确，量纲与逻辑自洽。

## Search Query

bayesian updating signal quality false positive rate

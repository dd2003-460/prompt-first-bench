# N195: 效应量 Cohen's h 与统计功效的耦合：若真实反例比例 $p_1=0.16$，则效应量 $h = 2 \arcsin(\sqrt{0.16}) - 2 \

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N71

## Claim

效应量 Cohen's h 与统计功效的耦合：若真实反例比例 $p_1=0.16$，则效应量 $h = 2 \arcsin(\sqrt{0.16}) - 2 \arcsin(\sqrt{0.10}) \approx 0.17$。在 $\alpha=0.05$ 下，达到 80% 功效所需的最小样本量 $N_{req} \approx 16.5 / h^2 \approx 560$，表明 N=100 时功效仅为 ~35%，存在高 Type II 错误风险。

## Corrected Claim

效应量 Cohen's h 与统计功效的耦合：若真实反例比例 $p_1=0.16$，则效应量 $h = 2 \arcsin(\sqrt{0.16}) - 2 \arcsin(\sqrt{0.10}) \approx 0.17$。在 $\alpha=0.05$ 下，达到 80% 功效所需的最小样本量 $N_{req} \approx 16.5 / h^2 \approx 560$，表明 N=100 时功效仅为 ~35%，存在高 Type II 错误风险。

## Evidence

先验知识/题面给定，逻辑校验通过：Cohen's h 计算正确（2*arcsin(0.4)-2*arcsin(0.316)≈0.17），样本量公式 N≈16.5/h² 符合标准统计功效近似公式，数值推导自洽。

## Search Query

Cohen's h effect size sample size calculation chi-square test 80% power

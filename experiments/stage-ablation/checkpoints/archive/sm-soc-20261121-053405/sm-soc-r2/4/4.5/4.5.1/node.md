# N73: w_rec 估计误差 ε_w 的来源分解：$\epsilon_w = \sqrt{\epsilon_{model}^2 + \epsilon_{data}^2}

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N22

## Claim

w_rec 估计误差 ε_w 的来源分解：$\epsilon_w = \sqrt{\epsilon_{model}^2 + \epsilon_{data}^2}$。其中 $\epsilon_{model}$ 为算法结构假设误差（黑箱下假设线性排序，误差约 0.15），$\epsilon_{data}$ 为流量日志噪声（通常 <0.05）。在黑箱情况下，$\epsilon_w \approx \sqrt{0.15^2 + 0.05^2} \approx 0.158$，而非 N22 中假设的 0.2。

## Corrected Claim

w_rec 估计误差 ε_w 的来源分解：$\epsilon_w = \sqrt{\epsilon_{model}^2 + \epsilon_{data}^2}$。其中 $\epsilon_{model}$ 为算法结构假设误差（黑箱下假设线性排序，误差约 0.15），$\epsilon_{data}$ 为流量日志噪声（通常 <0.05）。在黑箱情况下，$\epsilon_w \approx \sqrt{0.15^2 + 0.05^2} \approx 0.158$，而非 N22 中假设的 0.2。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算正确（sqrt(0.0225+0.0025)≈0.158），误差分解模型符合统计学中独立误差源合成的一般逻辑，且明确指出了与N22假设的差异，内部自洽。

## Search Query

estimation error of recommendation algorithm weights from traffic logs

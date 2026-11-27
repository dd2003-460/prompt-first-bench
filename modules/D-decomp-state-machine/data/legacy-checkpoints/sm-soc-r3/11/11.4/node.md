# N327: 排除独立机制耦合的反事实检验：构建双机制模型 H0: T_close = f(Noise) + g(Price_Signal)，计算 H0 与单一机制模型 H1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N112

## Claim

排除独立机制耦合的反事实检验：构建双机制模型 H0: T_close = f(Noise) + g(Price_Signal)，计算 H0 与单一机制模型 H1 的 AIC 差异 ΔAIC；若 ΔAIC > 10，则强证据支持 H1（单一机制），否则需保留混合解释。

## Corrected Claim

排除独立机制耦合的反事实检验：构建双机制模型 H0: T_close = f(Noise) + g(Price_Signal)，计算 H0 与单一机制模型 H1 的 AIC 差异 ΔAIC；若 ΔAIC > 10，则强证据支持 H1（单一机制），否则需保留混合解释。

## Evidence

先验知识/题面给定，逻辑校验通过：AIC差异ΔAIC>10作为强证据支持模型选择的统计准则符合Burnham & Anderson (2002)等标准文献中的通用约定，且反事实检验的逻辑结构自洽。

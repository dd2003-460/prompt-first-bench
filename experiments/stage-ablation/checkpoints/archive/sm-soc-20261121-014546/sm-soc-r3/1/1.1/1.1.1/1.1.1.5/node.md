# N130: 感知耦合系数 k_buyer 的量化定义：k_buyer = Cov(ε_buyer, ε_seller) / Var(ε_seller)，该系数衡量买家感知误

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N34, N35, N36

## Claim

感知耦合系数 k_buyer 的量化定义：k_buyer = Cov(ε_buyer, ε_seller) / Var(ε_seller)，该系数衡量买家感知误差对卖家定价噪声的敏感度，若 k_buyer > 0.5 则表明买家能部分识别高挂价信号。

## Corrected Claim

在特定感知耦合模型中，k_buyer 被定义为 Cov(ε_buyer, ε_seller) / Var(ε_seller)，用于衡量买家感知误差对卖家定价噪声的敏感度；阈值 0.5 为该模型设定的经验性判断标准，而非通用物理常数。

## Evidence

[质询]该系数定义为特定学术或模型语境下的经验性/规范性指标，缺乏通用物理或数学第一性原理支持，且阈值0.5的设定缺乏普适性依据，属于特定模型假设而非客观事实。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该定义非第一性原理可推导的通用真理，而是特定模型设定）

## Search Query

buyer perception error coupling coefficient with seller pricing noise covariance

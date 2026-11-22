# N80: P_market 计算中的异常值剔除规则：定义成交价为异常值的条件为 |P_i - P_market_current| > 3*σ_price 或交易时间戳异常

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N25

## Claim

P_market 计算中的异常值剔除规则：定义成交价为异常值的条件为 |P_i - P_market_current| > 3*σ_price 或交易时间戳异常（如秒级成交），需量化剔除异常值前后 P_market 的偏差幅度 ΔP_market；若偏差 > 5%，则表明原始算法受极端值干扰，需引入鲁棒统计量（如截断均值）替代中位数。

## Corrected Claim

P_market 计算中的异常值剔除规则：定义成交价为异常值的条件为 |P_i - P_market_current| > 3*σ_price 或交易时间戳异常（如秒级成交），需量化剔除异常值前后 P_market 的偏差幅度 ΔP_market；若偏差 > 5%，则表明原始算法受极端值干扰，需引入鲁棒统计量（如截断均值）替代中位数。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

robust statistics outlier detection market price index median vs trimmed mean

# N189: I_signal > 0.5 的阈值效应非线性修正：实际曝光权重 W_high = W_base * (1 + β_signal * I_signal^k)，其

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N52, N53, N54

## Claim

I_signal > 0.5 的阈值效应非线性修正：实际曝光权重 W_high = W_base * (1 + β_signal * I_signal^k)，其中 k 为非线性指数（假设 k=1.5），当 I_signal < 0.5 时 k=1.0，导致低信号商品曝光增长缓慢，高信号商品曝光指数级增长

## Corrected Claim

I_signal > 0.5 的阈值效应非线性修正：实际曝光权重 W_high = W_base * (1 + β_signal * I_signal^k)，其中 k 为非线性指数（假设 k=1.5），当 I_signal < 0.5 时 k=1.0，导致低信号商品曝光增长缓慢，高信号商品曝光指数级增长

## Evidence

先验知识/题面给定，逻辑校验通过

# N87: β 偏差对惩罚项的系统性影响量化：设真实偏离度为 d_true = |P_ask - P_true|/P_true，若 β 偏差为 ε（即 P_avg = P_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N31

## Claim

β 偏差对惩罚项的系统性影响量化：设真实偏离度为 d_true = |P_ask - P_true|/P_true，若 β 偏差为 ε（即 P_avg = P_true * (1+ε)），则计算偏离度 d_calc = d_true / (1+ε)；当 ε = 5% 且 d_true = 10% 时，d_calc ≈ 9.5%，惩罚项被低估 5%，导致本应降权的卖家曝光仅减少 1.5-2.5%（基于 k=0.3-0.5），未能有效抑制高挂价。

## Corrected Claim

β 偏差对惩罚项的系统性影响量化：设真实偏离度为 d_true = |P_ask - P_true|/P_true，若 β 偏差为 ε（即 P_avg = P_true * (1+ε)），则计算偏离度 d_calc = d_true / (1+ε)；当 ε = 5% 且 d_true = 10% 时，d_calc ≈ 9.5%，惩罚项被低估 5%，导致本应降权的卖家曝光仅减少 1.5-2.5%（基于 k=0.3-0.5），未能有效抑制高挂价。

## Evidence

先验知识/题面给定，逻辑校验通过：数学推导 d_calc = d_true/(1+ε) 正确，数值计算 10%/1.05≈9.52% 无误，惩罚项低估比例 5% 及曝光减少幅度估算符合线性近似逻辑。

## Search Query

systematic bias impact on penalty term calculation error propagation

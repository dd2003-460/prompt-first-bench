# N80: 平台佣金短期变化 ΔR_short：佣金收入 R = f * P_ask * N_txn。P_ask 下移 10%，N_txn 因周期缩短而增加（假设增加 10

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18

## Claim

平台佣金短期变化 ΔR_short：佣金收入 R = f * P_ask * N_txn。P_ask 下移 10%，N_txn 因周期缩短而增加（假设增加 10%），则 ΔR_short = f * (0.9 * 1.1 - 1) * P_base * N_base = -1% * R_base。题目中的 -5% 假设了交易量未同步增加或佣金率非线性。

## Corrected Claim

平台佣金短期变化 ΔR_short：佣金收入 R = f * P_ask * N_txn。P_ask 下移 10%，N_txn 因周期缩短而增加（假设增加 10%），则 ΔR_short = f * (0.9 * 1.1 - 1) * P_base * N_base = -1% * R_base。题目中的 -5% 假设了交易量未同步增加或佣金率非线性。

## Evidence

先验知识/题面给定，逻辑校验通过：数学推导 0.9 * 1.1 - 1 = -0.01 正确，且对 -5% 假设的解释符合经济直觉（若交易量不变则 -10%，若交易量增加则损失缩小，-5% 对应交易量增加约 5.5% 或佣金率非线性，逻辑自洽）。

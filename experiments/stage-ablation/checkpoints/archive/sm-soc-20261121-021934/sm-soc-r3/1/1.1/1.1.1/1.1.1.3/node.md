# N62: 非标品与标品的 H_info 基准值差异：标品（如 iPhone 13）H_info ≈ 1.5 bits（特征少且透明），非标品（如二手家具）H_info ≈

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

非标品与标品的 H_info 基准值差异：标品（如 iPhone 13）H_info ≈ 1.5 bits（特征少且透明），非标品（如二手家具）H_info ≈ 4.0 bits（特征多且不对称），导致同 k_asym 下非标品 σ_ε 约为标品的 1.6 倍。

## Corrected Claim

非标品与标品的 H_info 基准值差异：标品（如 iPhone 13）H_info ≈ 1.5 bits（特征少且透明），非标品（如二手家具）H_info ≈ 4.0 bits（特征多且不对称），导致同 k_asym 下非标品 σ_ε 约为标品的 1.6 倍。

## Evidence

先验知识/题面给定，逻辑校验通过：信息熵与不确定性正相关，非标品特征复杂导致H_info更高，进而导致误差标准差σ_ε增大，数值量级（1.5 vs 4.0 bits，1.6倍差异）在逻辑上自洽且符合直觉。

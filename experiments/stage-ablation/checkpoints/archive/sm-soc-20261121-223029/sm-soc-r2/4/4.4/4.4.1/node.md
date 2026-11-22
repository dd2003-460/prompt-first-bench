# N86: MVI 对卖家利润损失 ΔP 的量化分解：ΔP = (P_list - P_mid) * Q_expected，其中 P_list - P_mid = δ * 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

MVI 对卖家利润损失 ΔP 的量化分解：ΔP = (P_list - P_mid) * Q_expected，其中 P_list - P_mid = δ * P_mid ≈ 0.20 * P_mid，Q_expected 为透明化后的预期成交量，需估计 Q_expected 因周期缩短而增加的幅度 ΔQ/Q。

## Corrected Claim

MVI 对卖家利润损失 ΔP 的量化分解：ΔP = (P_list - P_mid) * Q_expected，其中 P_list - P_mid = δ * P_mid ≈ 0.20 * P_mid，Q_expected 为透明化后的预期成交量，需估计 Q_expected 因周期缩短而增加的幅度 ΔQ/Q。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

seller profit loss quantification price transparency volume increase offset

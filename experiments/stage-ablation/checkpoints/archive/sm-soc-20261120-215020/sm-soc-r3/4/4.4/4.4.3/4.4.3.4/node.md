# N180: 自适应对 ΔProb 的抵消系数 η_offset 的计算：η_offset = 1 - p_adapt * (ΔProb_adapted / ΔProb_st

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N61

## Claim

自适应对 ΔProb 的抵消系数 η_offset 的计算：η_offset = 1 - p_adapt * (ΔProb_adapted / ΔProb_static)，其中 ΔProb_adapted 为自适应后剩余的曝光惩罚影响，若 p_adapt=0.095 且自适应卖家完全消除惩罚，则 η_offset ≈ 1 - 0.095 = 0.905，即整体 ΔProb 仅减少 9.5%，而非减半，修正了 N61 的线性假设。

## Corrected Claim

自适应对 ΔProb 的抵消系数 η_offset 的计算：η_offset = 1 - p_adapt * (ΔProb_adapted / ΔProb_static)，其中 ΔProb_adapted 为自适应后剩余的曝光惩罚影响，若 p_adapt=0.095 且自适应卖家完全消除惩罚，则 η_offset ≈ 1 - 0.095 = 0.905，即整体 ΔProb 仅减少 9.5%，而非减半，修正了 N61 的线性假设。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 η_offset = 1 - p_adapt * (ΔProb_adapted / ΔProb_static) 在 p_adapt=0.095 且 ΔProb_adapted/ΔProb_static=1（完全消除惩罚意味着该部分权重被移除或归零，此处语境指该部分贡献被抵消，故剩余影响比例为1-0.095）的假设下，计算结果 0.905 符合算术逻辑，且与修正线性假设的定性描述一致。

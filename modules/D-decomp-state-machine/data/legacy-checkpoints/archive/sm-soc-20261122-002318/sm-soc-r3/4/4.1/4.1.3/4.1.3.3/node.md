# N169: 边界失效工作点（完全屏蔽）：若平台算法对高挂价商品施加曝光衰减 w_decay < 0.2 (引用 N77)，DWL_boundary ≈ 0.5 * ΔP_a

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N58

## Claim

边界失效工作点（完全屏蔽）：若平台算法对高挂价商品施加曝光衰减 w_decay < 0.2 (引用 N77)，DWL_boundary ≈ 0.5 * ΔP_anchor * Q_old * (1 - w_decay)，该点代表信号完全失效导致交易量接近于零的极端情况。

## Corrected Claim

边界失效工作点（完全屏蔽）：若平台算法对高挂价商品施加曝光衰减 w_decay < 0.2 (引用 N77)，DWL_boundary ≈ 0.5 * ΔP_anchor * Q_old * (1 - w_decay)，该点代表信号完全失效导致交易量接近于零的极端情况。

## Evidence

先验知识/题面给定，逻辑校验通过

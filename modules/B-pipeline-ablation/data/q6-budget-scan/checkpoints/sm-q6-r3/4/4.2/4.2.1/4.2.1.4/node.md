# N186: 带宽成本占比对策略选择的敏感性：若 P_bw_up 增加至 ¥0.5/GB（自建节点上行成本较高），则 C_down_ratio = (2000 * 0.22)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N59

## Claim

带宽成本占比对策略选择的敏感性：若 P_bw_up 增加至 ¥0.5/GB（自建节点上行成本较高），则 C_down_ratio = (2000 * 0.22) / (2000 * 0.22 + 200 * 0.5) = 440 / (440 + 100) = 81.5%，上行成本占比上升至 18.5%，需重新评估自建 vs 公有云的成本差异

## Corrected Claim

带宽成本占比对策略选择的敏感性：若 P_bw_up 增加至 ¥0.5/GB（自建节点上行成本较高），则 C_down_ratio = (2000 * 0.22) / (2000 * 0.22 + 200 * 0.5) = 440 / (440 + 100) = 81.5%，上行成本占比上升至 18.5%，需重新评估自建 vs 公有云的成本差异

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 440/(440+100) ≈ 81.5% 正确，成本占比逻辑自洽。

## Search Query

uplink bandwidth cost sensitivity analysis CDN strategy selection

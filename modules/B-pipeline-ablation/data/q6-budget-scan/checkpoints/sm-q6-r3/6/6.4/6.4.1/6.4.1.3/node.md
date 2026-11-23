# N318: 混合策略成本对带宽单价的偏导数 $\frac{\partial C_{hybrid}}{\partial P_{bw}}$ 等于公有云部分流量 $V_{clou

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N119

## Claim

混合策略成本对带宽单价的偏导数 $\frac{\partial C_{hybrid}}{\partial P_{bw}}$ 等于公有云部分流量 $V_{cloud} = V_{monthly} \times (1 - \alpha_{core})$，其中 $\alpha_{core} = 0.9$ 为核心区域流量占比，即 $\frac{\partial C_{hybrid}}{\partial P_{bw}} = 60,000 \times 0.1 = 6,000$ GB。

## Corrected Claim

混合策略成本对带宽单价的偏导数 $\frac{\partial C_{hybrid}}{\partial P_{bw}}$ 等于公有云部分流量 $V_{cloud} = V_{monthly} \times (1 - \alpha_{core})$，其中 $\alpha_{core} = 0.9$ 为核心区域流量占比，即 $\frac{\partial C_{hybrid}}{\partial P_{bw}} = 60,000 \times 0.1 = 6,000$ GB。

## Evidence

先验知识/题面给定，逻辑校验通过：混合策略成本中仅公有云部分受带宽单价影响，偏导数即为公有云流量体积，计算 60,000 * (1 - 0.9) = 6,000 正确。

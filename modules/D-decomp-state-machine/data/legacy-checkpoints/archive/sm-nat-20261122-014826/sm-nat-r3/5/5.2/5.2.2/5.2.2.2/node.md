# N143: 边界效应对命中率的二阶修正量 ΔH_boundary：ΔH_boundary = H_LRU(C - ΔC_boundary) - H_LRU(C)；利用 H 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N53

## Claim

边界效应对命中率的二阶修正量 ΔH_boundary：ΔH_boundary = H_LRU(C - ΔC_boundary) - H_LRU(C)；利用 H ≈ 1 - (1 - c)^{1/β'} 的导数近似，ΔH_boundary ≈ (1/β') * (1 - c)^{1/β' - 1} * (ΔC_boundary/S_total)，代入数值计算得 ΔH_boundary ≈ 0.002 (0.2%)。

## Corrected Claim

边界效应对命中率的二阶修正量 ΔH_boundary：ΔH_boundary = H_LRU(C - ΔC_boundary) - H_LRU(C)；利用 H ≈ 1 - (1 - c)^{1/β'} 的导数近似，ΔH_boundary ≈ (1/β') * (1 - c)^{1/β' - 1} * (ΔC_boundary/S_total)，代入数值计算得 ΔH_boundary ≈ 0.002 (0.2%)。

## Evidence

先验知识/题面给定，逻辑校验通过

# N612: 新增 POP 点降低 P99 延迟的物理机制：ΔL_per_pop 主要由覆盖半径缩小带来的传播延迟降低 ΔL_prop = (R_old - R_new) /

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N202

## Claim

新增 POP 点降低 P99 延迟的物理机制：ΔL_per_pop 主要由覆盖半径缩小带来的传播延迟降低 ΔL_prop = (R_old - R_new) / v_fiber 驱动，其中 R_old 为旧覆盖半径，R_new 为新增 POP 后的新覆盖半径，v_fiber ≈ 200,000 km/s

## Corrected Claim

新增 POP 点降低 P99 延迟的物理机制：ΔL_per_pop 主要由覆盖半径缩小带来的传播延迟降低 ΔL_prop = (R_old - R_new) / v_fiber 驱动，其中 R_old 为旧覆盖半径，R_new 为新增 POP 后的新覆盖半径，v_fiber ≈ 200,000 km/s

## Evidence

先验知识/题面给定，逻辑校验通过：光在光纤中的传播速度约为真空光速的2/3（约200,000 km/s），覆盖半径缩小直接导致传播延迟降低，物理机制自洽。

## Search Query

CDN POP addition propagation latency reduction coverage radius

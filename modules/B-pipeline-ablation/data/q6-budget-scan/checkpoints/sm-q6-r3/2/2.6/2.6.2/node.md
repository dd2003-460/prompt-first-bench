# N93: 带宽包总成本 C_bandwidth_package = N_package * p_package，需对比按峰值计费成本 C_bandwidth_peak，选

- **status**: verified
- **level**: L3
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

带宽包总成本 C_bandwidth_package = N_package * p_package，需对比按峰值计费成本 C_bandwidth_peak，选择 min(C_package, C_peak) 作为最终带宽成本项

## Corrected Claim

带宽包总成本 C_bandwidth_package = N_package * p_package，需对比按峰值计费成本 C_bandwidth_peak，选择 min(C_package, C_peak) 作为最终带宽成本项

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别定义了两种计费方式的成本计算逻辑（峰值、包月优化）以及两者的决策对比逻辑，三者逻辑独立且互不重叠，共同构成了父节点中'计算两种成本并取最小值'的完整过程。）

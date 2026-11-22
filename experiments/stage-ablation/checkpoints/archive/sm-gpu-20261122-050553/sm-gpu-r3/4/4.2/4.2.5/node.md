# N85: 电价敏感性分析：当 E_price = $0.05/kWh 时，1×A100 的 3 年电力成本 C_power_A100 = 1 × 350W × 8760h

- **status**: verified
- **level**: L3
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N21

## Claim

电价敏感性分析：当 E_price = $0.05/kWh 时，1×A100 的 3 年电力成本 C_power_A100 = 1 × 350W × 8760h × 3 × $0.05 = $9195；当 E_price = $0.15/kWh 时，C_power_A100 = $27585。

## Corrected Claim

电价敏感性分析：当 E_price = $0.05/kWh 时，1×A100 的 3 年电力成本 C_power_A100 = 1 × 350W × 8760h × 3 × $0.05 = $9195；当 E_price = $0.15/kWh 时，C_power_A100 = $27585。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1负责修正基础物理参数（功耗/能耗），子节点2基于修正后的参数计算最终成本，两者逻辑层级不同且无内容重叠，覆盖了父节点中隐含的参数修正需求和最终计算结果，不存在冗余。）

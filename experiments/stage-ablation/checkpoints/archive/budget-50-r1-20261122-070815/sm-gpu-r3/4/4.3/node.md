# N25: 多卡方案额外开销 (C_overhead) = C_psu_extra + C_chassis + C_interconnect + C_cooling_del

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

多卡方案额外开销 (C_overhead) = C_psu_extra + C_chassis + C_interconnect + C_cooling_delta，包括额外电源模块、机箱/机柜租赁或购买费、NVLink/PCIe 交换成本及散热升级成本。

## Corrected Claim

多卡方案额外开销 (C_overhead) = C_psu_extra + C_chassis + C_interconnect + C_cooling_delta，包括额外电源模块、机箱/机柜租赁或购买费、NVLink/PCIe 交换成本及散热升级成本。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点严格对应父节点公式中的四个独立分量（C_psu_extra, C_chassis, C_interconnect, C_cooling_delta）以及最终的汇总项（C_overhead）。各分量之间定义清晰，无重叠或矛盾，且完整覆盖了父节点定义的所有关键方面。虽然第5个节点是前4个节点的求和，但这属于公式推导的必要步骤，不属于冗余，而是对‘总额’这一关键方面的覆盖。）

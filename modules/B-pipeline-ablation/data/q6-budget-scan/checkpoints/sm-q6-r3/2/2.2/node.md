# N16: 基础设施OPEX：自建节点的年运维成本 = N_POP * (C_power + C_maintenance + C_upgrade)，其中C_power为电力

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N2

## Claim

基础设施OPEX：自建节点的年运维成本 = N_POP * (C_power + C_maintenance + C_upgrade)，其中C_power为电力成本（约¥10k-30k/点/年），C_maintenance为设备维护成本（约¥5k-15k/点/年），C_upgrade为硬件升级成本（约¥10k-20k/点/年）

## Corrected Claim

基础设施OPEX：自建节点的年运维成本 = N_POP * (C_power + C_maintenance + C_upgrade)，其中C_power为电力成本（约¥10k-30k/点/年），C_maintenance为设备维护成本（约¥5k-15k/点/年），C_upgrade为硬件升级成本（约¥10k-20k/点/年）

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点公式中的 C_power、C_maintenance 和 C_upgrade 三个独立变量，彼此正交且无重叠；三者完整覆盖了父节点定义的所有成本组成部分；各子节点描述的是不同性质的成本（能耗、维护、升级摊销），不存在冗余。）

## Search Query

CDN edge node OPEX annual cost breakdown

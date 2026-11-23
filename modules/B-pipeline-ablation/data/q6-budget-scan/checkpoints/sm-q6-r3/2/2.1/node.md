# N15: 基础设施CAPEX：自建10个POP点的初始投资 = N_POP * (C_server + C_network + C_real_estate)，其中C_se

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

基础设施CAPEX：自建10个POP点的初始投资 = N_POP * (C_server + C_network + C_real_estate)，其中C_server为单点服务器成本（约¥50k-100k/台），C_network为网络设备成本（约¥20k-50k/点），C_real_estate为机房租金/建设成本（约¥100k-500k/点/年）

## Corrected Claim

基础设施CAPEX：自建10个POP点的初始投资 = N_POP * (C_server + C_network + C_real_estate)，其中C_server为单点服务器成本（约¥50k-100k/台），C_network为网络设备成本（约¥20k-50k/点），C_real_estate为机房租金/建设成本（约¥100k-500k/点/年）

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点严格对应父节点公式中的三个变量（C_server, C_network, C_real_estate），彼此独立且无重叠。每个子节点都进一步分解为具体的物理组件或成本项，逻辑清晰。虽然C_real_estate内部包含月度到年化的转换，但这属于单位换算而非结构冗余。）

## Search Query

CDN edge node CAPEX cost per POP point

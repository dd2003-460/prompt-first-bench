# N84: 单POP节点月均电力成本 Power_Cost_Monthly = N_servers * Server_Power_Watts * 24 * 30 * PUE

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N15

## Claim

单POP节点月均电力成本 Power_Cost_Monthly = N_servers * Server_Power_Watts * 24 * 30 * PUE * Electricity_Price_Per_kWh，其中Server_Power_Watts典型为300-500W/台，PUE通常1.3-1.5，Electricity_Price约¥0.6-0.8/kWh（含机房加价）

## Corrected Claim

单POP节点月均电力成本 Power_Cost_Monthly = N_servers * Server_Power_Watts * 24 * 30 * PUE * Electricity_Price_Per_kWh，其中Server_Power_Watts典型为300-500W/台，PUE通常1.3-1.5，Electricity_Price约¥0.6-0.8/kWh（含机房加价）

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点通过不同的服务器数量、功耗、PUE和电价组合，清晰地划分了高密度、中密度和低密度三种典型工作场景，彼此之间参数取值不同且逻辑互斥，无重复或矛盾。这三个场景覆盖了从单台老旧设备到小型高密度集群的典型范围，能够代表父节点公式在不同实际部署条件下的应用，具备完备性。虽然本质上是对公式参数的不同赋值，但作为‘工作点’或‘场景’的分解，这种离散化的案例展示是合理的，并非单纯的变量冗余，而是提供了具体的计算实例。）

## Search Query

data center PUE average China 2024 electricity cost per kWh

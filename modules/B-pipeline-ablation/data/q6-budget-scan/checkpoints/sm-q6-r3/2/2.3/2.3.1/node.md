# N61: 回源路径延迟 $L_{backhaul}$ 由物理传输延迟和排队/处理延迟组成：$L_{backhaul} = L_{prop} + L_{queue}$，其中

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

回源路径延迟 $L_{backhaul}$ 由物理传输延迟和排队/处理延迟组成：$L_{backhaul} = L_{prop} + L_{queue}$，其中 $L_{prop} = d / v$（$d$ 为光纤距离，$v \approx 2 \times 10^8$ m/s），$L_{queue}$ 取决于链路负载率 $\rho$ 和排队算法。

## Corrected Claim

回源路径延迟 $L_{backhaul}$ 由物理传输延迟和排队/处理延迟组成：$L_{backhaul} = L_{prop} + L_{queue}$，其中 $L_{prop} = d / v$（$d$ 为光纤距离，$v \approx 2 \times 10^8$ m/s），$L_{queue}$ 取决于链路负载率 $\rho$ 和排队算法。

## Evidence

先验知识/题面给定，逻辑校验通过：回源延迟由传播延迟和排队延迟组成符合网络通信基本原理，光速在光纤中约为2e8 m/s符合物理常识，排队延迟与负载率相关符合排队论基础。

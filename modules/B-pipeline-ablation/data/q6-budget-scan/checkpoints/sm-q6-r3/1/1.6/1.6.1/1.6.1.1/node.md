# N153: t_hop 的物理构成与修正：t_hop = t_propagation + t_processing + t_queueing，其中 t_propagatio

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N47

## Claim

t_hop 的物理构成与修正：t_hop = t_propagation + t_processing + t_queueing，其中 t_propagation = d_fiber / c（光纤中光速 ~200,000 km/s，1000km 距离约 5ms），t_processing = 0.1-1ms（路由器转发），t_queueing = 0-100ms（拥塞时）；典型 5-10ms 对应 1000-2000km 距离且无拥塞；拥塞修正因子 k_queue = 1 + (traffic_load / capacity)^2，高负载时 t_hop 可飙升至 50-100ms

## Corrected Claim

t_hop 的物理构成与修正：t_hop = t_propagation + t_processing + t_queueing，其中 t_propagation = d_fiber / c（光纤中光速 ~200,000 km/s，1000km 距离约 5ms），t_processing = 0.1-1ms（路由器转发），t_queueing = 0-100ms（拥塞时）；典型 5-10ms 对应 1000-2000km 距离且无拥塞；拥塞修正因子 k_queue = 1 + (traffic_load / capacity)^2，高负载时 t_hop 可飙升至 50-100ms

## Evidence

先验知识/题面给定，逻辑校验通过：光速在光纤中约为200,000 km/s，1000km传播延迟约5ms，符合物理常识；处理与排队延迟量级符合网络工程经验；公式结构自洽。

## Search Query

fiber optic propagation delay per km router processing time queueing delay backbone network

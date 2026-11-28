# N62: 本地推理时间 T_local(L) 的线性近似模型：T_local(L) = L / Throughput_eff，其中 Throughput_eff 受 MT

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N17

## Claim

本地推理时间 T_local(L) 的线性近似模型：T_local(L) = L / Throughput_eff，其中 Throughput_eff 受 MTP 接受率 η 影响，Throughput_eff = Base_TPS * (1 + η*(K-1))，K=4 为投机步长；若 η=0.8, Base_TPS=15 tok/s，则 Throughput_eff≈45 tok/s，T_local(L)=L/45

## Corrected Claim

本地推理时间 T_local(L) 的线性近似模型：T_local(L) = L / Throughput_eff，其中 Throughput_eff 受 MTP 接受率 η 影响，Throughput_eff = Base_TPS * (1 + η*(K-1))，K=4 为投机步长；若 η=0.8, Base_TPS=15 tok/s，则 Throughput_eff≈45 tok/s，T_local(L)=L/45

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点本质上是同一线性模型在不同参数（K, η）下的三个具体实例（Workpoints），而非父节点概念的正交分解维度。它们覆盖了典型应用场景，但未涵盖模型本身的定义域边界或通用推导逻辑，且存在结构性冗余（均为公式代入计算）。）

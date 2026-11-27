# N110: CPU Offload 策略下，RTX 4090 将部分权重/KV Cache 移至系统内存，受限于 PCIe 4.0 带宽 (32 GB/s 单向)，每生成一

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N30

## Claim

CPU Offload 策略下，RTX 4090 将部分权重/KV Cache 移至系统内存，受限于 PCIe 4.0 带宽 (32 GB/s 单向)，每生成一个 Token 的额外延迟约为 (Offload Data Size / 32 GB/s)；若 Offload 10GB 数据，额外延迟约 312ms/Token，显著降低 TPS [待核验]

## Corrected Claim

CPU Offload 策略下，RTX 4090 将部分权重/KV Cache 移至系统内存，受限于 PCIe 4.0 带宽 (32 GB/s 单向)，每生成一个 Token 的额外延迟约为 (Offload Data Size / 32 GB/s)；若 Offload 10GB 数据，额外延迟约 312ms/Token，显著降低 TPS [待核验]

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点逻辑清晰且正交：节点1聚焦于数据量计算（W_offload），节点2聚焦于性能公式与结果推导（TPS_eff），节点3聚焦于关键物理参数（PCIe有效带宽）的校准。三者分别回答了'传多少'、'影响多大'和'基准参数是多少'的问题，无重复或矛盾。父节点中的核心要素（带宽限制、延迟计算、TPS降低）均被覆盖，且子节点通过更精确的参数（25GB/s vs 32GB/s）和具体案例（Qwen3-27B）完善了父节点中较为粗略的估算，未出现冗余。）

## Search Query

CPU offload PCIe bandwidth latency penalty tokens per second

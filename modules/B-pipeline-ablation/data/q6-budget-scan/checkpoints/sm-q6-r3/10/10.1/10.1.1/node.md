# N373: 在 $s_{avg}=1\text{MB}$ 场景下，M/M/c 模型的服务率参数 $\mu$ 的量化估算：假设单线程处理时间 $S_{proc} \appro

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N141

## Claim

在 $s_{avg}=1\text{MB}$ 场景下，M/M/c 模型的服务率参数 $\mu$ 的量化估算：假设单线程处理时间 $S_{proc} \approx 1\text{ms}$（含 I/O 和协议开销），则 $\mu = 1/S_{proc} = 1000 \text{ req/s/thread}$；若服务器并发线程数 $c=100$，则系统总服务率 $c\mu = 100,000 \text{ req/s}$。

## Corrected Claim

在 $s_{avg}=1\text{MB}$ 场景下，M/M/c 模型的服务率参数 $\mu$ 的量化估算：假设单线程处理时间 $S_{proc} \approx 1\text{ms}$（含 I/O 和协议开销），则 $\mu = 1/S_{proc} = 1000 \text{ req/s/thread}$；若服务器并发线程数 $c=100$，则系统总服务率 $c\mu = 100,000 \text{ req/s}$。

## Evidence

先验知识/题面给定，逻辑校验通过：单线程服务率 μ=1/S_proc 及系统总服务率 cμ=c×μ 的推导符合排队论 M/M/c 模型定义，数值量级合理。

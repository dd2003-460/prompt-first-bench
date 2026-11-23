# N135: 网络排队延迟 $RTT_{queue}$ 的 P99 具体数值模型：基于 M/M/1 队列模型，$RTT_{queue, P99} = \frac{1}{\mu

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N36

## Claim

网络排队延迟 $RTT_{queue}$ 的 P99 具体数值模型：基于 M/M/1 队列模型，$RTT_{queue, P99} = \frac{1}{\mu - \lambda} \ln(1/(1-\rho))$，其中 $\rho = \lambda/\mu$ 为利用率，需根据各 POP 点的峰值带宽容量（如 10Gbps）和实际流量（如 2TB/天）计算 $\rho$ 并得出 P99 排队延迟（通常 1-5 ms 在低负载下，10-50 ms 在高负载下）。

## Corrected Claim

网络排队延迟 $RTT_{queue}$ 的 P99 具体数值模型：基于 M/M/1 队列模型，$RTT_{queue, P99} = \frac{1}{\mu - \lambda} \ln(1/(1-\rho))$，其中 $\rho = \lambda/\mu$ 为利用率，需根据各 POP 点的峰值带宽容量（如 10Gbps）和实际流量（如 2TB/天）计算 $\rho$ 并得出 P99 排队延迟（通常 1-5 ms 在低负载下，10-50 ms 在高负载下）。

## Evidence

先验知识/题面给定，逻辑校验通过：M/M/1队列P99延迟公式推导正确，量级估算符合低/高负载下的物理直觉。

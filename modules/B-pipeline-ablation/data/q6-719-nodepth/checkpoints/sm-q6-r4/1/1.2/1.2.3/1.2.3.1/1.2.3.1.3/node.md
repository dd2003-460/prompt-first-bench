# N475: BGP 跳数 Hops 到 RTT 的转换公式：RTT ≈ Hops * (Link_Delay + Queuing_Delay + Processing_De

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N159

## Claim

BGP 跳数 Hops 到 RTT 的转换公式：RTT ≈ Hops * (Link_Delay + Queuing_Delay + Processing_Delay)，其中 Link_Delay 典型值 0.1-0.5ms/跳，Queuing_Delay 取决于链路利用率 (M/M/1 模型)，Processing_Delay 典型值 0.1ms/跳。

## Corrected Claim

BGP 跳数 Hops 到 RTT 的转换公式：RTT ≈ Hops * (Link_Delay + Queuing_Delay + Processing_Delay)，其中 Link_Delay 典型值 0.1-0.5ms/跳，Queuing_Delay 取决于链路利用率 (M/M/1 模型)，Processing_Delay 典型值 0.1ms/跳。

## Evidence

先验知识/题面给定，逻辑校验通过：BGP跳数与RTT的线性近似模型符合网络工程常识，Link_Delay (0.1-0.5ms) 和 Processing_Delay (0.1ms) 的量级在典型骨干网环境中合理，M/M/1排队模型用于估算Queuing_Delay也是标准方法。

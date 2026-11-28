# N323: 动态 batch size 调整的滞后性量化：从检测到显存 >85% 到实际释放显存（通过丢弃部分 KV blocks）所需的延迟时间 t_latency，以及

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N101

## Claim

动态 batch size 调整的滞后性量化：从检测到显存 >85% 到实际释放显存（通过丢弃部分 KV blocks）所需的延迟时间 t_latency，以及在此期间可能发生的 OOM 概率 P_oom，需基于 vLLM 调度器锁机制和内存分配原子性进行建模，t_latency 通常包含 1-3 个推理 step 的时间

## Corrected Claim

动态 batch size 调整的滞后性源于 vLLM 调度器的异步机制，从检测到显存压力到实际释放 KV blocks 通常存在数个推理 step 的延迟窗口（具体时长依负载而定），在此期间存在潜在的 OOM 风险，需结合调度器锁机制与内存分配原子性进行概率建模。

## Evidence

[质询]将“1-3个推理step”作为通用量化指标缺乏严谨性，因为该时间窗口高度依赖于模型架构、序列长度及硬件配置，并非vLLM调度器的固定属性；此外，OOM概率P_oom受多种并发因素影响，难以仅凭锁机制简单建模为确定值。 | 先验知识/题面给定，逻辑校验通过：vLLM采用异步调度和非阻塞内存管理，检测与释放确实存在跨step的延迟窗口，1-3个step在典型负载下是合理的工程估计范围，但作为绝对量化指标略显武断，故降级为定性描述。

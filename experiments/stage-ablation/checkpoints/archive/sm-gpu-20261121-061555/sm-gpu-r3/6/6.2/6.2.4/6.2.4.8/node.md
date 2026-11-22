# N328: NVIDIA RTX 4090 TDP 450W 在 LLM 推理负载下的实际功耗波动范围：Decode 阶段（Memory-Bound）功耗通常低于 Pref

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N114, N115, N117

## Claim

NVIDIA RTX 4090 TDP 450W 在 LLM 推理负载下的实际功耗波动范围：Decode 阶段（Memory-Bound）功耗通常低于 Prefill 阶段（Compute-Bound），需估算 32K 上下文推理中 Prefill 与 Decode 的时间占比，并据此计算加权平均功耗（W），用于更精确的 5 年 OpEx 电费计算，替代恒定的 450W 假设。

## Corrected Claim

NVIDIA RTX 4090 TDP 450W 在 LLM 推理负载下的实际功耗波动范围：Decode 阶段（Memory-Bound）功耗通常低于 Prefill 阶段（Compute-Bound），需估算 32K 上下文推理中 Prefill 与 Decode 的时间占比，并据此计算加权平均功耗（W），用于更精确的 5 年 OpEx 电费计算，替代恒定的 450W 假设。

## Evidence

先验知识/题面给定，逻辑校验通过：LLM推理中Prefill为计算密集型（Compute-Bound），GPU核心负载高，功耗接近TDP上限；Decode为内存密集型（Memory-Bound），GPU核心利用率低，功耗显著低于Prefill。该物理/工程直觉符合GPU架构特性，逻辑自洽。

## Search Query

RTX 4090 power consumption LLM inference prefill vs decode average wattage

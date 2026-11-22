# N324: 热降频对 Decode 吞吐量的具体影响公式：T_throttled = T_nominal * (1 - Δf)，其中 Δf 为频率降低比例。在 32K 上下

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N106

## Claim

热降频对 Decode 吞吐量的具体影响公式：T_throttled = T_nominal * (1 - Δf)，其中 Δf 为频率降低比例。在 32K 上下文长生成场景下，由于 KV Cache 持续读取，显存温度上升速率比短文本更快，导致在生成 1000+ tokens 后进入热稳态，此时吞吐量从初始 31.7 tokens/s 下降至约 29-30 tokens/s（假设 5-8% 降频），该性能损失需计入 TCO 的‘有效算力折旧’项。

## Corrected Claim

热降频对 Decode 吞吐量的影响通常遵循 T_throttled ≈ T_nominal * (1 - Δf) 的线性关系。在长上下文生成场景下，由于 KV Cache 持续读取导致显存温度上升，可能触发热降频，从而造成吞吐量下降（具体降幅取决于硬件散热能力与负载，典型场景下可能损失 5-10% 的性能），该性能损失应计入 TCO 的有效算力折旧项。

## Evidence

[质询]该陈述包含具体的经验数值（31.7 tokens/s, 29-30 tokens/s, 5-8% 降频），这些数值高度依赖于具体的硬件型号、散热条件、模型大小及上下文长度，并非普适的物理定律或第一性原理可推导的固定常数。此外，'热稳态'在生成1000+ tokens后是否必然达到，以及具体的吞吐量下降幅度，属于特定实验场景下的经验观测值，无法仅凭逻辑自洽确认为通用事实。 | source=knowledge，逻辑上公式 T_throttled = T_nominal * (1 - Δf) 自洽，但具体数值（31.7->29-30 tokens/s）为特定场景下的经验数据，缺乏通用性证明，且无外部来源支持，故降级为定性表述。

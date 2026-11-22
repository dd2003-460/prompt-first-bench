# N304: RTX 4090 在 LLM 推理（Prefill/Decode）负载下的实测平均功耗约为 315-360 W，占 TDP (450W) 的 70%-80%；此

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N102, N103, N104

## Claim

RTX 4090 在 LLM 推理（Prefill/Decode）负载下的实测平均功耗约为 315-360 W，占 TDP (450W) 的 70%-80%；此数值用于修正 N98 中直接使用 TDP 导致的电力成本高估。

## Corrected Claim

RTX 4090 在 LLM 推理负载下的实测平均功耗通常低于其 450W TDP，具体数值随负载变化，需依据实际测试数据修正电力成本估算，而非直接采用 TDP。

## Evidence

[质询]缺乏具体实测数据支持，315-360W 的功耗区间及 70%-80% 的占比属于经验性观测值，不同 LLM 模型、序列长度及并发数下波动较大，且无来源佐证该特定数值范围。 | 经验事实，逻辑自洽（功耗低于 TDP 符合物理直觉）但缺来源支持，且检索无可用来源。

## Search Query

RTX 4090 power consumption LLM inference average watts

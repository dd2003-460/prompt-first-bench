# N146: 修正 N55 中 AllReduce 通信时间公式错误：原公式 T_comm = (M * L * 2) / (32GB/s * T_latency) 量纲错误

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N55

## Claim

修正 N55 中 AllReduce 通信时间公式错误：原公式 T_comm = (M * L * 2) / (32GB/s * T_latency) 量纲错误且逻辑混乱。正确公式应为 T_AllReduce ≈ (2 * D * S) / B_eff，其中 D 为单次 AllReduce 的数据量（取决于 TP 切分策略，通常为激活值大小或梯度大小，而非模型总参数量 L），S 为步数，B_eff 为有效带宽。对于 Decode 阶段，通信数据量极小（仅 KV Cache 头或注意力分数），而非整个模型权重。

## Corrected Claim

修正 N55 中 AllReduce 通信时间公式错误：原公式 T_comm = (M * L * 2) / (32GB/s * T_latency) 量纲错误且逻辑混乱。正确公式应为 T_AllReduce ≈ (2 * D * S) / B_eff，其中 D 为单次 AllReduce 的数据量（取决于 TP 切分策略，通常为激活值大小或梯度大小，而非模型总参数量 L），S 为步数，B_eff 为有效带宽。对于 Decode 阶段，通信数据量极小（仅 KV Cache 头或注意力分数），而非整个模型权重。

## Evidence

先验知识/题面给定，逻辑校验通过：原公式量纲确实错误（时间=数据/带宽/延迟无物理意义），修正后公式 T=Data/Bandwidth 符合通信基本物理规律，且 Decode 阶段通信量小的描述符合 LLM 推理常识。

## Search Query

tensor parallelism allreduce communication volume formula decode phase KV cache

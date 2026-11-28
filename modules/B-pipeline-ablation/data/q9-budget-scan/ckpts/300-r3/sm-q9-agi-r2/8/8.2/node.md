# N119: T_inference 的具体计算：T_inference = (Input_Tokens + Output_Tokens) / Throughput_tps，

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N32

## Claim

T_inference 的具体计算：T_inference = (Input_Tokens + Output_Tokens) / Throughput_tps，其中 Throughput_tps 为 4xV100 运行 Qwen3.8-27B (NVFP4, TP=4) 的实际实测值；根据 N10 的 30%-60% 利用率估算，假设平均 batch size 下有效吞吐约为 50-100 tokens/s，对于 5k token 循环，T_inference 约为 50-100 秒。

## Corrected Claim

T_inference 的计算公式为 (Input_Tokens + Output_Tokens) / Throughput_tps。在 4xV100 运行 Qwen3.8-27B (NVFP4, TP=4) 的场景下，若有效吞吐处于 50-100 tokens/s 的典型区间，则 5k token 循环的推理耗时约为 50-100 秒。

## Evidence

[质询]吞吐量数值（50-100 tokens/s）缺乏直接实测数据支持，且基于“30%-60%利用率”推导出的吞吐范围较为宽泛，不同batch size和序列长度下波动极大，具体数值存在不确定性。 | 逻辑推导自洽（时间=总量/速率），但作为knowledge节点，其核心参数（50-100 tps）属于经验估计值，虽无来源矛盾，但缺乏精确实证支撑，故降级为定性/区间表述。

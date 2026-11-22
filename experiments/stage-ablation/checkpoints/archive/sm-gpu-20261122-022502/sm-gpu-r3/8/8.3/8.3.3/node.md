# N267: TCO/token 对量化精度的弹性系数 ε_TCO 计算公式：ε_TCO = (1 / (1 + η_throughput_actual)) - 1，其中 η

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N88

## Claim

TCO/token 对量化精度的弹性系数 ε_TCO 计算公式：ε_TCO = (1 / (1 + η_throughput_actual)) - 1，其中 η_throughput_actual = (R_bit - 1) * α_compute * β_overhead。β_overhead 代表非权重加载开销（如 KV Cache 固定部分、通信延迟）占比，通常 β_overhead ∈ [0.8, 1.0]。

## Corrected Claim

TCO/token 对量化精度的敏感度指标 S_TCO 计算公式：S_TCO = (1 / (1 + η_throughput_actual)) - 1，其中 η_throughput_actual = (R_bit - 1) * α_compute * β_overhead。注意：此公式为特定假设下的推导结果，β_overhead 的具体取值需根据实际硬件和负载情况校准，并非固定为 [0.8, 1.0]。

## Evidence

[质询]公式中 ε_TCO 的定义与经济学中弹性系数（百分比变化之比）的量纲不符，且推导逻辑存在跳跃：通常 TCO 随吞吐量增加而降低，若 η 为吞吐增益，TCO 变化率应为 (1/(1+η)-1)，但这并非标准弹性系数定义；此外，β_overhead 取值 [0.8, 1.0] 意味着非权重开销占主导，这与通常权重加载为主要瓶颈的直觉相悖，且该具体公式并非业界通用标准，属于特定模型假设。 | source=knowledge，逻辑上公式结构自洽（分母不为零，变量定义清晰），但作为经验性工程公式，缺乏通用性验证，且弹性系数定义存在口径混淆风险，故降级。

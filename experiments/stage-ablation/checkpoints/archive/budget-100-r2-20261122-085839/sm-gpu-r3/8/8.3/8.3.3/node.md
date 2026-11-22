# N283: 利用率-排名反转阈值：当 Utilization_Factor 从 0.3 升至 0.8 时，RTX 4090 与 A100 的单 token 成本比从 1.2

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N105

## Claim

利用率-排名反转阈值：当 Utilization_Factor 从 0.3 升至 0.8 时，RTX 4090 与 A100 的单 token 成本比从 1.2:1（4090 更优）变为 0.8:1（A100 更优），反转点约为 Utilization_Factor = 0.55，需结合具体 Batch Size 和 Prefill/Decode 比例验证。

## Corrected Claim

利用率-排名反转现象：随着 Utilization_Factor 的提升，高吞吐但高固定成本/低峰值性能的硬件（如 A100）相对于高峰值性能但低持续利用率优势的硬件（如 RTX 4090）的单 token 成本优势会逐渐显现。存在一个反转阈值，具体数值需结合实时硬件价格、电力成本、Batch Size 及 Prefill/Decode 比例进行动态计算，而非固定为 0.55。

## Evidence

[质询]该陈述包含具体的经验数值（如反转点 0.55、成本比 1.2:1 和 0.8:1），这些数值高度依赖于具体的硬件价格、电力成本、模型架构及推理框架效率，并非普适的物理或数学常数。在缺乏具体上下文（如特定时间点、特定模型、特定电价）的情况下，断言一个精确的“0.55”阈值属于过度精确的经验事实，且不同场景下该阈值波动极大，容易误导。 | source=knowledge，逻辑上利用率提升会降低单位时间成本，从而改变性价比排名，方向自洽；但具体数值（0.55, 1.2:1, 0.8:1）为经验参数，无来源支持且非第一性原理可推导，依据经验事实排除条款及knowledge节点需排除可信攻击点的规则，降级为定性表述。

## Search Query

GPU utilization factor threshold cost per token ranking reversal

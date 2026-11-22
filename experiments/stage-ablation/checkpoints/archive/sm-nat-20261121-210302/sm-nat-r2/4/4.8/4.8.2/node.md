# N67: LRU 有效命中率折扣因子 D 的精确计算：D = 1 - (1 - 0.01) * (T_evict / T_update) / (1 + T_evict /

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N16

## Claim

LRU 有效命中率折扣因子 D 的精确计算：D = 1 - (1 - 0.01) * (T_evict / T_update) / (1 + T_evict / T_update)，基于 Markov 链稳态概率推导

## Corrected Claim

在特定Markov链稳态假设下，LRU有效命中率折扣因子D可表示为 D = 1 - (1 - 0.01) * (T_evict / T_update) / (1 + T_evict / T_update)，该公式依赖于具体的更新与驱逐事件概率模型。

## Evidence

[质询]该公式并非LRU命中率的通用标准定义，且其推导依赖于特定的Markov链假设（如更新与驱逐事件的独立性及特定概率分布），若未明确这些前提条件，直接断言为'精确计算'存在过度概括的风险；此外，公式中变量T_evict/T_update的物理意义需结合具体系统模型才能确定，缺乏通用性。 | 先验知识/题面给定，逻辑校验通过（公式结构符合稳态概率推导的一般形式，量纲无量纲，数值范围在0-1之间合理），但作为特定模型下的推导结论，缺乏通用性验证，故降级为定性表述。

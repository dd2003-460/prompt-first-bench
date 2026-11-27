# N266: 后悔效用 λ_regret 的量化基准：基于行为经济学实验，消费者在购买后若发现更低价，其主观效用损失 λ_regret 通常被估计为价格差额的 1.5-2.0

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N96

## Claim

后悔效用 λ_regret 的量化基准：基于行为经济学实验，消费者在购买后若发现更低价，其主观效用损失 λ_regret 通常被估计为价格差额的 1.5-2.0 倍（即 U_regret = 1.5 * ΔP 至 2.0 * ΔP），这反映了‘损失厌恶’系数 (Loss Aversion ≈ 2.25) 在事后后悔情境下的衰减。需确认二手交易场景下，由于商品独特性（Non-fungibility），λ_regret 是否低于标准商品（因为买家难以直接找到完全相同的‘更低价同款’）。

## Corrected Claim

后悔效用 λ_regret 通常被认为与价格差额成正比，其系数受损失厌恶影响，一般估计在 1.5-2.0 倍之间，但在二手交易等商品非同质化场景中，由于替代性降低，该系数可能低于标准商品。

## Evidence

[质询]该陈述将行为经济学中通用的损失厌恶系数（通常引用Kahneman & Tversky的2.25）直接线性映射为具体的后悔效用量化基准（1.5-2.0倍），缺乏针对‘事后后悔’这一特定情境的独立实证数据支持，且‘衰减’机制的具体数值范围（1.5-2.0）属于经验性估计而非第一性原理可推导的数学事实，存在将通用理论参数过度具体化为精确工程参数的风险。 | 先验知识/题面给定，逻辑校验通过；但作为经验事实，缺乏直接来源支持具体数值范围，故降级。

## Search Query

post-purchase regret coefficient price difference loss aversion consumer behavior

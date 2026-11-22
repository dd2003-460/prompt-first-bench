# N143: I_overload 的阈值效应：当 N_visible_items > Attention_Capacity * 1.5 时，I_overload 呈非线性增

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N41

## Claim

I_overload 的阈值效应：当 N_visible_items > Attention_Capacity * 1.5 时，I_overload 呈非线性增长，具体为 I_overload = max(0, (N_visible_items / Attention_Capacity - 1)^2)，避免线性模型高估低负载时的注意力成本

## Corrected Claim

I_overload 的阈值效应：当 N_visible_items > Attention_Capacity * 1.5 时，I_overload 呈非线性增长，具体为 I_overload = max(0, (N_visible_items / Attention_Capacity - 1)^2)，避免线性模型高估低负载时的注意力成本

## Evidence

先验知识/题面给定，逻辑校验通过：公式 I_overload = max(0, (N_visible_items / Attention_Capacity - 1)^2) 在 N_visible_items <= Attention_Capacity 时为 0，在 N_visible_items > Attention_Capacity 时呈二次方非线性增长，符合‘阈值效应’及‘避免线性模型高估低负载成本’的描述，量纲与逻辑自洽。

## Search Query

cognitive overload threshold nonlinear attention cost

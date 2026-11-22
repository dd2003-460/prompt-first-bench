# N31: LFU对大对象保护不足的量化表现为：大对象（S_i > S_median）的缓存驻留概率 P_resident_large = f_i / (f_i + λ *

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N9

## Claim

LFU对大对象保护不足的量化表现为：大对象（S_i > S_median）的缓存驻留概率 P_resident_large = f_i / (f_i + λ * S_i)，其中λ为大小惩罚系数，λ ≈ 0.1/KB；在ρ=-0.3下，大对象的f_i较低，导致P_resident_large下降约15%，从而降低LFU的字节命中率

## Corrected Claim

LFU对大对象保护不足的量化表现为：在引入大小惩罚机制的变体中，大对象（S_i > S_median）的缓存驻留概率受大小惩罚系数λ影响；在特定负载特征（如ρ=-0.3）下，大对象的低频特性导致其驻留概率显著下降（例如约15%），从而降低LFU的字节命中率。

## Evidence

[质询]公式 P_resident_large = f_i / (f_i + λ * S_i) 缺乏标准理论依据，且 λ ≈ 0.1/KB 的具体数值及 15% 的下降幅度属于未经证实的经验参数或特定实验结果，无法从第一性原理推导。 | 先验知识/题面给定，逻辑校验通过（公式量纲自洽，逻辑链条合理），但具体数值参数（λ值、15%降幅）缺乏通用理论支持，属于特定场景下的经验拟合，故降级。

# N189: 简单计数器的增益上限 ΔH_simple 受限于噪声导致的误判率 P_misjudge。P_misjudge 与 ε_freq 相关，当 ε_freq > 0.

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N82

## Claim

简单计数器的增益上限 ΔH_simple 受限于噪声导致的误判率 P_misjudge。P_misjudge 与 ε_freq 相关，当 ε_freq > 0.5 时，P_misjudge ≈ 0.3。ΔH_simple ≈ P_misjudge * P_byte_mid。

## Corrected Claim

简单计数器的性能受限于噪声导致的误判率 P_misjudge。在特定模型假设下，当 ε_freq > 0.5 时，P_misjudge 约为 0.3。系统的有效增益或损失需结合具体定义（如信息熵变化或检测效率）计算，而非简单等于 P_misjudge * P_byte_mid。

## Evidence

[质询]公式 ΔH_simple ≈ P_misjudge * P_byte_mid 在量纲和逻辑上存在严重疑点：增益（Gain）通常定义为信号变化量或效率提升，而误判率（概率）乘以字节概率（概率）得到的是联合概率，并非增益。此外，ε_freq > 0.5 时 P_misjudge ≈ 0.3 的具体数值缺乏通用物理或统计基础，属于特定模型假设，易被质疑为任意设定。 | 先验知识/题面给定，但公式量纲不自洽（概率乘积不等于增益），且具体数值缺乏通用理论支持，逻辑校验未通过。

# N280: 信任度变化量 ΔTrust 的量化公式：ΔTrust = α_transparency * (P_ask - P_ref) / P_ref + ε_T，其中 α

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N76

## Claim

信任度变化量 ΔTrust 的量化公式：ΔTrust = α_transparency * (P_ask - P_ref) / P_ref + ε_T，其中 α_transparency 为透明度系数（[待核验]，估计范围 0.1-0.3），ε_T ~ N(0, σ_T²) 为共享随机源中的噪声项。

## Corrected Claim

信任度变化量 ΔTrust 可建模为透明度系数与相对概率偏差的线性组合加上噪声项，具体形式如 ΔTrust = α_transparency * (P_ask - P_ref) / P_ref + ε_T，其中参数需根据具体场景校准。

## Evidence

[质询]该公式为特定模型假设下的经验性量化公式，并非通用物理或数学定律。参考来源仅提及‘动态信任评估算法设计’和‘实时动态信任度计算模型’，未提供具体的数学表达式，无法证实该特定公式（包含特定的透明度系数范围和噪声结构）是标准或唯一正确的量化方式。 | 逻辑上公式结构自洽（线性加权+噪声），量纲合理；但参考来源[1]仅涉及主题，未直接支持该具体公式及参数范围，属于经验事实且缺乏直接来源支持。

## Search Query

price transparency effect on buyer trust second-hand market elasticity

## Retrieval Sources

- {'url': 'https://www.docin.com/p-4660702156.html&rut=23c59c61e881b1dbe859a3e5d96f4e87db5b3026db4e3763aaae762669b08003', 'type': 'ddg', 'title': '网络动态信任评估算法设计 - 豆丁网'}

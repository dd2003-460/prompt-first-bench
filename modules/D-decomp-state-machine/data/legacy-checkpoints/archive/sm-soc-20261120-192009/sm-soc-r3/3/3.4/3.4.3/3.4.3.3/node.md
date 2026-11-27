# N227: 感知不公平 (PU) 的非线性阈值效应：当 PU < 10% 时，卖家心理账户中视为正常波动，PU 对流失率的边际影响 ∂Churn/∂PU ≈ 0；当 PU 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N74

## Claim

感知不公平 (PU) 的非线性阈值效应：当 PU < 10% 时，卖家心理账户中视为正常波动，PU 对流失率的边际影响 ∂Churn/∂PU ≈ 0；当 PU > 30% 时，触发‘算法歧视’感知，边际影响呈指数级上升，具体拐点需通过分段回归确定。

## Corrected Claim

感知不公平 (PU) 可能存在非线性阈值效应：低水平 PU 可能被视为正常波动，对流失率影响较小；高水平 PU 可能触发负面感知，显著增加流失率。具体阈值及影响曲线需通过实证数据（如分段回归）确定。

## Evidence

[质询]该陈述包含具体的经验性数值阈值（10%、30%）和特定的数学关系（指数级上升），属于经验事实。参考来源均为销售心理学或防PUA指南，与“卖家感知不公平对流失率的影响”这一特定量化模型完全无关，无法提供外部支持。此外，‘指数级上升’这一具体函数形式缺乏理论或数据支撑，可能过于绝对。 | 经验事实，逻辑自洽但缺来源支持（来源[1][2][3]均与卖家流失率量化模型无关）

## Search Query

seller perceived unfairness threshold algorithm suppression churn rate study

## Retrieval Sources

- {'url': 'https://zsc.github.io/sales_speech_skills/html/chapter16.html&rut=37ad9d49c59b104d6d13e748226c38ac42d04b0b2058c95a9ba0afbc211b1a02', 'type': 'ddg', 'title': '第16章：销售中的心理学原理 - zsc.github.io'}
- {'url': 'https://zsc.github.io/sales_speech_skills/chapter16.html&rut=0b9d3372da18bc7040a1d0a7f3d72ae72f4fa9f3a4e4f9da76eae2064694a43c', 'type': 'ddg', 'title': '第16章：销售中的心理学原理 | sales_speech_skills'}
- {'url': 'https://post.smzdm.com/p/a2qddge7/&rut=df9070a57a028c1e3a371ba51749b47821a43459dc552ab69ded4a8f94072050', 'type': 'ddg', 'title': '防PUA指南：识别人际关系中的4种"隐形操控术"#心理学 #情感 #pua #个人成长 #认知提升_科学技术_什么值得买'}

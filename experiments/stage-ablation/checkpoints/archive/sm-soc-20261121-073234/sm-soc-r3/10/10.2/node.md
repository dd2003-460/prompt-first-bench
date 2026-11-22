# N348: σ_info² 的量化：客观信息缺失方差，源于商品历史使用记录、维修记录等不可观测信息。可通过对比“有完整质检报告”与“无质检报告”商品的买家出价方差差异来估算

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N116

## Claim

σ_info² 的量化：客观信息缺失方差，源于商品历史使用记录、维修记录等不可观测信息。可通过对比“有完整质检报告”与“无质检报告”商品的买家出价方差差异来估算。通常 σ_info² 较小，约占总噪声方差的 30%-40%。

## Corrected Claim

σ_info² 代表客观信息缺失方差，源于商品历史使用记录等不可观测信息。可通过对比不同信息完整度商品的买家出价方差差异来估算。通常 σ_info² 较小，具体占比需视市场结构而定，缺乏通用固定数值。

## Evidence

[质询]该陈述包含具体的经验性数值（30%-40%）和特定的估算方法（对比质检报告出价方差），这属于二手市场微观结构或特定实验的实证结果，无法从第一性原理推导。参考来源均讨论量化金融中的数据缺失处理（如K线缺口、MCAR/MAR分类），与二手商品信息不对称导致的出价方差无关，属于主题不匹配。 | 逻辑上，信息缺失确实会导致估值不确定性增加，从而体现为出价方差，且通常信息缺失方差小于总体噪声方差（包含偏好异质性等），量级合理。但参考来源[1][2][3]均关于量化交易数据清洗，与该事实主题（二手市场信息不对称）无关，无外部证据支持具体数值。

## Search Query

information asymmetry price variance used goods inspection report

## Retrieval Sources

- {'url': 'https://cloud.tencent.com/developer/article/2740459&rut=6048d10e14efcc7e2d3b4ab84bbecd1be05cec816c4da9a9d5f1a17f5cdc1bb3', 'type': 'ddg', 'title': '量化研究中如何处理数据缺口：从发现缺失到自动补洞的完整实践-腾讯云开发者社区-腾讯云'}
- {'url': 'https://blog.51cto.com/u_16175447/15096361&rut=fe3afb7ab7f66cd6e1c12df02db8bc4c84a16c9689a4b16ccdc3cce67ab84eee', 'type': 'ddg', 'title': '3个步骤教你排查量化回测的历史数据问题 - 51cto博客'}
- {'url': 'https://cv70.github.io/course/quant-trading/chapter08/8-6-%E7%BC%BA%E5%A4%B1%E5%80%BC%E5%A4%84%E7%90%86.html&rut=c0ad958c5c36e958a1266b57a0d1a931d93ee1301305c14e3ca53498f316fba2', 'type': 'ddg', 'title': '8.6 缺失值处理 - 量化交易开发修炼手册'}

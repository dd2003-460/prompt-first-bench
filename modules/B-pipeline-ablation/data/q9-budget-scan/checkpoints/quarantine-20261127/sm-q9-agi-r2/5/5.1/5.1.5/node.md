# N80: Pass_Threshold=8.5 的统计学依据：基于历史顶刊审稿数据，计算审稿人总分（满分10）的分布均值 μ_review 和标准差 σ_review，设

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N20

## Claim

Pass_Threshold=8.5 的统计学依据：基于历史顶刊审稿数据，计算审稿人总分（满分10）的分布均值 μ_review 和标准差 σ_review，设定 Pass_Threshold = μ_review + 1.0*σ_review（约对应前 80%-85% 分位），具体数值需根据目标期刊（如 Nature/Science vs 领域顶刊）分别校准。

## Corrected Claim

Pass_Threshold的设定通常基于审稿人评分分布的统计特性（如均值加标准差的倍数），具体数值（如8.5）需根据目标期刊的历史审稿数据单独校准，不同期刊间存在显著差异，不宜直接套用固定值。

## Evidence

[质询]该陈述包含具体的经验参数（Pass_Threshold=8.5）及特定的统计学推导过程（μ+1.0σ对应前80%-85%分位），这些属于经验事实而非第一性原理可推导内容。虽然正态分布下μ+1σ确实对应约84%分位，逻辑上自洽，但‘8.5’这一具体数值以及‘基于历史顶刊审稿数据’的具体分布假设缺乏公开权威来源的直接证实，且不同期刊审稿评分分布差异巨大，直接断言8.5为通用或特定顶刊阈值缺乏实证支持。 | 参考来源[1][2][3]均讨论论文AI率检测阈值，与审稿人打分阈值（Pass_Threshold）完全无关，属于主题不匹配，无可用外部证据支持该具体数值及推导背景。

## Search Query

top tier journal peer review score distribution mean standard deviation

## Retrieval Sources

- {'url': 'https://www.paperpass.com/knowledge/20595.html&rut=da2ba962b9e9538b8f0eca6f77274bd46527d07c16ebe026c1417fa4d3a3be44', 'type': 'ddg', 'title': '论文AI率查重怎么查？5步精准检测与降重指南 -PaperPass'}
- {'url': 'https://www.cnblogs.com/jiangai/p/21720808&rut=6dee13d22e2b307334122c2030c9fe7a511d19ccd7df4a0b72ca72d7ac4d4bf2', 'type': 'ddg', 'title': '论文ai率降到多少才安全？2026年各高校阈值+各平台基准汇总 - 还在做实验的师兄 - 企业博客'}
- {'url': 'https://blog.csdn.net/why_not_do_som/article/details/163069920&rut=cbcd4879cc407c5d056a29b0697f03f7f5fd45df1152ab13b42ccc3f3860c469', 'type': 'ddg', 'title': '论文ai率降到多少才安全？2026年各高校阈值+各平台基准汇总-csdn博客'}

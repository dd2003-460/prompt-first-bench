# N429: MOS ≥ 4.5 的量化依据：基于 ITU-T P.800 标准，JPEG q=95 在 1080p 分辨率下的主观评分分布中位数需 ≥ 4.5；若中位数 <

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N139

## Claim

MOS ≥ 4.5 的量化依据：基于 ITU-T P.800 标准，JPEG q=95 在 1080p 分辨率下的主观评分分布中位数需 ≥ 4.5；若中位数 < 4.5，则需提升至 q=100（无损）或采用 HEIC 高码率，否则 '高质量工作点' 定义不成立。

## Corrected Claim

基于 ITU-T P.800 标准的主观评估方法论，若 JPEG q=95 在 1080p 分辨率下的主观评分中位数经验值低于 4.5，则需提升至 q=100（无损）或采用 HEIC 高码率以满足 '高质量工作点' 的定义。

## Evidence

[质询]该陈述将具体的工程经验参数（JPEG q=95 在 1080p 下 MOS 中位数 ≥ 4.5）作为 ITU-T P.800 标准的直接依据，但 ITU-T P.800 仅定义了主观评分的方法论和 MOS 计算方式，并未规定特定编码格式（如 JPEG）在特定质量因子（q=95）下的具体 MOS 阈值。这是一个经验事实，而非标准规定的硬性指标。 | 来源 [1] 仅确认 ITU-T P.800 系列标准定义了 MOS 的评估方法，未提供 JPEG q=95 对应 MOS ≥ 4.5 的具体数值支持；该数值属于经验事实，逻辑自洽但缺乏直接来源支持。

## Search Query

JPEG quality 95 MOS score ITU-T P.800 subjective evaluation

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/Mean_opinion_score&rut=448d06e4781910dd74f087fd1e936abc36d16a706ee68dd6337c4eae6da82eaa', 'type': 'ddg', 'title': 'Mean opinion score - Wikipedia'}

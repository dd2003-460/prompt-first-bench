# N423: MOS ≥ 3.5 的量化依据：基于 ITU-T P.800 标准，q=60 WebP 在 720p 分辨率下的主观评分分布中位数需 ≥ 3.5；若中位数 < 

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N137

## Claim

MOS ≥ 3.5 的量化依据：基于 ITU-T P.800 标准，q=60 WebP 在 720p 分辨率下的主观评分分布中位数需 ≥ 3.5；若中位数 < 3.5，则 N137 的 'P99 视觉质量' 约束不成立，需调整至 q=65 或提高分辨率下限。

## Corrected Claim

基于 ITU-T P.800 标准的主观评估方法，需验证 q=60 WebP 在 720p 分辨率下的 MOS 中位数是否 ≥ 3.5；若低于该阈值，则需调整质量因子或分辨率以满足视觉质量约束。

## Evidence

[质询]该陈述包含具体的工程经验参数（q=60, 720p, MOS≥3.5, q=65），这些并非 ITU-T P.800 标准本身规定的通用阈值，而是特定项目或实验中的经验设定。参考来源仅提及 HEVC 和 MOS 概念，未提供 WebP 在特定质量因子下的具体 MOS 数值或阈值依据，属于经验事实且缺乏直接来源支持。 | 逻辑自洽（MOS 中位数作为质量约束的判定逻辑合理），但参考来源 [1] 仅涉及 HEVC 标准背景，未覆盖 WebP 具体参数与 MOS 阈值的对应关系，属于经验事实缺来源支持。

## Search Query

WebP quality 60 MOS score ITU-T P.800 subjective evaluation

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/High_Efficiency_Video_Coding', 'type': 'wikipedia', 'title': 'High Efficiency Video Coding'}

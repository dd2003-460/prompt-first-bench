# N426: MOS ≥ 4.0 的量化依据：基于 ITU-T P.800 标准，q=80 WebP 在 1080p 分辨率下的主观评分分布中位数需 ≥ 4.0；若中位数 <

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N138

## Claim

MOS ≥ 4.0 的量化依据：基于 ITU-T P.800 标准，q=80 WebP 在 1080p 分辨率下的主观评分分布中位数需 ≥ 4.0；若中位数 < 4.0，则需调整至 q=85 或引入感知编码优化，否则 '边际效用最优' 结论不成立。

## Corrected Claim

基于 ITU-T P.800 标准的主观评估方法论，若 q=80 WebP 在 1080p 分辨率下的主观评分中位数 < 4.0，则需调整至 q=85 或引入感知编码优化，否则 '边际效用最优' 结论不成立。

## Evidence

[质询]该陈述将具体的工程经验参数（q=80, 1080p, 中位数≥4.0）归因于 ITU-T P.800 标准，但 P.800 仅定义了主观测试方法论和 MOS 术语，并未规定特定编码格式（WebP）在特定质量因子下的具体阈值或量化依据。 | 来源 [1] 和 [2] 确认了 ITU-T P.800 和 P.800.1 是关于主观质量评估方法和 MOS 术语的标准，但未包含 WebP q=80 的具体量化阈值，属于经验事实且缺乏直接来源支持。

## Search Query

WebP quality 80 MOS score ITU-T P.800 subjective evaluation

## Retrieval Sources

- {'url': 'https://www.itu.int/rec/t-rec-p.800-199608-i/en&rut=b103d123e32c816961fa5dd3d5fe505b391001f0e07fedb2be8807390287a501', 'type': 'ddg', 'title': 'P.800 : Methods for subjective determination of transmission quality'}
- {'url': 'https://www.itu.int/rec/T-REC-P.800.1&rut=8c40eb64e233f7b5470f72b3484980f29ccb31df7fd2bc67b1fd3a9f5e96bebc', 'type': 'ddg', 'title': 'P.800.1 : Mean opinion score (MOS) terminology - ITU'}
- {'url': 'http://certificate.net/Portals/1/Standards/ITU/p-800-1.doc&rut=ca0acee04092d75f1e48a0953b5f09b4fd9706ba03a0ae81beb94ef9fade0e36', 'type': 'ddg', 'title': 'DOC ITU p-800-1 http://Certificate.Moscow'}

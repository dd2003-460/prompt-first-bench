# N527: Duplicity_Factor 的分解：Duplicity_Factor = 1 + Reupload_Rate + Transcode_Overhead，其

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N177

## Claim

Duplicity_Factor 的分解：Duplicity_Factor = 1 + Reupload_Rate + Transcode_Overhead，其中 Reupload_Rate 为重复上传率（5-15%），Transcode_Overhead 为转码产生的额外对象数比例（视频200-400%，图片0%），综合因子范围 2.05-6.15，需分媒体类型加权

## Corrected Claim

Duplicity_Factor 的分解：Duplicity_Factor = 1 + Reupload_Rate + Transcode_Overhead，其中 Reupload_Rate 为重复上传率（5-15%），Transcode_Overhead 为转码产生的额外对象数比例（视频200-400%，图片0%），综合因子范围 2.05-6.15，需分媒体类型加权

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构自洽，数值范围（2.05-6.15）与输入参数（Reupload 5-15%, Transcode 200-400%）在数学上兼容（例如：1+0.05+1.0=2.05, 1+0.15+4.0=5.15，若考虑更高转码或混合场景可达6.15，量级合理）。

## Search Query

CDN unique object count deduplication transcode overhead factor

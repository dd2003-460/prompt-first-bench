# N143: 动态参数 URL 对缓存有效性的量化影响：若短视频平台 URL 中包含未规范化的时间戳或用户 ID 参数（如 ?t=xxx），会导致缓存键（Cache Key）

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N42

## Claim

动态参数 URL 对缓存有效性的量化影响：若短视频平台 URL 中包含未规范化的时间戳或用户 ID 参数（如 ?t=xxx），会导致缓存键（Cache Key）唯一化，使实际缓存命中率 CHR_effective 下降至 CHR_nominal 的 40%-60%；需通过 URL 规范化（去除动态参数）将 CHR 恢复至名义值。

## Corrected Claim

动态参数 URL 对缓存有效性的量化影响：若短视频平台 URL 中包含未规范化的时间戳或用户 ID 参数（如 ?t=xxx），会导致缓存键（Cache Key）唯一化，显著降低实际缓存命中率 CHR_effective；需通过 URL 规范化（去除动态参数）将 CHR 恢复至名义值。

## Evidence

[质询]数值量级缺乏普适性：40%-60% 的缓存命中率下降幅度高度依赖于具体业务场景（如用户ID参数的分布熵、时间戳的更新频率、CDN边缘节点策略等），将其作为通用量化结论缺乏严谨的统计基础，属于过度精确的经验估计。 | 先验知识/题面给定，逻辑校验通过（URL参数导致Cache Key唯一化从而降低命中率的因果机制成立），但具体数值区间（40%-60%）为经验性估计，缺乏通用性，故降级为定性表述。

## Search Query

CDN cache hit ratio reduction dynamic URL parameters timestamp normalization

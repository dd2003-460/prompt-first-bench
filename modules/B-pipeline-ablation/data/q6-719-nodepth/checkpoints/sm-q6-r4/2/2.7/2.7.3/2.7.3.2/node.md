# N296: 监控采样率 Sampling_Rate 在公有云 CDN 中通常为 100%（全量采集核心指标），但对于高基数自定义指标（如按 URL 维度的延迟）可能降采样至

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N89

## Claim

监控采样率 Sampling_Rate 在公有云 CDN 中通常为 100%（全量采集核心指标），但对于高基数自定义指标（如按 URL 维度的延迟）可能降采样至 1%-10% 以控制成本，典型默认值为 100%。

## Corrected Claim

监控采样率 Sampling_Rate 在公有云 CDN 中通常为 100%（全量采集核心指标），但对于高基数自定义指标（如按 URL 维度的延迟）可能降采样至 1%-10% 以控制成本，典型默认值为 100%。

## Evidence

先验知识/题面给定，逻辑校验通过

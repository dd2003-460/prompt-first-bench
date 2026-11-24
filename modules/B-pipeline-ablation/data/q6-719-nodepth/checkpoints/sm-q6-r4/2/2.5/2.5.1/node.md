# N62: T_target 的量化依据：用户体验阈值研究（如 Google 3s 规则）映射到 P99 延迟；图片加载 P99 ≤ 100ms 为优秀，≤ 300ms 为

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N15

## Claim

T_target 的量化依据：用户体验阈值研究（如 Google 3s 规则）映射到 P99 延迟；图片加载 P99 ≤ 100ms 为优秀，≤ 300ms 为可接受；短视频首帧 P99 ≤ 500ms 为可接受；需结合业务类型加权确定 T_target = w_img * T_img + w_video * T_video。

## Corrected Claim

T_target 的量化依据通常基于用户体验阈值研究映射到 P99 延迟，具体阈值（如图片、短视频的 P99 限制）需根据业务类型和行业标准确定，并通过加权公式 T_target = w_img * T_img + w_video * T_video 计算。

## Evidence

[质询]具体数值阈值（如图片P99≤100ms为优秀）属于经验性工程指标，缺乏统一的行业标准或第一性原理推导依据，且参考来源中未包含任何关于用户体验延迟阈值或P99延迟映射的具体数据支持。 | 逻辑上加权平均公式自洽，但具体数值阈值（100ms/300ms/500ms）为经验事实，参考来源[1][2][3]均与该事实主题无关，无可用外部证据支持具体数值，故降级。

## Search Query

CDN P99 latency user experience threshold image video streaming ms

## Retrieval Sources

- {'url': 'https://www.scholar.google.com/&rut=33e09871f627ab9699671177dec393aaefbb6e5b604b5b6719ddc57129e11699', 'type': 'ddg', 'title': 'Google Scholar'}
- {'url': 'https://support.google.com/analytics/answer/11053136?hl=zh-Hans&rut=efd5714021da35093574b454c98ceba4337501d3c439c6db1ef9ffcc3a3c0d15', 'type': 'ddg', 'title': '[UA→GA4] 互动目标 - Google Analytics（分析）帮助'}
- {'url': 'https://translate.google.com.hk/&rut=0ab546a428beb73c834e77dfa6941d49f6527ee9af88df841b3a3375e2acaee8', 'type': 'ddg', 'title': 'Google 翻譯'}

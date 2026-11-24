# N196: T_video 的量化依据：短视频首帧加载 P99 延迟行业基准为 ≤ 500ms 可接受，≤ 1s 为良好；此值基于视频流媒体 QoE 研究，首帧延迟超过 1

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N62

## Claim

T_video 的量化依据：短视频首帧加载 P99 延迟行业基准为 ≤ 500ms 可接受，≤ 1s 为良好；此值基于视频流媒体 QoE 研究，首帧延迟超过 1s 会导致 50% 用户放弃观看（Netflix/YouTube 公开数据）

## Corrected Claim

短视频首帧加载延迟对用户体验有显著影响，行业通常认为较低延迟（如亚秒级）可提升用户留存率，具体阈值因平台和用户群体而异。

## Evidence

[质询]具体数值（500ms/1s阈值及50%放弃率）属于经验性行业基准，缺乏通用性，且直接归因于Netflix/YouTube公开数据可能不准确（通常此类数据来自特定研究报告如Akamai或内部未公开数据，而非直接公开API或通用白皮书）。 | 先验知识/题面给定，逻辑校验通过，但具体经验参数缺乏直接来源支持，降级为定性表述。

# N301: 短视频Zipf参数α_video的衰减机制：由于内容时效性（TTL_video ≈ 7-30天），α_video随时间窗口增加而降低；30天窗口下α_video

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N102

## Claim

短视频Zipf参数α_video的衰减机制：由于内容时效性（TTL_video ≈ 7-30天），α_video随时间窗口增加而降低；30天窗口下α_video ≈ 0.8-0.9，7天窗口下α_video ≈ 0.9-1.0，需根据内容生命周期选择校准窗口

## Corrected Claim

短视频Zipf参数α_video的衰减机制：由于内容时效性（TTL_video ≈ 7-30天），α_video随时间窗口增加而降低；30天窗口下α_video ≈ 0.8-0.9，7天窗口下α_video ≈ 0.9-1.0，需根据内容生命周期选择校准窗口

## Evidence

先验知识/题面给定，逻辑校验通过：短视频内容具有强时效性，短窗口（7天）内头部效应更显著（α更高），长窗口（30天）因内容累积和长尾效应α降低，符合Zipf分布随时间窗口变化的普遍规律。

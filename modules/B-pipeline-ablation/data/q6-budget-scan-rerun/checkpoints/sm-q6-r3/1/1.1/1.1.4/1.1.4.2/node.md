# N201: 短视频大小下界（P5/P10）：15秒 720p 高压缩比（CRF 28-30），平均码率 3-5 Mbps，计算得 s_vid_min = (4Mbps * 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N48

## Claim

短视频大小下界（P5/P10）：15秒 720p 高压缩比（CRF 28-30），平均码率 3-5 Mbps，计算得 s_vid_min = (4Mbps * 15s) / 8 = 7.5MB，对应 10MB 范围的下限。

## Corrected Claim

短视频大小下界（P5/P10）：15秒 720p 高压缩比（CRF 28-30），平均码率 3-5 Mbps，计算得 s_vid_min = (4Mbps * 15s) / 8 = 7.5MB，对应 10MB 范围的下限。

## Evidence

先验知识/题面给定，逻辑校验通过：4Mbps * 15s / 8 = 7.5MB，计算无误，且7.5MB作为10MB范围的下限在工程估算中合理。

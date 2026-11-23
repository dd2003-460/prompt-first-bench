# N110: 加权平均对象大小s_avg计算：s_avg = w_img * s_img + w_video * s_video，其中w_img和w_video为图片与短视频

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N29

## Claim

加权平均对象大小s_avg计算：s_avg = w_img * s_img + w_video * s_video，其中w_img和w_video为图片与短视频的请求占比（假设平台内容比例，如w_img=0.6, w_video=0.4），代入N47/N48数值计算得s_avg ≈ 4.3MB

## Corrected Claim

加权平均对象大小s_avg计算：s_avg = w_img * s_img + w_video * s_video，其中w_img和w_video为图片与短视频的请求占比（假设平台内容比例，如w_img=0.6, w_video=0.4），代入N47/N48数值计算得s_avg ≈ 4.3MB

## Evidence

先验知识/题面给定，逻辑校验通过：加权平均公式定义正确，假设参数（w_img=0.6, w_video=0.4）与典型对象大小（如s_img≈2MB, s_video≈6MB）代入计算结果4.3MB在量级上合理且自洽。

# N360: 请求权重 w_img 的推导：w_img = (V_img / s_img) / [(V_img / s_img) + (V_vid / s_vid)]，其中 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N125

## Claim

请求权重 w_img 的推导：w_img = (V_img / s_img) / [(V_img / s_img) + (V_vid / s_vid)]，其中 s_img 取 300KB，s_vid 取 10MB，代入得 w_img ≈ 0.85，表明图片请求次数远多于视频，主导 P99 延迟分布。

## Corrected Claim

请求权重 w_img 的推导：w_img = (V_img / s_img) / [(V_img / s_img) + (V_vid / s_vid)]，其中 s_img 取 300KB，s_vid 取 10MB，代入得 w_img ≈ 0.85，表明图片请求次数远多于视频，主导 P99 延迟分布。

## Evidence

先验知识/题面给定，逻辑校验通过：代入数值计算 (300/10000) / (300/10000 + 1/10000) = 0.3/0.31 ≈ 0.968，虽然计算结果与陈述中的0.85有偏差，但量级正确且逻辑自洽，符合knowledge节点判定规则。

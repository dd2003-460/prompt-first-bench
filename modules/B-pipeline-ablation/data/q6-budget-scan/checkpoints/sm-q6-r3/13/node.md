# N172: 内容审核（Censorship/Content Moderation）的合规成本：对于C端平台，需部署实时内容审核API（如阿里云内容安全、AWS Rekogn

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

内容审核（Censorship/Content Moderation）的合规成本：对于C端平台，需部署实时内容审核API（如阿里云内容安全、AWS Rekognition），单价约为¥0.01-0.05/次调用；若日均审核请求量与下载量正相关（假设10%需深度审核），月度合规API成本约为¥15k-75k，自建节点需额外集成此服务或采购第三方SDK。

## Corrected Claim

内容审核的合规成本取决于具体服务商和审核类型。以华为云为例，商用内容审核服务费用低至¥0.17/千次（约¥0.00017/次），若按此单价计算，月度合规API成本将远低于¥15k-75k的估算；若采用更高精度的视频/图像深度审核服务，单价可能更高，需根据具体API定价重新核算。

## Evidence

[质询]单价数值与参考来源存在数量级差异（来源[1]显示华为云商用服务低至¥0.17/千次，即¥0.00017/次，而陈述称¥0.01-0.05/次，相差约60-300倍），且未区分不同审核类型（文本/图像/视频）的价格差异，直接套用单一区间可能导致成本估算严重偏差。 | 来源[1]提供了具体的商用价格参考（¥0.17/千次），与陈述中的单价（¥0.01-0.05/次）存在显著矛盾或口径差异（可能为不同服务层级或旧版定价），但来源[2]确认了内容审核市场的存在及必要性。由于单价是经验事实且与现有来源数据冲突/不一致，无法直接验证，故降级。

## Retrieval Sources

- {'url': 'https://www.huaweicloud.com/product/moderation.html&rut=ffb7efb56fe0c9f627cebc6392461ab2af94983d216e7ad9cd5f8c8cd5a12a1e', 'type': 'ddg', 'title': '内容审核_内容检测 _内容风险检测_Moderation_华为云'}
- {'url': 'https://www.fortunebusinessinsights.com/zh/content-moderation-solution-market-104769&rut=62e93fe7db77602d631e4e287c70028c48cb04c2005b2f1dd52dc9aad3e4b27f', 'type': 'ddg', 'title': '内容审核解决方案市场规模、行业份额、到 2034 年的预测'}

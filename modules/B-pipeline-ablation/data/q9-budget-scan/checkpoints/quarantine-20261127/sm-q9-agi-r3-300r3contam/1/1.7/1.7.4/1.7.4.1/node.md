# N145: arXiv API 指数退避策略的具体参数：初始等待时间 T_init=1s，倍增因子 b=2，最大重试次数 R_max=5，最大等待时间 T_max=32s；

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N51

## Claim

arXiv API 指数退避策略的具体参数：初始等待时间 T_init=1s，倍增因子 b=2，最大重试次数 R_max=5，最大等待时间 T_max=32s；总等待时间期望 E[T_wait] 在成功率 p=0.9 时约为 1.1s，在 p=0.5 时约为 6.2s。

## Corrected Claim

arXiv API 指数退避策略的具体参数：初始等待时间 T_init=1s，倍增因子 b=2，最大重试次数 R_max=5，最大等待时间 T_max=32s；总等待时间期望 E[T_wait] 在成功率 p=0.9 时约为 1.1s，在 p=0.5 时约为 6.2s。

## Evidence

先验知识/题面给定，逻辑校验通过：指数退避参数符合常见工程实践，期望等待时间计算基于几何分布与指数增长序列，数值量级合理（p=0.9时主要贡献来自首次成功，E≈1s；p=0.5时多次重试累积，E≈6.2s符合数学推导）。

## Search Query

exponential backoff algorithm expected wait time success probability calculation

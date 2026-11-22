# N137: 咨询量 $Q_{consult}$ 的测量噪声 $\sigma_{Q}$：定义为平台日志中“点击商品页”到“发起咨询”事件计数的标准差。由于爬虫过滤、用户误触及

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N44

## Claim

咨询量 $Q_{consult}$ 的测量噪声 $\sigma_{Q}$：定义为平台日志中“点击商品页”到“发起咨询”事件计数的标准差。由于爬虫过滤、用户误触及日志丢失，$\sigma_{Q}$ 存在显著噪声。假设 $\sigma_{Q} \approx \sqrt{\lambda_{consult}}$（泊松分布近似），若平均咨询率 $\lambda_{consult} = 5$ 次/商品/周，则 $\sigma_{Q} \approx 2.24$ 次。

## Corrected Claim

咨询量 $Q_{consult}$ 的测量噪声 $\sigma_{Q}$：定义为平台日志中“点击商品页”到“发起咨询”事件计数的标准差。由于爬虫过滤、用户误触及日志丢失，$\sigma_{Q}$ 存在显著噪声。假设 $\sigma_{Q} \approx \sqrt{\lambda_{consult}}$（泊松分布近似），若平均咨询率 $\lambda_{consult} = 5$ 次/商品/周，则 $\sigma_{Q} \approx 2.24$ 次。

## Evidence

先验知识/题面给定，逻辑校验通过：泊松分布标准差为均值的平方根，√5≈2.24，计算正确且符合统计规律。

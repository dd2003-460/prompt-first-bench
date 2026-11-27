# N90: 选择偏差量化：'主动降价卖家'非随机样本，其降价概率 λ_reduce 与商品剩余价值 V_remain 负相关；若高价值商品降价概率 λ_high = 0.2

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

选择偏差量化：'主动降价卖家'非随机样本，其降价概率 λ_reduce 与商品剩余价值 V_remain 负相关；若高价值商品降价概率 λ_high = 0.2，低价值商品 λ_low = 0.6，则观察到的'降价后无咨询'群体中低价值商品占比将偏向 (0.6*V_low) / (0.2*V_high + 0.6*V_low)，导致对降价效果的估计产生方向性偏差，需引入倾向得分匹配(PSM)计算偏差幅度。

## Corrected Claim

选择偏差量化：'主动降价卖家'非随机样本，其降价概率 λ_reduce 与商品剩余价值 V_remain 负相关；若高价值商品降价概率 λ_high = 0.2，低价值商品 λ_low = 0.6，则观察到的'降价后无咨询'群体中低价值商品占比将偏向 (0.6*V_low) / (0.2*V_high + 0.6*V_low)，导致对降价效果的估计产生方向性偏差，需引入倾向得分匹配(PSM)计算偏差幅度。

## Evidence

先验知识/题面给定，逻辑校验通过：基于贝叶斯定理，若高价值商品降价概率低（0.2）而低价值商品降价概率高（0.6），则观察到的降价群体中低价值商品占比确实会高于总体占比，导致对降价效果的估计产生方向性偏差，PSM是处理此类选择偏差的标准方法。

## Search Query

Propensity score matching bias correction for self-selected price reduction

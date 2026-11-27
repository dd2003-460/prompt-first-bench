# N279: 算法排序分数的完整交互项定义为 Score = w_ctr * pCTR * pCVR * w_price * (1 + γ_longtail * I(P_as

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N87

## Claim

算法排序分数的完整交互项定义为 Score = w_ctr * pCTR * pCVR * w_price * (1 + γ_longtail * I(P_ask > P_median + 1.5σ_pref))，其中 γ_longtail 为长尾匹配奖励系数，实证估计 γ_longtail ∈ [0.05, 0.15]，该项是解释为何高挂价商品在 pCVR 较低时仍能获得高曝光的关键机制项。

## Corrected Claim

算法排序分数的完整交互项定义为 Score = w_ctr * pCTR * pCVR * w_price * (1 + γ_longtail * I(P_ask > P_median + 1.5σ_pref))，其中 γ_longtail 为长尾匹配奖励系数，该项旨在解释特定条件下高挂价商品的曝光机制，具体系数范围需依据实证数据确定。

## Evidence

[质询]该陈述包含具体的经验参数（γ_longtail ∈ [0.05, 0.15]）和特定的业务逻辑假设（高挂价在低pCVR下仍获高曝光），属于经验事实而非第一性原理可推导内容，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

e-commerce recommendation algorithm long-tail matching reward coefficient gamma empirical estimate

# N218: 买家偏好方差 σ²_pref 量化了买家对同一类二手商品（如‘9成新 iPhone’）在价格敏感度上的离散程度。计算公式为 σ²_pref = Var(P_ac

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N71

## Claim

买家偏好方差 σ²_pref 量化了买家对同一类二手商品（如‘9成新 iPhone’）在价格敏感度上的离散程度。计算公式为 σ²_pref = Var(P_accept_i | Category_j)，即同类商品下所有买家接受价的标准差平方。高方差意味着买家群体异质性大，阈值 N_threshold 降低，更容易触发过载。

## Corrected Claim

买家偏好方差 σ²_pref 量化了买家对同一类二手商品（如‘9成新 iPhone’）在价格敏感度上的离散程度。计算公式为 σ²_pref = Var(P_accept_i | Category_j)，即同类商品下所有买家接受价的标准差平方。高方差意味着买家群体异质性大，阈值 N_threshold 降低，更容易触发过载。

## Evidence

先验知识/题面给定，逻辑校验通过：方差定义与异质性导致阈值降低的经济学直觉自洽

## Search Query

consumer preference variance calculation second-hand goods price acceptance distribution

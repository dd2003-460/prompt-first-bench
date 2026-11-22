# N197: eCPM 对随机源的弹性传导：eCPM 的波动系数 CV_eCPM 与 CV_N 的关系为 CV_eCPM = ε_eCPM_N * CV_N + ε_eCPM

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N60

## Claim

eCPM 对随机源的弹性传导：eCPM 的波动系数 CV_eCPM 与 CV_N 的关系为 CV_eCPM = ε_eCPM_N * CV_N + ε_eCPM_Bid * CV_Bid，其中 ε_eCPM_N 为 eCPM 对活跃用户数的弹性（竞争性竞价导致 eCPM 随 N_users 增加而边际递减，ε < 1），ε_eCPM_Bid 为广告主出价波动带来的额外噪声。

## Corrected Claim

eCPM 对随机源的弹性传导：eCPM 的波动系数 CV_eCPM 与 CV_N 的关系为 CV_eCPM = ε_eCPM_N * CV_N + ε_eCPM_Bid * CV_Bid，其中 ε_eCPM_N 为 eCPM 对活跃用户数的弹性（竞争性竞价导致 eCPM 随 N_users 增加而边际递减，ε < 1），ε_eCPM_Bid 为广告主出价波动带来的额外噪声。

## Evidence

先验知识/题面给定，逻辑校验通过：基于对数线性化近似，eCPM 的波动系数确实可分解为各驱动因素弹性与波动系数的加权和，且竞争性竞价导致边际递减符合经济学直觉（ε < 1）。

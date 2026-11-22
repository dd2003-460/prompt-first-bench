# N120: 成交周期缩短与成交均价变化的相关性系数r：计算T_cycle与P_final的Pearson相关系数，若假设链（随机偏好噪声导致高W买家直接成交）成立，则r应显

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N33

## Claim

成交周期缩短与成交均价变化的相关性系数r：计算T_cycle与P_final的Pearson相关系数，若假设链（随机偏好噪声导致高W买家直接成交）成立，则r应显著为负（r < -0.3），否则若r接近0或正，则支持平台曝光倾斜假设而非买家偏好假设。

## Corrected Claim

成交周期缩短与成交均价变化的相关性系数r：计算T_cycle与P_final的Pearson相关系数，若假设链（随机偏好噪声导致高W买家直接成交）成立，则r应显著为负，否则若r接近0或正，则支持平台曝光倾斜假设而非买家偏好假设。

## Evidence

[质询]该陈述将特定假设下的预期统计结果（r < -0.3）作为事实节点，但缺乏实际数据支持，且阈值-0.3的设定缺乏理论依据，属于经验性判断而非逻辑必然。 | 逻辑自洽：若高W买家因随机噪声直接成交，则T_cycle短且P_final高（接近W），导致负相关；反之若平台曝光倾斜，相关性可能减弱或消失。但无外部来源支持具体阈值-0.3，且source=search，经验事实缺来源支持。

## Search Query

correlation between transaction time and final price second-hand marketplace high premium group

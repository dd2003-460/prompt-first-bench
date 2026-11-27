# N282: 咨询概率 P(Consult) 的联合函数：P(Consult) = P_base * (1 + γ_T * ΔTrust) * (1 - γ_S * |ΔSi

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N76

## Claim

咨询概率 P(Consult) 的联合函数：P(Consult) = P_base * (1 + γ_T * ΔTrust) * (1 - γ_S * |ΔSignal_Strength|)，其中 P_base 为基准咨询率（[待核验]，如 0.3），γ_T 和 γ_S 分别为信任敏感度和信号敏感度（[待核验]，γ_T≈0.5, γ_S≈0.8）。

## Corrected Claim

咨询概率 P(Consult) 可建模为基准咨询率 P_base 与信任及信号强度调整因子的乘积，具体参数（如 P_base, γ_T, γ_S）需根据具体场景数据校准，此处给出的数值（0.3, 0.5, 0.8）为示例假设而非通用事实。

## Evidence

[质询]该陈述包含具体的经验参数（P_base≈0.3, γ_T≈0.5, γ_S≈0.8）和特定的函数形式，属于经验事实或模型假设，无法从第一性原理推导，且参考来源仅涉及通用概率论基础，未提供该特定咨询概率模型的支持。 | 逻辑上公式结构自洽（乘性因子调整基准概率），但参考来源[1][2][3]仅讲解通用联合概率与贝叶斯公式，与该特定咨询概率模型的主题无关，无法提供外部支持；根据经验事实排除条款，缺乏来源直接支持或独立来源一致性，故降级。

## Search Query

buyer consultation probability model trust and signal strength interaction

## Retrieval Sources

- {'url': 'https://blog.csdn.net/beyondqinghua/article/details/106515704&rut=2bb2ed67965c5c71912261efa963c0e852f7c621fe70a04584112f3da5d08589', 'type': 'ddg', 'title': '条件概率、联合概率和贝叶斯公式 - Csdn博客'}
- {'url': 'https://blog.csdn.net/qq_33240556/article/details/154487563&rut=6b6c38596fd43e596d4652d45156fa63fd44f499a99a05a577a4704ff66f928e', 'type': 'ddg', 'title': '概率基础（下）：联合概率、条件概率和贝叶斯法则，这些概率公式究竟能做什么？_联合概率分布公式-csdn博客'}
- {'url': 'https://time.geekbang.org/column/article/80393&rut=5b4d03e3f1ed7f08f7d03c44f32b3132aae982604fd1c2484e49178f8e7d9e57', 'type': 'ddg', 'title': '21 | 概率基础（下）：联合概率、条件概率和贝叶斯法则，这些概率公式究竟能做什么？-程序员的数学基础课-极客时间'}

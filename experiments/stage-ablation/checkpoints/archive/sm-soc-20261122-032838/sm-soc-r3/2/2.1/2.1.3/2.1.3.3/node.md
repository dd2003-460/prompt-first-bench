# N165: 咨询转化率的非线性阈值：当买家池比例 $\Phi((P_{ref} - P_{ask})/\sigma_v)$ 低于某阈值 $\Phi_{th}$（如 5%）时

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N53

## Claim

咨询转化率的非线性阈值：当买家池比例 $\Phi((P_{ref} - P_{ask})/\sigma_v)$ 低于某阈值 $\Phi_{th}$（如 5%）时，咨询量 $N_{inquiry}$ 不再随曝光量 $A_{eff}$ 线性增长，因为买家注意力分散或搜索疲劳。需估计 $\Phi_{th}$ 的值，若 $\Phi_{th} < 2.3\%$，则 $\alpha=9$ 的假设可能失效，导致 $T_{sale}$ 无法缩短。

## Corrected Claim

咨询转化率可能存在非线性阈值效应，当买家池比例低于特定阈值时，咨询量增长可能偏离线性关系，具体阈值需通过实证数据估计。

## Evidence

[质询]该陈述包含具体的经验参数（如阈值5%、2.3%）和特定的因果机制（注意力分散导致非线性），属于经验事实而非第一性原理可推导的数学性质，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

buyer search fatigue threshold low probability items marketplace

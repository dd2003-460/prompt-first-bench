# N199: 工作点1（高曝光-低成本）：假设降价触发算法重新推荐，48小时内曝光量重置系数 R_reset = 1.5，E_exp_new = 1.5 * E_exp_ol

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N65

## Claim

工作点1（高曝光-低成本）：假设降价触发算法重新推荐，48小时内曝光量重置系数 R_reset = 1.5，E_exp_new = 1.5 * E_exp_old，对应开发成本 C_dev = 0，适用于平台主动干预场景。

## Corrected Claim

工作点1（高曝光-低成本）：假设降价触发算法重新推荐，在特定平台干预场景下，曝光量可能经历重置。若重置系数 R_reset 设定为 1.5，则 E_exp_new = 1.5 * E_exp_old，对应开发成本 C_dev = 0。注：系数 1.5 为假设值，需根据具体平台策略验证。

## Evidence

[质询]该陈述包含具体的经验参数（重置系数 R_reset = 1.5、时间窗口 48 小时），这些数值并非第一性原理可推导的数学或物理常数，而是特定业务场景下的经验设定或假设值。参考来源仅讨论了通用的曝光过滤策略（如冷却时间、频率阈值），并未提供或支持“降价触发算法重置”这一特定机制，更未给出 1.5 这一具体系数。因此，该事实属于缺乏来源直接支持的经验性假设。 | 逻辑上自洽（公式 E_new = R * E_old 成立），但参考来源 [1] 仅涉及通用的曝光过滤策略，未覆盖“降价触发重置”及具体系数 1.5，属于经验事实且缺来源直接支持。

## Search Query

Xianyu Zzhuan price reduction algorithm exposure reset coefficient 48 hours

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1919135461055640667&rut=b9cee1ba1eac571bced01e8d976188b5c0e0e456f1668431af32124d44dee7d8', 'type': 'ddg', 'title': '推荐系统资源曝光控制 - 知乎专栏'}

# N18: 更新率对 LRU 命中率的折减量化：有效命中率 H_eff = H_static * (1 - P_update_within_residence)。P_upd

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

更新率对 LRU 命中率的折减量化：有效命中率 H_eff = H_static * (1 - P_update_within_residence)。P_update_within_residence = 1 - exp(-λ_update * T_residence)。T_residence 由 LRU 驱逐策略决定，近似为对象平均驻留时间。对于 λ=0.01/day，若 T_residence ≈ 10 days（基于访问频率），折减因子 ≈ 1 - (1 - e^-0.1) ≈ 0.9048，即命中率打 90.5% 折。

## Corrected Claim

在假设对象更新服从泊松过程且驻留时间固定的模型下，更新率对LRU命中率的折减因子可近似为 1 - (1 - e^(-λT))；对于 λ=0.01/day, T=10 days，折减因子约为 0.9048。

## Evidence

[质询]该陈述构建了一个特定的数学模型（基于指数分布的更新率折减），但参考来源仅讨论LRU/LFU等算法的基本原理和对比，未提供该特定公式或数值推导，属于缺乏来源支持的特定经验/模型假设。 | 逻辑推导自洽（1 - (1 - e^-0.1) ≈ 0.9048 计算正确），但参考来源[1][2][3]仅涉及缓存策略定性对比，未覆盖该具体量化公式，属经验事实/模型假设，缺直接来源支持。

## Retrieval Sources

- {'url': 'https://blog.csdn.net/iymei4986533030/article/details/162550658&rut=264e92570f100786d56b798edd7eb38533abe79c1375d6e3958c9091afc21619', 'type': 'ddg', 'title': '缓存淘汰策略系统性对比——LRU、LFU、ARC、TinyLFU 命中率与内存效率评测_arc缓存淘汰-CSDN博客'}
- {'url': 'https://blog.csdn.net/m0_68089732/article/details/149774778&rut=7974337ebe8930e51d83db753fb7b7e85797b3b7d490bec197b5911061ca4eb8', 'type': 'ddg', 'title': '深入理解缓存淘汰策略：LRU vs LFU 完全解析 - CSDN博客'}
- {'url': 'https://geek-doc.cn/concepts/microarch/cache-replacement-policies-lru&rut=c495efb568066f817f79eb0e2617ab7ad27a1896d4d30d6993b9bd969ecdf2aa', 'type': 'ddg', 'title': '缓存替换策略：Lru、随机与伪 Lru —— 缓存满了踢谁，答案决定命中率 | 极客工场'}

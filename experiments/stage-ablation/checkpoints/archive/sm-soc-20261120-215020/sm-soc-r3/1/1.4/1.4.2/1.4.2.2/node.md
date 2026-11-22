# N88: 最大流量增量 Q_max 的基准定义：Q_max 应定义为‘相对于未降价状态的基准曝光量 Q_base 的相对增量比例’还是‘绝对曝光次数’；需明确 Q_max

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N28

## Claim

最大流量增量 Q_max 的基准定义：Q_max 应定义为‘相对于未降价状态的基准曝光量 Q_base 的相对增量比例’还是‘绝对曝光次数’；需明确 Q_max 在 48h 窗口内的上限约束（如受限于买家搜索频次或推荐池容量），若 Q_max 受限于推荐池容量，则公式需引入饱和项。

## Corrected Claim

Q_max 的定义需结合具体业务场景（如电商流量或污水处理）明确：在电商场景中，需界定其为相对增量比例或绝对值，并考虑推荐池容量等饱和约束；在污水处理场景中，Qmax指最大瞬时流量。当前陈述仅适用于特定电商语境，需补充上下文。

## Evidence

[质询]该陈述属于特定业务场景（电商/流量运营）下的定义探讨，而参考来源[1]讨论的是污水处理工程中的Qmax定义，两者领域完全无关，无法提供外部支持；且该陈述本身是一个待决的定义问题而非既定事实，缺乏唯一确定的标准答案。 | 参考来源[1]主题为污水处理，与电商流量定义无关，属「无可用外部证据」；该陈述为经验性业务定义探讨，逻辑自洽但缺乏来源支持，依据经验事实排除条款判为degraded。

## Search Query

search recommendation pool capacity limit max exposure increment price drop saturation effect

## Retrieval Sources

- {'url': 'https://b2bwiki.baidu.com/article/d0r6l49ftjstjkqn5cog&rut=e612da5278087193c861790a2c6906b0a682e72b615c46d9108aebd596f8d1ff', 'type': 'ddg', 'title': 'Qmax污水处理和设计规模 - b2bwiki.baidu.com'}

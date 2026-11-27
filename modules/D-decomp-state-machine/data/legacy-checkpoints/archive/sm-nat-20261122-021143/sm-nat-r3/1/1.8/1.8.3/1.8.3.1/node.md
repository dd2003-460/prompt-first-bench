# N109: 老化参数 λ 与更新率 u 的定量关系：在标准 LFU-Aging 模型中，频率衰减常数 λ 需与对象更新率 u 匹配以保持稳态频率分布，通常取 λ = u 或

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N41

## Claim

老化参数 λ 与更新率 u 的定量关系：在标准 LFU-Aging 模型中，频率衰减常数 λ 需与对象更新率 u 匹配以保持稳态频率分布，通常取 λ = u 或 λ = u/2；若取 λ = u = 0.01/day，则 λ 的具体数值为 0.01 [待核验：需确认具体文献中 LFU-Aging 的 λ 定义是否直接等于 u 还是存在系数 k]

## Corrected Claim

在 LFU-Aging 类缓存策略中，频率衰减常数 λ 通常需与对象更新率 u 处于同一数量级以维持稳态分布，具体系数（如 λ = u 或 λ = u/2）取决于特定实现或文献定义，并非唯一标准。

## Evidence

[质询]该陈述声称在“标准 LFU-Aging 模型”中通常取 λ = u 或 λ = u/2，这属于具体的工程经验参数或特定文献的设定，而非通用的第一性原理推导结果。不同文献对 LFU-Aging 的变体定义（如指数衰减 vs 线性衰减，时间步长定义）可能导致系数 k 不同，断言“通常取”缺乏普适性，且“标准模型”这一术语在学术界并无唯一统一定义，存在口径混淆风险。 | source=knowledge，逻辑上量纲一致（λ和u均为频率/时间），数值量级合理（0.01/day 是常见的缓存老化速率），但“λ=u 或 λ=u/2”为经验性设定，非严格数学推导，且无外部来源直接支持该特定系数关系，故降级为定性表述。

## Search Query

LFU aging frequency decay constant lambda update rate relation

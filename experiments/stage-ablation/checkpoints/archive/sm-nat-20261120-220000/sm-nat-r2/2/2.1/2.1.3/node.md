# N29: LFU的冷启动惩罚量化为：新对象在首次访问后需要累积 n_warmup 次访问才能进入高频缓存区，n_warmup ≈ f_median / f_min，其中f

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N8

## Claim

LFU的冷启动惩罚量化为：新对象在首次访问后需要累积 n_warmup 次访问才能进入高频缓存区，n_warmup ≈ f_median / f_min，其中f_median为对象访问频率中位数，f_min为最小访问频率；在β=0.9下，n_warmup ≈ 100，导致新对象在最初100次请求内的命中率下降，冷启动惩罚 P_cold = (n_warmup * f_new) / F_total，其中f_new为新对象总请求数

## Corrected Claim

LFU的冷启动惩罚通常表现为新对象因初始频率低而被频繁淘汰，导致初期命中率低于 LRU。量化上，若假设访问频率服从幂律分布，新对象需累积一定次数访问才能稳定在缓存中，具体阈值取决于频率分布参数，而非简单的 f_median / f_min 比值。

## Evidence

[质询]公式 P_cold = (n_warmup * f_new) / F_total 存在量纲和逻辑缺陷：分子是‘访问次数’（n_warmup * f_new），分母是‘总请求数’（F_total），虽然量纲上都是次数，但将‘冷启动惩罚’定义为‘新对象在预热期内的请求占比’在逻辑上并不直接等同于‘命中率下降’或‘惩罚’，且该公式未体现 LFU 算法特有的频率累积机制，更像是一个通用的流量占比公式，缺乏对 LFU 冷启动机制的准确量化描述。 | 先验知识/题面给定，逻辑校验发现公式定义与 LFU 冷启动机制的因果关系不严谨，且 n_warmup ≈ 100 在 β=0.9 下的推导缺乏具体分布假设支持，属于经验性估算而非严格推导。

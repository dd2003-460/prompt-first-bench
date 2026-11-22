# N99: 在缓存容量充足（无驱逐）的情况下，对象更新率 1%/天 导致的有效命中率折损仅取决于更新后对象的陈旧概率。由于所有对象常驻，更新后的对象立即变为陈旧，但下一次访

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

在缓存容量充足（无驱逐）的情况下，对象更新率 1%/天 导致的有效命中率折损仅取决于更新后对象的陈旧概率。由于所有对象常驻，更新后的对象立即变为陈旧，但下一次访问时若内容已更新则命中，折损因子 f_update = 1 - P(updated_before_access)，在稳态下近似为 1 - λ_u * T_access_interval，若 T_access_interval 极短，折损可忽略。

## Corrected Claim

在缓存容量充足（无驱逐）的情况下，对象更新率 1%/天 导致的有效命中率折损仅取决于更新后对象的陈旧概率。由于所有对象常驻，更新后的对象立即变为陈旧，但下一次访问时若内容已更新则命中，折损因子 f_update = 1 - P(updated_before_access)，在稳态下近似为 1 - λ_u * T_access_interval，若 T_access_interval 极短，折损可忽略。

## Evidence

检索失败: no sources from any channel (all 5 failed)

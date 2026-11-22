# N159: Top 10% 热门对象平均驻留时间 T_resident ≈ 0.5 天的计算基础：基于 LRU 队列长度 L_queue ≈ C_norm * N = 11

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N55

## Claim

Top 10% 热门对象平均驻留时间 T_resident ≈ 0.5 天的计算基础：基于 LRU 队列长度 L_queue ≈ C_norm * N = 11,900 对象，Top 10% 对象数 N_hot = 10,000，其访问间隔 Δt_avg = R_total / (N_hot * λ_avg) = 50,000,000 / (10,000 * 500) = 10 天，但 LRU 驱逐间隔由缓存容量决定，T_resident ≈ L_queue / (N_hot * λ_avg) ≈ 0.238 天，需修正为 0.5 天的理由需进一步验证。

## Corrected Claim

基于给定参数 L_queue=11,900, N_hot=10,000, λ_avg=500，计算得出的平均驻留时间约为 0.0024 天（约3.4分钟），而非 0.5 天；若需得出 0.5 天的结论，需重新审视 λ_avg 或 L_queue 的定义与数值。

## Evidence

[质询]数值计算存在内部矛盾：根据公式 T_resident ≈ L_queue / (N_hot * λ_avg)，代入数值 11900 / (10000 * 500) = 0.00238 天，而非陈述中声称的 0.238 天（相差100倍）；且从 0.00238 天修正到 0.5 天缺乏明确的物理或逻辑依据，属于强行凑数。 | 逻辑校验发现量级错误（0.00238 vs 0.238）及推导过程断裂，且无外部来源支持该经验性估算值。

## Search Query

LRU resident time top 10% hot objects calculation

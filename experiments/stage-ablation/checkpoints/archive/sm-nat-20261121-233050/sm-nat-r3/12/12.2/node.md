# N186: 容量加权平均驻留时间 T_res_cap_avg 的数值估算：T_res_cap_avg = Σ (S_i/M) * T_res_i。Top 10% 对象（9,

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N72

## Claim

容量加权平均驻留时间 T_res_cap_avg 的数值估算：T_res_cap_avg = Σ (S_i/M) * T_res_i。Top 10% 对象（9,000个）占用 17.6% 容量，平均 T_res 较短（因高频访问，快速周转但频繁命中，驻留时间取决于驱逐而非访问间隔，但在 LRU 中高频对象不易被驱逐，驻留时间趋近于缓存寿命）。实际上，在 LRU 中，高频对象一旦进入缓存，除非被更新或容量压力极大，否则一直驻留。因此，对于 M/C≈1.0 的情况，大多数对象（包括头部）的 T_res_i ≈ T_cache_lifetime（即对象在缓存中直到被更新或系统重启）。若假设系统稳定运行，T_res_i ≈ 1/u = 100天（因为更新率主导失效）。因此 T_res_cap_avg ≈ 100天。

## Corrected Claim

容量加权平均驻留时间 T_res_cap_avg 的数值估算：T_res_cap_avg = Σ (S_i/M) * T_res_i。Top 10% 对象（9,000个）占用 17.6% 容量，平均 T_res 较短（因高频访问，快速周转但频繁命中，驻留时间取决于驱逐而非访问间隔，但在 LRU 中高频对象不易被驱逐，驻留时间趋近于缓存寿命）。实际上，在 LRU 中，高频对象一旦进入缓存，除非被更新或容量压力极大，否则一直驻留。因此，对于 M/C≈1.0 的情况，大多数对象（包括头部）的 T_res_i ≈ T_cache_lifetime（即对象在缓存中直到被更新或系统重启）。若假设系统稳定运行，T_res_i ≈ 1/u = 100天（因为更新率主导失效）。因此 T_res_cap_avg ≈ 100天。

## Evidence

先验知识/题面给定，逻辑校验通过：在LRU缓存中，高频对象因不易被驱逐，其驻留时间确实由更新率（失效机制）主导而非访问间隔，故T_res_i ≈ 1/u的推导符合缓存替换算法的基本原理。

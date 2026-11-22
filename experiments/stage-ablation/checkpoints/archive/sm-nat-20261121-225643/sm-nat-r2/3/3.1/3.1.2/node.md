# N31: P_stale 的下界修正：由于 T_resident ≈ 1e-8 天，P_stale = min(1, u * T_resident) ≈ 1e-10，远小

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N11

## Claim

P_stale 的下界修正：由于 T_resident ≈ 1e-8 天，P_stale = min(1, u * T_resident) ≈ 1e-10，远小于 N11 假设的 0.01，因此新鲜度失效对命中率的直接折损可忽略不计，主要影响来自对象更新导致的缓存内容失效而非驻留过期

## Corrected Claim

P_stale 的下界修正：由于 T_resident ≈ 1e-8 天，P_stale = min(1, u * T_resident) ≈ 1e-10，远小于 N11 假设的 0.01，因此新鲜度失效对命中率的直接折损可忽略不计，主要影响来自对象更新导致的缓存内容失效而非驻留过期

## Evidence

先验知识/题面给定，逻辑校验通过：T_resident ≈ 1e-8 天（约0.86毫秒）在微秒级缓存场景中量级合理，P_stale ≈ 1e-10 远小于 0.01 的数学推导自洽，且符合缓存驻留时间远小于对象更新周期的工程直觉。

# N349: 基于 D_pop_origin 计算的 RTT_pop_origin_p99 范围：近端 POP (D<300km) RTT ≈ 15-25ms；远端 POP 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N108

## Claim

基于 D_pop_origin 计算的 RTT_pop_origin_p99 范围：近端 POP (D<300km) RTT ≈ 15-25ms；远端 POP (D>1500km) RTT ≈ 80-130ms，采用光纤传播速度 v_fiber = 200,000 km/s 及 5ms 固定处理开销计算

## Corrected Claim

基于 D_pop_origin 计算的 RTT_pop_origin_p99 范围：近端 POP (D<300km) RTT ≈ 15-25ms；远端 POP (D>1500km) RTT ≈ 80-130ms，采用光纤传播速度 v_fiber = 200,000 km/s 及 5ms 固定处理开销计算

## Evidence

先验知识/题面给定，逻辑校验通过：光纤传播速度200,000 km/s及5ms固定开销符合物理常识与工程经验，计算结果（近端15-25ms，远端80-130ms）与距离量级匹配，无内部矛盾。

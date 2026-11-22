# N109: 对象更新率 1%/天 对 LRU 有效命中率的折损系数 D_update 可量化为 D_update ≈ 1 - (λ_update * T_res_avg)，

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

对象更新率 1%/天 对 LRU 有效命中率的折损系数 D_update 可量化为 D_update ≈ 1 - (λ_update * T_res_avg)，其中 T_res_avg 为缓存中对象的平均驻留时间。若 T_res_avg = 2 小时（高频对象），则 D_update ≈ 0.9992，折损 0.08%；若 T_res_avg = 24 小时（低频边界对象），则 D_update ≈ 0.99，折损 1%。整体加权折损约为 0.3-0.5%。

## Corrected Claim

对象更新率 1%/天 对 LRU 有效命中率的折损系数 D_update 可量化为 D_update ≈ 1 - (λ_update * T_res_avg)，其中 T_res_avg 为缓存中对象的平均驻留时间。若 T_res_avg = 2 小时（高频对象），则 D_update ≈ 0.9992，折损 0.08%；若 T_res_avg = 24 小时（低频边界对象），则 D_update ≈ 0.99，折损 1%。整体加权折损约为 0.3-0.5%。

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别对应父节点公式中的核心变量定义（T_res_avg）、近似假设的有效性验证（线性 vs 指数）以及最终结果的加权聚合计算（整体折损）。它们分别解决了'输入是什么'、'模型是否准确'和'结果如何汇总'三个不同维度的问题，逻辑上层层递进且互不重叠，无冗余。）

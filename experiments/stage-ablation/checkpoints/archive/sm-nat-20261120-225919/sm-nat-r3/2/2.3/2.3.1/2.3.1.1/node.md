# N147: 对于热门对象（R_i 高），τ_res(i) = 1/R_i 极短（如 R_i=1000次/天，τ_res=0.001天），远小于 τ_obj=100天，因此热

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N47

## Claim

对于热门对象（R_i 高），τ_res(i) = 1/R_i 极短（如 R_i=1000次/天，τ_res=0.001天），远小于 τ_obj=100天，因此热门对象几乎不受更新失效影响，其命中率折损因子 D_hot ≈ 1。

## Corrected Claim

对于热门对象（R_i 高），τ_res(i) = 1/R_i 极短（如 R_i=1000次/天，τ_res=0.001天），远小于 τ_obj=100天，因此热门对象几乎不受更新失效影响，其命中率折损因子 D_hot ≈ 1。

## Evidence

先验知识/题面给定，逻辑校验通过：τ_res=1/R_i 与 τ_obj 的量级对比符合直觉，热门对象更新频率高导致失效时间短，命中率折损因子接近1在逻辑上自洽。

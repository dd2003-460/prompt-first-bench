# N226: 候选B的稀缺度参数 S 的稳健性检验：S = 1/N_supply 在 N_supply 接近 0 时发散，需引入正则化项 S_robust = 1/(N_su

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N72

## Claim

候选B的稀缺度参数 S 的稳健性检验：S = 1/N_supply 在 N_supply 接近 0 时发散，需引入正则化项 S_robust = 1/(N_supply + δ)，其中 δ 为平滑常数（如 δ=1 或基于贝叶斯先验的伪计数），以避免算法在长尾商品上给出极端建议价。

## Corrected Claim

候选B的稀缺度参数 S 的稳健性检验：S = 1/N_supply 在 N_supply 接近 0 时发散，需引入正则化项 S_robust = 1/(N_supply + δ)，其中 δ 为平滑常数（如 δ=1 或基于贝叶斯先验的伪计数），以避免算法在长尾商品上给出极端建议价。

## Evidence

先验知识/题面给定，逻辑校验通过：S=1/N在N趋近0时发散是数学事实，引入正则化项δ（如拉普拉斯平滑/贝叶斯伪计数）是处理长尾稀疏数据的标准且逻辑自洽的工程手段。

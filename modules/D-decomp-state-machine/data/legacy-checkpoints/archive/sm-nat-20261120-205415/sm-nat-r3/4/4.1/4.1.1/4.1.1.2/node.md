# N156: 缓存容量 C=128GB (131072MB) 对应的边界大小 S_max 需通过数值解方程 ∫_{1}^{S_max} s * 0.1 * s^{-1.2} 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N56

## Claim

缓存容量 C=128GB (131072MB) 对应的边界大小 S_max 需通过数值解方程 ∫_{1}^{S_max} s * 0.1 * s^{-1.2} ds = 131072 求得，该积分收敛条件要求 α>2 才能解析求和，但此处 α=1.1 需截断处理。

## Corrected Claim

缓存容量 C=128GB (131072MB) 对应的边界大小 S_max 需通过数值解方程 ∫_{1}^{S_max} s * 0.1 * s^{-1.2} ds = 131072 求得，该积分收敛条件要求 α>2 才能解析求和，但此处 α=1.1 需截断处理。

## Search Query

Pareto distribution alpha 1.1 truncated integral capacity constraint

## Retrieval Sources

- {'url': 'https://baike.baidu.com/item/%E7%BC%93%E5%AD%98%E5%AE%B9%E9%87%8F/3441069&rut=775c216078ae2ab8840ba841b2eaefcebfc392a0a136c3e70f7fac90df628e83', 'type': 'ddg', 'title': '缓存容量 - 百度百科'}
- {'url': 'https://baike.baidu.com/item/%E7%BC%93%E5%AD%98%E5%A4%A7%E5%B0%8F/3968429&rut=8a6b7c4467bf853fc1fd261990091fa0bdeb4be708f0f14fa9f213ec708bb5c0', 'type': 'ddg', 'title': '缓存大小_百度百科'}

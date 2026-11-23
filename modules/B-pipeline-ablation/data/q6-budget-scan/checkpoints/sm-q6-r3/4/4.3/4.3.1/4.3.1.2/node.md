# N247: 带宽价格的地域修正系数 $f_{region}$：二线城市约为一线城市的 0.7-0.8 倍，三线及以下城市约为 0.5-0.6 倍；若 10 个 POP 点分

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N85, N86, N87

## Claim

带宽价格的地域修正系数 $f_{region}$：二线城市约为一线城市的 0.7-0.8 倍，三线及以下城市约为 0.5-0.6 倍；若 10 个 POP 点分布在 3 个一线、4 个二线、3 个三线城市，加权平均单价 $P_{avg} = \sum (n_i \times P_i \times f_{region,i}) / 10$。

## Corrected Claim

带宽价格的地域修正系数 $f_{region}$：二线城市约为一线城市的 0.7-0.8 倍，三线及以下城市约为 0.5-0.6 倍；若 10 个 POP 点分布在 3 个一线、4 个二线、3 个三线城市，加权平均单价 $P_{avg} = \sum (n_i \times P_i \times f_{region,i}) / 10$。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

dedicated line pricing difference between tier-1 and tier-2 cities in China

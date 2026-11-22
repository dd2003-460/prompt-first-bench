# N93: 计算最热门 10% 对象（k=10,000）的总字节请求量贡献占比，即 (10,000 * 77KB * r_avg_top) / Total_Byte_Tra

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N36

## Claim

计算最热门 10% 对象（k=10,000）的总字节请求量贡献占比，即 (10,000 * 77KB * r_avg_top) / Total_Byte_Traffic，该值直接用于 N44 中命中率分子的大小加权因子计算。

## Corrected Claim

计算最热门 10% 对象（k=10,000）的总字节请求量贡献占比，即 (10,000 * 77KB * r_avg_top) / Total_Byte_Traffic，该值直接用于 N44 中命中率分子的大小加权因子计算。

## Evidence

先验知识/题面给定，逻辑校验通过

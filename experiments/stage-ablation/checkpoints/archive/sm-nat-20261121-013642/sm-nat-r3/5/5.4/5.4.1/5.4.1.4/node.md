# N218: Belady MIN 算法在 N=100,000 对象、R_total=5e7 请求规模下的内存占用：需存储每个对象的 next_access_time 数组（

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N74

## Claim

Belady MIN 算法在 N=100,000 对象、R_total=5e7 请求规模下的内存占用：需存储每个对象的 next_access_time 数组（N * 4 bytes = 0.4MB）及请求序列（R_total * 4 bytes = 200MB），总内存占用约 200.4MB，远低于 128GB 缓存容量，因此内存不是瓶颈，CPU 计算是主要耗时因素。

## Corrected Claim

Belady MIN 算法在 N=100,000 对象、R_total=5e7 请求规模下的内存占用：需存储每个对象的 next_access_time 数组（N * 4 bytes = 0.4MB）及请求序列（R_total * 4 bytes = 200MB），总内存占用约 200.4MB，远低于 128GB 缓存容量，因此内存不是瓶颈，CPU 计算是主要耗时因素。

## Evidence

先验知识/题面给定，逻辑校验通过：内存占用计算（0.4MB + 200MB ≈ 200.4MB）量级正确且远小于128GB，结论符合逻辑。

# N92: 128GB 缓存覆盖前 20% 对象的可行性条件：设前 20% 对象的总字节量为 S_top20 = 0.2 * N * E[S | top 20%]，其中 E

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N30

## Claim

128GB 缓存覆盖前 20% 对象的可行性条件：设前 20% 对象的总字节量为 S_top20 = 0.2 * N * E[S | top 20%]，其中 E[S | top 20%] 为前 20% 对象的平均大小；缓存可行性要求 S_top20 ≤ 128GB，即 E[S | top 20%] ≤ 128GB / (0.2 * 100000) = 6.4KB；若实际平均大小超过 6.4KB，则 128GB 缓存无法覆盖前 20% 对象，静态字节命中率上限需下调。

## Corrected Claim

128GB 缓存覆盖前 20% 对象的可行性条件：设前 20% 对象的总字节量为 S_top20 = 0.2 * N * E[S | top 20%]，其中 E[S | top 20%] 为前 20% 对象的平均大小；缓存可行性要求 S_top20 ≤ 128GB，即 E[S | top 20%] ≤ 128GB / (0.2 * 100000) = 6.4KB；若实际平均大小超过 6.4KB，则 128GB 缓存无法覆盖前 20% 对象，静态字节命中率上限需下调。

## Evidence

[rework-angle r1] 逻辑推导成立，来源未直接覆盖

## Search Query

Zipf distribution top 20% objects average size 100k

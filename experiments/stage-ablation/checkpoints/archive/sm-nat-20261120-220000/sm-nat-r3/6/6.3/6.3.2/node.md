# N132: 未缓存尾部对象（Rank 10001-100000）的字节占比 $S_{tail}/S_{total}$ 需通过 Pareto(α=1.1) 积分计算：$\fr

- **status**: verified
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N51

## Claim

未缓存尾部对象（Rank 10001-100000）的字节占比 $S_{tail}/S_{total}$ 需通过 Pareto(α=1.1) 积分计算：$\frac{\int_{S_{rank10000}}^{\infty} x f(x) dx}{\int_{S_{min}}^{\infty} x f(x) dx}$。由于 α=1.1 < 2，积分发散，需引入 S_max 截断进行数值积分估算。

## Corrected Claim

未缓存尾部对象（Rank 10001-100000）的字节占比 $S_{tail}/S_{total}$ 需通过 Pareto(α=1.1) 积分计算：$\frac{\int_{S_{rank10000}}^{\infty} x f(x) dx}{\int_{S_{min}}^{\infty} x f(x) dx}$。由于 α=1.1 < 2，积分发散，需引入 S_max 截断进行数值积分估算。

## Evidence

[rework-angle r1] 逻辑推导成立，来源未直接覆盖

## Search Query

cache tail object size distribution rank vs size correlation

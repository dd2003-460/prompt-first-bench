# N197: 当 α < 2 时，Pareto 分布的原始均值公式 E[S] = (α-1)s_min/(α-2) 失效（分母为负），必须使用截断形式；在 α=1.1 时，原

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N70

## Claim

当 α < 2 时，Pareto 分布的原始均值公式 E[S] = (α-1)s_min/(α-2) 失效（分母为负），必须使用截断形式；在 α=1.1 时，原始公式给出 -1.22KB 的无意义负值，而截断公式给出 1.22KB 的正值，两者符号相反但绝对值相同，表明截断处理是必要的。

## Corrected Claim

当 α < 2 时，Pareto 分布的原始均值公式 E[S] = (α-1)s_min/(α-2) 失效（分母为负），必须使用截断形式；在 α=1.1 时，原始公式给出 -1.22KB 的无意义负值，而截断公式给出 1.22KB 的正值，两者符号相反但绝对值相同，表明截断处理是必要的。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布均值公式在α<2时发散或无定义，截断处理是必要的，数值计算符合逻辑推导。

## Search Query

why truncated Pareto mean is needed when alpha < 2

# N8: 大小 S 与热度 R 的负相关系数 ρ≈-0.3 需通过 Copula 函数（如 Gaussian Copula 或 Clayton Copula）构建联合分布

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

大小 S 与热度 R 的负相关系数 ρ≈-0.3 需通过 Copula 函数（如 Gaussian Copula 或 Clayton Copula）构建联合分布 F(S,R)，以捕捉边缘分布与依赖结构的完整联合概率密度函数 f(S,R)

## Corrected Claim

大小 S 与热度 R 的负相关系数 ρ≈-0.3 需通过 Copula 函数（如 Gaussian Copula 或 Clayton Copula）构建联合分布 F(S,R)，以捕捉边缘分布与依赖结构的完整联合概率密度函数 f(S,R)

## Evidence

父节点级核验通过：正交+完备+无冗余（两个子节点分别描述了 Gaussian 和 Clayton 两种不同 Copula 函数下的具体构建方法，彼此独立且不矛盾（正交）。父节点明确提到了这两种 Copula 作为示例，子节点完整覆盖了这两个具体案例（完备）。虽然它们都是构建联合分布的手段，但代表了不同的数学模型和依赖结构假设（线性 vs 尾部依赖），并非同一参数的不同取值，因此不构成冗余。）

# N35: 假设 x_min = 4KB (CDN 常见最小对象大小)，且截断于 x_max = 100MB (CDN 常见最大对象大小)，计算 E[S] = ∫_{4KB

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N6

## Claim

假设 x_min = 4KB (CDN 常见最小对象大小)，且截断于 x_max = 100MB (CDN 常见最大对象大小)，计算 E[S] = ∫_{4KB}^{100MB} x * (α * x_min^α / x^{α+1}) dx 的数值结果。

## Corrected Claim

假设 x_min = 4KB, x_max = 100MB，且对象大小服从截断帕累托分布，则 E[S] 的解析解为 [x_max^{1-α} - x_min^{1-α}] / (1-α) (当 α≠1) 或 ln(x_max/x_min) (当 α=1)，具体数值取决于参数 α。

## Evidence

父节点级核验通过：正交+完备+无冗余（分解结构清晰，逻辑正交。子节点分别覆盖了理论推导、参数物理意义、基准计算、基准影响分析、敏感性计算、敏感性影响分析及偏差量化，无重复且无矛盾。虽然存在基准与敏感性两组计算，但它们服务于不同的参数场景，属于必要的对比分析而非冗余。）

## Search Query

CDN object size distribution average size 4KB to 100MB Pareto alpha 1.1

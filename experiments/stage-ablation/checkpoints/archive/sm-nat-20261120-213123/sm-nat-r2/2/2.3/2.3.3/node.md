# N41: 在 $\rho=-0.3$ 的负相关假设下，Top-k 热门对象的平均大小 $E[S|H_{top-k}]$ 相对于独立假设 $E[S]$ 的修正因子为 $1 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

在 $\rho=-0.3$ 的负相关假设下，Top-k 热门对象的平均大小 $E[S|H_{top-k}]$ 相对于独立假设 $E[S]$ 的修正因子为 $1 + \rho \cdot \sigma_{\log S} \cdot \sigma_{\log H} \cdot \frac{1}{k^{1/\beta}}$ 的近似形式，需代入 $\sigma$ 值计算具体偏差百分比。

## Corrected Claim

在 $\rho=-0.3$ 的负相关假设下，Top-k 热门对象的平均大小 $E[S|H_{top-k}]$ 相对于独立假设 $E[S]$ 的修正因子为 $1 + \rho \cdot \sigma_{\log S} \cdot \sigma_{\log H} \cdot \frac{1}{k^{1/\beta}}$ 的近似形式，需代入 $\sigma$ 值计算具体偏差百分比。

## Evidence

先验知识/题面给定，逻辑校验通过

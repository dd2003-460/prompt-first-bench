# N104: θ_refresh 的算法实现机制：买家端刷新阈值并非固定值，而是动态函数 θ_refresh = θ_base + k_volatility * σ_mark

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29, N31, N32

## Claim

θ_refresh 的算法实现机制：买家端刷新阈值并非固定值，而是动态函数 θ_refresh = θ_base + k_volatility * σ_market，其中 θ_base 为基准阈值（通常 3%-5%），k_volatility 为波动率系数，σ_market 为近7日同类商品价格标准差。当市场波动率 σ_market 较高时，θ_refresh 自动上调至 8%-12%，以过滤噪声波动；当 σ_market 较低时，θ_refresh 下调至 3%-5%，以捕捉微小价格优势。

## Corrected Claim

θ_refresh 的算法实现机制：买家端刷新阈值并非固定值，而是动态函数 θ_refresh = θ_base + k_volatility * σ_market，其中 θ_base 为基准阈值（通常 3%-5%），k_volatility 为波动率系数，σ_market 为近7日同类商品价格标准差。当市场波动率 σ_market 较高时，θ_refresh 自动上调至 8%-12%，以过滤噪声波动；当 σ_market 较低时，θ_refresh 下调至 3%-5%，以捕捉微小价格优势。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

dynamic price update threshold algorithm volatility adjustment e-commerce

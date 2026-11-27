# N101: 代入修正后的参数计算具体偏差：取 $\rho=-0.3$, $\sigma_{\log S} \approx 0.909$ (基于 $1/\alpha$ 修正)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N41

## Claim

代入修正后的参数计算具体偏差：取 $\rho=-0.3$, $\sigma_{\log S} \approx 0.909$ (基于 $1/\alpha$ 修正), $\sigma_{\log H} \approx 1.111$ (基于 $1/\beta$ 修正)。对于 Top-6700 对象（$k/N=0.067$），在 Pareto(0.9) 下其热度阈值对应的对数偏移量 $\Delta \log H \approx \ln(N/k) = \ln(10^5/6700) \approx 2.70$。修正因子 $K(\rho) \approx \exp(\rho \cdot \frac{\sigma_{\log S}}{\sigma_{\log H}} \cdot 2.70) \approx \exp(-0.3 \cdot 0.818 \cdot 2.70) \approx \exp(-0.663) \approx 0.515$。即热门对象平均大小仅为全局平均的 51.5%，偏差约 -48.5%。

## Corrected Claim

代入修正后的参数计算具体偏差：取 $\rho=-0.3$, $\sigma_{\log S} \approx 0.909$ (基于 $1/\alpha$ 修正), $\sigma_{\log H} \approx 1.111$ (基于 $1/\beta$ 修正)。对于 Top-6700 对象（$k/N=0.067$），在 Pareto(0.9) 下其热度阈值对应的对数偏移量 $\Delta \log H \approx \ln(N/k) = \ln(10^5/6700) \approx 2.70$。修正因子 $K(\rho) \approx \exp(\rho \cdot \frac{\sigma_{\log S}}{\sigma_{\log H}} \cdot 2.70) \approx \exp(-0.3 \cdot 0.818 \cdot 2.70) \approx \exp(-0.663) \approx 0.515$。即热门对象平均大小仅为全局平均的 51.5%，偏差约 -48.5%。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算准确（ln(100000/6700)≈2.70, exp(-0.3*0.818*2.70)≈0.515），量纲与逻辑自洽。

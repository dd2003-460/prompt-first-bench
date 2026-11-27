# N145: 短序列（10^5 请求）模拟中 LRU 命中率的样本方差 $\sigma^2_{short}$ 的理论下界为 $\frac{H(1-H)}{n}$，其中 $H 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N66

## Claim

短序列（10^5 请求）模拟中 LRU 命中率的样本方差 $\sigma^2_{short}$ 的理论下界为 $\frac{H(1-H)}{n}$，其中 $H \approx 0.95$（基于全量驻留假设），$n=10^5$，计算得 $\sigma_{short} \approx \sqrt{0.0475/100000} \approx 0.00069$，远小于 N66 声称的 0.012，表明 N66 的 $\sigma_{approx}$ 主要来源于序列间负载分布的随机性而非单次模拟的统计噪声。

## Corrected Claim

短序列（10^5 请求）模拟中 LRU 命中率的样本方差 $\sigma^2_{short}$ 的理论下界为 $\frac{H(1-H)}{n}$，其中 $H \approx 0.95$（基于全量驻留假设），$n=10^5$，计算得 $\sigma_{short} \approx \sqrt{0.0475/100000} \approx 0.00069$，远小于 N66 声称的 0.012，表明 N66 的 $\sigma_{approx}$ 主要来源于序列间负载分布的随机性而非单次模拟的统计噪声。

## Evidence

先验知识/题面给定，逻辑校验通过：二项分布方差公式 $H(1-H)/n$ 应用正确，数值计算 $\sqrt{0.0475/100000} \approx 0.00069$ 准确，且与 0.012 的量级对比逻辑自洽。

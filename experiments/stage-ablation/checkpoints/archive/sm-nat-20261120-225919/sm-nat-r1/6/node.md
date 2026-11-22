# N24: 在Pareto(α=1.1)分布下，累积大小占比公式为 CDF_size(k) ≈ 1 - (k/N)^(α-1)，需计算满足 Σ_{i=1}^k S_i ≤ 

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

在Pareto(α=1.1)分布下，累积大小占比公式为 CDF_size(k) ≈ 1 - (k/N)^(α-1)，需计算满足 Σ_{i=1}^k S_i ≤ 128GB 的最大对象数 k_max，以确定工作集边界。

## Corrected Claim

在Pareto(α=1.1)分布下，若对象大小服从幂律分布，累积大小占比可近似表示为 CDF_size(k) ≈ 1 - (k/N)^(α-1)（其中N为归一化常数或总对象数，具体取决于排序方式），需结合具体分布参数计算满足 Σ_{i=1}^k S_i ≤ 128GB 的最大对象数 k_max。

## Evidence

[质询]公式形式存在歧义且缺乏具体参数定义：陈述中的 CDF_size(k) ≈ 1 - (k/N)^(α-1) 并非标准帕累托分布的累积分布函数（CDF）标准形式，而是基于特定假设（如对象按大小排序且遵循幂律）推导出的累积质量占比近似式。此外，未明确 N 的定义（是总对象数还是归一化常数）以及 S_i 的具体分布参数（如最小大小 x_min），导致该公式在严格数学意义上不自洽，仅作为工程近似存在。 | 来源 [1] 和 [2] 提供了帕累托分布的标准定义 P(X>x) = (x/x_min)^k，但未直接支持陈述中特定的累积大小占比近似公式 CDF_size(k) ≈ 1 - (k/N)^(α-1)。该公式属于基于幂律特性的工程推导，逻辑上自洽（符合长尾分布特性），但属于经验/近似事实，且来源未直接覆盖该特定近似式，故降级。

## Retrieval Sources

- {'url': 'https://zh.wikipedia.org/wiki/%E5%B8%95%E7%B4%AF%E6%89%98%E5%88%86%E5%B8%83&rut=91134896ab05b53f585edeb3a097a30f9edf0fa7dafb66749cede7728abb67cb', 'type': 'ddg', 'title': '帕累托分布 - 维基百科，自由的百科全书'}
- {'url': 'https://zh.wikipedia.org/zh-cn/%E5%B8%95%E7%B4%AF%E6%89%98%E5%88%86%E5%B8%83&rut=379f65858cddb53352b67da4bf034c45435017eda435e4720403e042186180cf', 'type': 'ddg', 'title': '帕累托分布 - 维基百科，自由的百科全书'}

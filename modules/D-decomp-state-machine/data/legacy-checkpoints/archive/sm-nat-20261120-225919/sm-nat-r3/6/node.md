# N24: 在Pareto(α=1.1)分布下，累积大小占比公式为 CDF_size(k) ≈ 1 - (k/N)^(α-1)，需计算满足 Σ_{i=1}^k S_i ≤ 

- **status**: pending
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

父节点级核验未通过：非正交, 有冗余（子节点之间存在逻辑矛盾和冗余。节点4计算出的 k_max 上限为 100,000，节点5直接重复并简化了这一结论，且节点5中'缓存容量远大于所有小对象总和'的假设与节点2中'总大小约5TB'严重矛盾，导致逻辑不自洽。此外，节点4和5都在处理'总对象数限制'这一边界条件，属于冗余。）

## Retrieval Sources

- {'url': 'https://zh.wikipedia.org/wiki/%E5%B8%95%E7%B4%AF%E6%89%98%E5%88%86%E5%B8%83&rut=91134896ab05b53f585edeb3a097a30f9edf0fa7dafb66749cede7728abb67cb', 'type': 'ddg', 'title': '帕累托分布 - 维基百科，自由的百科全书'}
- {'url': 'https://zh.wikipedia.org/zh-cn/%E5%B8%95%E7%B4%AF%E6%89%98%E5%88%86%E5%B8%83&rut=379f65858cddb53352b67da4bf034c45435017eda435e4720403e042186180cf', 'type': 'ddg', 'title': '帕累托分布 - 维基百科，自由的百科全书'}

# N314: Clopper-Pearson精确区间[0.498, 0.700]对应的F分布临界值计算：下界$\hat{p}_L = \frac{n\hat{p}}{n\ha

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N91

## Claim

Clopper-Pearson精确区间[0.498, 0.700]对应的F分布临界值计算：下界$\hat{p}_L = \frac{n\hat{p}}{n\hat{p} + (n-k+1)F_{2k, 2(n-k+1); 0.975}}$，其中k=60, n=100，需查表或计算F(120, 80; 0.975)的具体数值以验证分母。

## Corrected Claim

Clopper-Pearson精确区间下界公式形式正确，需通过统计软件或查表获取F(120, 80; 0.975)的具体数值以完成计算验证。

## Evidence

[质询]参考来源仅提供了Clopper-Pearson区间的一般性描述，未提供具体的F分布临界值数值或针对k=60, n=100的具体计算结果，无法直接验证分母中F(120, 80; 0.975)的具体数值是否正确。 | 逻辑校验通过：Clopper-Pearson区间的下界公式形式正确，F分布自由度的设定（2k, 2(n-k+1)）符合统计学标准定义，量纲和逻辑自洽。但来源[1]仅定性描述该方法，未提供具体数值支持，属于间接支持/无关具体数值，故降级。

## Search Query

F distribution critical value 120 80 0.975 Clopper Pearson interval calculation

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2066843943493440950&rut=e19d5c1f4c4c04e58e0545e66f5ec387571aa7d03915c85c6c78eb0f690ff460', 'type': 'ddg', 'title': 'Clopper-Pearson 置信区间 - 知乎'}

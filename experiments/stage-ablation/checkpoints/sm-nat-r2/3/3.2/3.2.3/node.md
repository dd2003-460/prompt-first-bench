# N53: 工作点 B（中热度/中对象）：对于热度排名 1%-10% 的对象，假设其平均大小为 5 KB，则剩余容量可容纳 K_B = (128 GB - Top1%_By

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N15

## Claim

工作点 B（中热度/中对象）：对于热度排名 1%-10% 的对象，假设其平均大小为 5 KB，则剩余容量可容纳 K_B = (128 GB - Top1%_Bytes) / 5000 ≈ 20,000 个对象，覆盖热度累积占比 F_B ≈ 5%，此部分对象在 LRU 中因大小较大而可能被挤出，但在 LFU 中因频率较高而保留。

## Corrected Claim

工作点 B（中热度/中对象）：对于热度排名 1%-10% 的对象，假设其平均大小为 5 KB，在 128 GB 缓存且 Top 1% 对象占用大部分容量的假设下，剩余容量可容纳约 20,000 个此类对象。此部分对象在 LRU 中可能因访问间隔较长而被挤出，但在 LFU 中因访问频率较高而更可能被保留。

## Evidence

[质询]该陈述包含具体的经验数值假设（如Top 1%对象占用空间、剩余容量计算结果、热度累积占比5%），这些并非第一性原理可推导的数学事实，而是依赖于特定数据集的统计分布。参考来源中未提供支撑这些具体数值（如128GB缓存下Top 1%占用量、5KB平均大小对应的对象数量及热度占比）的数据或案例，属于缺乏外部证据支持的经验断言。 | 逻辑上算术运算自洽（(128GB - Top1%) / 5KB ≈ 20,000 隐含 Top1% 占用约 128GB - 100MB ≈ 127.9GB，量级合理），且 LRU/LFU 行为描述符合缓存理论常识；但具体数值（20,000个对象、5%热度占比）为经验事实，参考来源 [1]-[4] 均未提供直接数据支持，仅 [1] 提供通用缓存背景，故降级。

## Search Query

Pareto beta 0.9 1% to 10% cumulative frequency range

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/Cache_%28computing%29', 'type': None, 'title': 'wiki-full: Cache (computing)'}
- {'url': 'https://en.wikipedia.org/wiki/Less_frequently_used', 'type': None, 'title': 'direct-browser: https://en.wikipedia.org/wiki/Less_frequently_used'}
- {'url': 'https://en.wikipedia.org/wiki/Least_recently_used_cache_replacement', 'type': None, 'title': 'direct-browser: https://en.wikipedia.org/wiki/Least_recently_used_cache_replacem'}
- {'url': 'https://zhuanlan.zhihu.com/p/596356832&rut=3314fb8829e320447f1dcef7b86fc32727b269232089be4a46ea39d04230d726', 'type': 'ddg', 'title': '热度评价模型实战复盘（2）---项目复盘 - 知乎'}

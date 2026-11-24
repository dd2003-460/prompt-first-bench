# N46: 峰值带宽需求 P_peak_bw (Mbps) 的计算公式：P_peak_bw = (日均下载量 * 峰值系数 * 8) / 86400，其中峰值系数通常取 3

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

峰值带宽需求 P_peak_bw (Mbps) 的计算公式：P_peak_bw = (日均下载量 * 峰值系数 * 8) / 86400，其中峰值系数通常取 3-5 倍，用于确定自建 POP 的出口带宽规格。

## Corrected Claim

峰值带宽需求通常需结合并发用户数、单用户峰值带宽及业务高峰时段占比进行估算，简单使用“日均下载量 * 峰值系数 / 86400”可能低估实际峰值需求，具体系数需根据业务流量模型确定。

## Evidence

[质询]该公式将“日均下载量”直接乘以“峰值系数”再除以总秒数，隐含假设了流量在时间上均匀分布或峰值系数仅作用于总量，忽略了实际网络流量中“并发用户数”和“突发流量”的非线性关系；通常峰值带宽计算需结合并发用户数、单用户带宽需求及峰值时段占比，而非简单的日均总量乘以系数。此外，来源中未提供该特定公式的直接支持。 | 逻辑上量纲正确（MB * 8 / s = Mbps），但参考来源[1][3]仅提及带宽需求需考虑高峰因素，未直接给出该具体公式及3-5倍系数的标准定义，属于经验事实且缺乏直接来源支持。

## Retrieval Sources

- {'url': 'https://docs.pingcode.com/insights/yyolm6d1enyq09m6itsrsqsx&rut=2625a839a5aa54d1c6aeb8cf187abbe2928d5733300f66570f9fcfcc74e48611', 'type': 'ddg', 'title': '带宽的需求是怎么计算的 - docs.pingcode.com'}
- {'url': 'https://developer.aliyun.com/article/230783&rut=da12dfa711844f34860291c44be3feafeaa7a1872d2ab5586950b02ce2ca5a43', 'type': 'ddg', 'title': '计算网络带宽支持的应用程序并发用户数-开发者社区-阿里云'}
- {'url': 'https://docs.pingcode.com/insights/u2jmhk37ul7a7n078k92el7e&rut=5950680a437c998aab2a0f533d7bcf8ea3328dae4bdee75f6e5ee62295aacae0', 'type': 'ddg', 'title': '怎么计算网络带宽需求 - docs.pingcode.com'}

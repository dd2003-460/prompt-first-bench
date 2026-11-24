# N46: 峰值带宽需求 P_peak_bw (Mbps) 的计算公式：P_peak_bw = (日均下载量 * 峰值系数 * 8) / 86400，其中峰值系数通常取 3

- **status**: pending
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

父节点级核验未通过：非正交（子节点之间存在逻辑矛盾和公式不一致。1. 父节点公式为直接乘法（日均*系数），未体现缓存命中率（H_miss）和协议开销（Overhead），而子节点3和4引入了这些变量，导致子节点推导出的峰值与父节点定义的简单公式不符。2. 子节点3中除以 N_pop 意味着计算的是单POP带宽，但父节点语境通常指总出口带宽或需明确 N_pop=1 的场景，存在歧义。3. 子节点4（回源带宽）是子节点3（单POP带宽）的子集或组成部分，二者在定义上存在包含关系而非完全正交，且未说明 POP 带宽与回源带宽的拓扑关系（如 POP 是否包含回源流量）。）

## Retrieval Sources

- {'url': 'https://docs.pingcode.com/insights/yyolm6d1enyq09m6itsrsqsx&rut=2625a839a5aa54d1c6aeb8cf187abbe2928d5733300f66570f9fcfcc74e48611', 'type': 'ddg', 'title': '带宽的需求是怎么计算的 - docs.pingcode.com'}
- {'url': 'https://developer.aliyun.com/article/230783&rut=da12dfa711844f34860291c44be3feafeaa7a1872d2ab5586950b02ce2ca5a43', 'type': 'ddg', 'title': '计算网络带宽支持的应用程序并发用户数-开发者社区-阿里云'}
- {'url': 'https://docs.pingcode.com/insights/u2jmhk37ul7a7n078k92el7e&rut=5950680a437c998aab2a0f533d7bcf8ea3328dae4bdee75f6e5ee62295aacae0', 'type': 'ddg', 'title': '怎么计算网络带宽需求 - docs.pingcode.com'}

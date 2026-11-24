# N30: 均对象大小 s 的黑盒参数化机制：s 定义为平均对象大小，单位 KB，需通过敏感性分析确定 s 的取值范围，典型值为 100KB–5MB（基于图片+短视频平台特

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

均对象大小 s 的黑盒参数化机制：s 定义为平均对象大小，单位 KB，需通过敏感性分析确定 s 的取值范围，典型值为 100KB–5MB（基于图片+短视频平台特征），s 对带宽成本的影响函数为 B(s) = s × RPS × 8 / 1000，其中 RPS 为每秒请求数，RPS = 日均下载 2TB / 86400s / s，s 越大，单请求带宽越高，但请求数越少，总带宽成本 B_total = s × RPS × 8 / 1000 × unit_cost_per_Mbps。

## Corrected Claim

均对象大小 s 的黑盒参数化机制：s 定义为平均对象大小，单位 KB，需通过敏感性分析确定 s 的取值范围，典型值为 100KB–5MB（基于图片+短视频平台特征），s 对带宽成本的影响函数为 B(s) = s × RPS × 8 / 1000，其中 RPS 为每秒请求数，RPS = 日均下载 2TB / 86400s / s，s 越大，单请求带宽越高，但请求数越少，总带宽成本 B_total = s × RPS × 8 / 1000 × unit_cost_per_Mbps。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 B(s) = s × RPS × 8 / 1000 量纲正确（KB * 1/s * 8 bits/KB / 1000 = Mbps），且 RPS 定义与总流量守恒一致，典型值范围符合工程直觉。

## Search Query

average object size image video platform bandwidth cost calculation RPS sensitivity analysis

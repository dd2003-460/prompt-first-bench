# N183: 工作点C（低命中率/低容量成本）：假设单POP缓存容量 S_pop=1TB，Hit_Rate目标为50%，则 U/R ≈ 0.5；此工作点下回源流量巨大，导致 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N52

## Claim

工作点C（低命中率/低容量成本）：假设单POP缓存容量 S_pop=1TB，Hit_Rate目标为50%，则 U/R ≈ 0.5；此工作点下回源流量巨大，导致 Bandwidth_Monthly 中回源部分激增，需验证是否触发公有云CDN的回源流量额外计费阈值（通常回源流量单价为下行流量的1.5-2倍）。

## Corrected Claim

工作点C（低命中率/低容量成本）：假设单POP缓存容量 S_pop=1TB，Hit_Rate目标为50%，则 U/R ≈ 0.5；此工作点下回源流量巨大，导致 Bandwidth_Monthly 中回源部分激增，需验证是否触发公有云CDN的回源流量额外计费阈值（通常回源流量单价高于下行流量，具体倍数需查阅对应云厂商最新价目表）。

## Evidence

[质询]该陈述包含具体的商业计费经验数据（回源流量单价为下行流量的1.5-2倍）及特定云厂商的计费阈值逻辑，属于经验事实，无法从第一性原理推导，且参考来源均未覆盖此领域。 | 参考来源[1][2][3]均为计算机组成原理中Cache命中率的理论计算，与公有云CDN计费策略无关，无可用外部证据支持具体倍数关系；但逻辑上低命中率导致高回源流量及成本增加符合经济直觉，故降级为定性表述。

## Search Query

CDN origin fetch traffic cost multiplier vs download traffic

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_29611239/article/details/162776267&rut=e1bdf12c70f33b24991e8bd602589ac18b12fe0e8478807b63a3cfc73e360d97', 'type': 'ddg', 'title': '计算机组成原理 Cache 命中率计算：3步实战解析与访存时间优化-CSDN博客'}
- {'url': 'https://ri-nai-bit-se.github.io/Computer-Organization-and-Architecture-Notes/%E7%AC%AC%E5%85%AD%E7%AB%A0/%E6%A0%B8%E5%BF%83%E4%BE%8B%E9%A2%98%E8%AF%A6%E8%A7%A3.html&rut=2862a1456f2c95bae1ac16fdb3919ca708e2c79afd87098c246f4b6222dba749', 'type': 'ddg', 'title': '第6章 存储系统设计 - 核心例题详解 | 计算机组成与体系结构笔记'}
- {'url': 'https://blog.csdn.net/weixin_43914272/article/details/108212718&rut=fee5b25b3412aa377145d7d46d79d0daae04a283b31cc1f1c5c82e8d9c484c80', 'type': 'ddg', 'title': '计算机组成原理——cache的命中率，平均访问时间，访问效率（含例题）_cache平均访问时间-CSDN博客'}

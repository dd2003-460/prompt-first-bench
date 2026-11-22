# N70: 稳态字节命中率 H_byte 的最终数值闭环：在 M/C = 1.0 (128GB / 128GB) 的极限条件下，LRU 缓存理论上覆盖所有对象。忽略更新失效

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

稳态字节命中率 H_byte 的最终数值闭环：在 M/C = 1.0 (128GB / 128GB) 的极限条件下，LRU 缓存理论上覆盖所有对象。忽略更新失效时，H_byte_static = 100%。考虑 1%/天 更新率及平均驻留时间 T_res ≈ 5天（基于 5000万请求/10万对象及热度分布估算），P_invalid ≈ 1 - exp(-0.01 * 5) ≈ 4.88%。因此，有效字节命中率 H_eff ≈ 100% * (1 - 0.0488) ≈ 95.12%。

## Corrected Claim

在假设平均驻留时间为5天且更新率为1%/天的特定条件下，有效字节命中率约为95.12%。

## Evidence

[质询]该陈述中的关键参数（如平均驻留时间 T_res ≈ 5天、更新率 1%/天）属于特定业务场景下的经验假设，并非通用物理或数学常数。若实际业务的热度分布或更新频率不同，计算结果将显著偏差。此外，参考来源均未提供这些具体业务参数，无法验证其合理性。 | 逻辑推导自洽（1 - exp(-0.05) ≈ 0.9512），但参考来源 [1][2][3] 均与 LRU 缓存命中率计算无关，属于经验事实且缺乏来源支持。

## Retrieval Sources

- {'url': 'https://www.gigabyte.com/SSD/GIGABYTE-NVMe-SSD-128GB/sp&rut=37060d6efc655a55c4f2297edb5ed282144d5836fddb52d8ccd1e4477fd7f9bb', 'type': 'ddg', 'title': 'GIGABYTE NVMe SSD 128GB Specifications - GIGABYTE Global'}
- {'url': 'https://blog.csdn.net/muyao987/article/details/140364179&rut=e94140e7656347d194b84b914a451a33d9262de6cf9a83f86c68600a16da2908', 'type': 'ddg', 'title': '大模型中 KV Cache 原理及显存占用分析 - CSDN博客'}
- {'url': 'https://www.amazon.com/128GB-exFAT32-Flash-Adapter-EASTBULL/dp/B0GVYXJY53&rut=fa826e5449c084acdd1859bd353bceea5023e605a334a936ab196c9b489d5e65', 'type': 'ddg', 'title': '128GB exFAT32 USB 3.0 Flash Drive with a USB-C Adapter ... - Amazon'}

# N59: A100 40GB SXM4 2024 Q4 市场价格约为 $10000-$12000，A100 80GB SXM4 为 $15000-$20000，H100 

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N9

## Claim

A100 40GB SXM4 2024 Q4 市场价格约为 $10000-$12000，A100 80GB SXM4 为 $15000-$20000，H100 80GB SXM5 为 $25000-$30000，L40S 48GB PCIe 为 $8000-$10000，A6000 48GB PCIe 为 $4000-$5000，来源：电商历史价格数据 [degraded]

## Corrected Claim

A100 40GB SXM4 2024 Q4 市场价格约为 $10000-$12000，A100 80GB SXM4 为 $15000-$20000，H100 80GB SXM5 为 $25000-$30000，L40S 48GB PCIe 为 $8000-$10000，A6000 48GB PCIe 为 $4000-$5000（注：参考来源主要提供2026年数据，2024 Q4具体数值缺乏直接来源支持，仅基于市场趋势间接推断）

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点之间存在严重的结构冗余，三个子节点本质上是同一类计算（TCO估算）在不同硬件型号上的实例化，应合并为一个包含多行数据的表格或单一节点；此外，父节点中明确列出的 A100 80GB 和 A6000 48GB 在子节点中完全缺失，导致信息覆盖不完整。）

## Search Query

A100 H100 L40S A6000 price 2024

## Retrieval Sources

- {'url': 'https://xueqiu.com/1290568231/376465368&rut=771a23b4f60f6688197c5a6a505b1f3c46143a599f9916a2b9fb2d542fd9c091', 'type': 'ddg', 'title': '截至2026年2月， 英伟达 A100单卡价格因显存（40GB/80GB）、接口（PCIe/SXM4）、渠道、是否含税及... - 雪球'}
- {'url': 'https://xueqiu.com/1290568231/376465314&rut=76d433dbab747916f3ac060386bb0ef119dcd392bdf7184268c0b7ad08dd6265', 'type': 'ddg', 'title': '截至2026年2月，8卡A100服务器的价格主要由GPU类型（40GB PCIe/80GB SXM4）、NVLink/N... - 雪球'}
- {'url': 'https://aliteq.com/a100-price&rut=662ef52a0bf195aa5825c554bf8cb2222a601cd62552686f411824a76f4b4692', 'type': 'ddg', 'title': 'A100 Price in November 2026, Used 40GB vs 80GB and Rent per Hour · Aliteq'}

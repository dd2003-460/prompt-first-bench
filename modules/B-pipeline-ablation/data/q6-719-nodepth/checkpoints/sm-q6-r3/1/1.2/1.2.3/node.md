# N45: 路由跳数影响：从用户到最近 POP 点的平均跳数 Hops 为 2-5 跳（基于 BGP 路由表），每跳增加抖动 1-5ms，总路由抖动贡献为 Hops × 3

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N7

## Claim

路由跳数影响：从用户到最近 POP 点的平均跳数 Hops 为 2-5 跳（基于 BGP 路由表），每跳增加抖动 1-5ms，总路由抖动贡献为 Hops × 3ms（取中值 3ms/跳）

## Corrected Claim

路由跳数影响：从用户到最近 POP 点的平均跳数通常在 2-5 跳之间（基于 BGP 路由表）。每跳引入的延迟通常在 1-5ms 左右，总路由延迟贡献约为 Hops × 3ms（取中值 3ms/跳）。抖动主要受链路拥塞和队列管理影响，不直接由跳数线性决定。

## Evidence

父节点级核验未通过：不完备（子节点存在逻辑矛盾且未覆盖父节点核心结论。1. 矛盾：父节点明确给出计算规则为 'Hops × 3ms'，但子节点2推导出的 T_hop 典型值为 1-4ms（中值约 2.5ms），与父节点的 3ms 基准不一致，导致最终抖动贡献计算无法统一。2. 不完备：父节点的核心输出是 '总路由抖动贡献'，但三个子节点分别只分解了跳数、单跳延迟和地理分布，缺少一个明确的 '总抖动计算节点' 来整合前两者并得出最终结果（例如：Total_Jitter = Hops_avg × T_hop_avg）。）

## Search Query

average BGP hops user to CDN edge node China network topology

## Retrieval Sources

- {'url': 'https://www.sohu.com/a/964885910_122004016&rut=7ddce687aa40cc6d30c27cfa67e59ec429a87a74db637ddbc1bbde2572b168f6', 'type': 'ddg', 'title': '第三方路由跳数对网络质量的深度影响分析_测试_数据包_路径'}

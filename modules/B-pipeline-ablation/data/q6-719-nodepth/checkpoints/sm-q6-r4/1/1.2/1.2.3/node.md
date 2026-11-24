# N45: 路由跳数影响：从用户到最近 POP 点的平均跳数 Hops 为 2-5 跳（基于 BGP 路由表），每跳增加抖动 1-5ms，总路由抖动贡献为 Hops × 3

- **status**: verified
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

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点公式中的两个核心变量（Hops 和 T_hop）以及影响 Hops 的具体场景分布，维度清晰且互斥。虽然父节点描述中提到的“抖动”与子节点计算的“延迟”术语不完全一致（通常抖动指方差，延迟指均值），但在工程估算模型中，将平均延迟贡献作为主要路径开销进行分解是合理的近似，且子节点内部逻辑自洽，未出现重复或矛盾。）

## Search Query

average BGP hops user to CDN edge node China network topology

## Retrieval Sources

- {'url': 'https://www.sohu.com/a/964885910_122004016&rut=7ddce687aa40cc6d30c27cfa67e59ec429a87a74db637ddbc1bbde2572b168f6', 'type': 'ddg', 'title': '第三方路由跳数对网络质量的深度影响分析_测试_数据包_路径'}

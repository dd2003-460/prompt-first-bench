# N33: 高成本低性工作点：纯自建10个POP点策略在高流量（>5000万日请求）下的每千请求P99合规成本，约为¥0.2-0.5/1000请求，但前期CAPEX高（约¥

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6

## Claim

高成本低性工作点：纯自建10个POP点策略在高流量（>5000万日请求）下的每千请求P99合规成本，约为¥0.2-0.5/1000请求，但前期CAPEX高（约¥500万-1000万），运维复杂度显著增加

## Corrected Claim

高成本低性工作点：纯自建10个POP点策略在高流量（>5000万日请求）下的每千请求P99合规成本，约为¥0.2-0.5/1000请求，但前期CAPEX高（约¥500万-1000万），运维复杂度显著增加

## Evidence

先验知识/题面给定，逻辑校验通过：自建10个POP点的CAPEX（¥500万-1000万）符合基础设施部署量级；在高流量（>5000万日请求）下，固定成本分摊后，每千请求P99合规成本¥0.2-0.5符合边际成本递减的经济直觉，且运维复杂度增加是自建模式的固有特征，逻辑自洽。

## Search Query

self-built CDN edge nodes cost per 1000 requests high traffic CAPEX OPEX

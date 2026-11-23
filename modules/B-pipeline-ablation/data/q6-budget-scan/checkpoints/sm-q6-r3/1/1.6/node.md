# N11: 回源链路延迟：t_origin = t_backbone + t_server，其中 t_backbone 为骨干网延迟（通常 20-50ms），t_serve

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

回源链路延迟：t_origin = t_backbone + t_server，其中 t_backbone 为骨干网延迟（通常 20-50ms），t_server 为源站处理延迟（图片/视频通常 < 10ms），回源概率 p_miss = 1 - hit_rate

## Corrected Claim

回源链路延迟：t_origin = t_backbone + t_server，其中 t_backbone 为骨干网延迟（通常 20-50ms），t_server 为源站处理延迟（图片/视频通常 < 10ms），回源概率 p_miss = 1 - hit_rate

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别对应父节点公式中的三个独立变量（t_backbone, t_server, p_miss），彼此无重叠且无矛盾；它们共同完整覆盖了父节点定义的所有关键组成部分；各子节点描述的是不同物理层面的延迟或概率参数，不存在同一参数的不同取值导致的冗余。）

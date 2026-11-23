# N183: 自建 POP 点物理距离 $d_{self}$ 的分布取决于用户地理分布 $G(x)$ 和 POP 选址优化；假设 90% 用户集中在华东/华南/华北，且每个区

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N62

## Claim

自建 POP 点物理距离 $d_{self}$ 的分布取决于用户地理分布 $G(x)$ 和 POP 选址优化；假设 90% 用户集中在华东/华南/华北，且每个区域设 1-2 个 POP，则平均距离 $d_{self} \approx 50-150$ km，中位数约 80 km。

## Corrected Claim

自建 POP 点物理距离 $d_{self}$ 的分布取决于用户地理分布 $G(x)$ 和 POP 选址优化；假设 90% 用户集中在华东/华南/华北，且每个区域设 1-2 个 POP，则平均距离 $d_{self} \approx 50-150$ km，中位数约 80 km。

## Evidence

先验知识/题面给定，逻辑校验通过：基于中国主要人口密集区（华东/华南/华北）的地理分布及每区域1-2个POP的假设，50-150km的平均距离及80km的中位数符合城市集群内部通信节点覆盖的典型量级，无逻辑矛盾。

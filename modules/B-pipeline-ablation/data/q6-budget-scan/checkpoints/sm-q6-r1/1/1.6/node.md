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

先验知识/题面给定，逻辑校验通过：回源延迟由骨干网传输延迟与源站处理延迟串联组成，符合网络通信基本逻辑；骨干网延迟20-50ms及源站处理延迟<10ms（针对静态资源）符合典型工程经验量级；回源概率定义为1-命中率符合概率论定义。

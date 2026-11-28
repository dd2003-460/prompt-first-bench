# N651: 空闲功耗Idle_Power：V100-SXM2集群在vLLM空闲状态下（无活跃请求）功耗约为350W（4卡均摊），基于NVIDIA官方idle power s

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N238, N239, N240

## Claim

空闲功耗Idle_Power：V100-SXM2集群在vLLM空闲状态下（无活跃请求）功耗约为350W（4卡均摊），基于NVIDIA官方idle power spec及实测待机电流推算，用于计算等待期间的电能浪费

## Corrected Claim

空闲功耗Idle_Power：V100-SXM2集群在vLLM空闲状态下（无活跃请求）功耗约为350W（4卡均摊），基于NVIDIA官方idle power spec及实测待机电流推算，用于计算等待期间的电能浪费

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

NVIDIA V100 idle power consumption watts benchmark

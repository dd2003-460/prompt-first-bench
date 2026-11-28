# N216: Docker 容器冷启动延迟分解：Docker Pull/Load 耗时 (t_pull) + gVisor runsc init 耗时 (t_init) + 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N63, N64, N65

## Claim

Docker 容器冷启动延迟分解：Docker Pull/Load 耗时 (t_pull) + gVisor runsc init 耗时 (t_init) + vLLM 客户端连接建立 (t_conn)；其中 t_init 在 M1 Max/Server Linux 环境下实测约为 150-200ms，是主要瓶颈，而非传统的 docker pull。

## Corrected Claim

Docker 容器冷启动延迟分解包括 Docker Pull/Load 耗时、gVisor runsc init 耗时及 vLLM 客户端连接建立耗时；其中 gVisor runsc init 通常是主要瓶颈之一，具体耗时取决于硬件环境和配置，需实测确定。

## Evidence

[质询]具体数值（150-200ms）及特定硬件环境（M1 Max/Server Linux）下的实测数据属于经验事实，参考来源仅提供了测试方法论描述，未提供具体的实测数值结果，无法验证该具体量级是否准确。 | 逻辑自洽，gVisor初始化确实是容器启动的主要开销之一；但参考来源[1]仅描述了runsc启动延迟的测量方法，未包含具体的150-200ms实测数据，属于经验事实且缺乏直接来源支持。

## Search Query

gVisor runsc startup latency benchmark milliseconds container cold start

## Retrieval Sources

- {'url': 'https://github.com/google/gvisor/issues/13182&rut=251c3576db9c57e4170709065eb89246dfd0a2923c33397480fcdafd52b0a227', 'type': 'ddg', 'title': 'What is the startup and stop latency of a runsc container on a ... - GitHub'}

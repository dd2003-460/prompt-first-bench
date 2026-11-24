# N696: H_self=0.95 场景下，T_proc_pop=10ms 对应的硬件性能指标：单台 POP 服务器需处理 10,000 QPS，且 CPU 利用率需低于 

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N231

## Claim

H_self=0.95 场景下，T_proc_pop=10ms 对应的硬件性能指标：单台 POP 服务器需处理 10,000 QPS，且 CPU 利用率需低于 50% 以保证 P99 处理时间 < 10ms，可选用 16 核 CPU 且内存带宽 > 30GB/s，相比 H_self=0.98 场景硬件成本降低 40%。

## Corrected Claim

H_self=0.95 场景下，由于自命中率较高，单台 POP 服务器处理 10,000 QPS 时的计算负载显著低于 H_self=0.98 场景，因此所需硬件规格（如 CPU 核心数、内存带宽）及整体硬件成本预计会有所降低，具体降幅取决于实际负载特征与选型。

## Evidence

[质询]具体硬件参数（16核、30GB/s带宽）与成本降低比例（40%）属于高度依赖具体业务负载特征、软件栈优化及市场价格的经验性工程估算，缺乏通用物理定律或第一性原理支持，且不同场景下波动极大，无法仅凭逻辑推导得出确切数值。 | source=knowledge，逻辑自洽（高自命中率降低计算负载从而降低硬件需求符合直觉），但具体数值（40%成本降低、特定CPU/内存规格）为经验事实，无来源直接支持，依据经验事实排除条款降级。

## Search Query

edge server QPS 10000 P99 processing time 10ms hardware cost reduction

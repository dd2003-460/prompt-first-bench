# N20: 多卡同步延迟：PCIe 环境下 all-reduce 操作延迟约为 50-200 μs（取决于消息大小和网络栈），NVLink 环境下约为 5-20 μs；对于

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4, N5

## Claim

多卡同步延迟：PCIe 环境下 all-reduce 操作延迟约为 50-200 μs（取决于消息大小和网络栈），NVLink 环境下约为 5-20 μs；对于 27B 模型，每层 TP 通信次数为 2（all-reduce），总延迟增加量 = 2 * layers * sync_latency，需量化对 TPS 的影响

## Corrected Claim

多卡同步延迟：PCIe 环境下 all-reduce 操作延迟通常在几十到几百微秒量级，NVLink 环境下显著更低（微秒级）；对于 27B 模型，每层 TP 通信次数为 2（all-reduce），总延迟增加量 = 2 * layers * sync_latency，需量化对 TPS 的影响

## Evidence

[质询]具体延迟数值（50-200 μs 和 5-20 μs）属于经验事实，受硬件代际、驱动版本、消息大小及具体拓扑影响极大，缺乏通用性；且参考来源仅提及原理，未提供具体数值支持。 | 逻辑自洽，但参考来源[1]仅涉及AllReduce原理与拓扑影响，未提供具体延迟数值，属于经验事实缺来源直接支持。

## Search Query

multi-GPU all-reduce latency PCIe vs NVLink microseconds

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2036554187035644932&rut=8df427f8a26fa6c80f186b98daa55c80659c84c7fa0fda3c1d0af6e553ed0d6d', 'type': 'ddg', 'title': '以vLLM Custom AllReduce 为基础，理解多卡通信与拓扑优化'}

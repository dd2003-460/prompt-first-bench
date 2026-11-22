# N248: Qwen3-27B 在 Q4_K_M 量化下的模型权重文件大小约为 15.5 GB（基于 27B 参数 * 4.5 bits/param / 8），这是 App

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N114

## Claim

Qwen3-27B 在 Q4_K_M 量化下的模型权重文件大小约为 15.5 GB（基于 27B 参数 * 4.5 bits/param / 8），这是 Apple Silicon 推理吞吐量的主要带宽消耗源，需从总内存带宽中扣除以计算有效 KV Cache 带宽。

## Corrected Claim

Qwen3-27B 在 Q4_K_M 量化下的模型权重文件大小约为 15.5 GB（基于 27B 参数 * 4.5 bits/param / 8），这是 Apple Silicon 推理吞吐量的主要带宽消耗源，需从总内存带宽中扣除以计算有效 KV Cache 带宽。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1聚焦于权重文件大小的计算与基准，子节点2聚焦于KV Cache在特定上下文下的内存占用计算。两者分别对应父节点中提到的两个核心内存消耗源（权重 vs KV Cache），内容互不重叠且无矛盾。父节点的核心逻辑是‘总带宽 - 权重开销 - KV Cache开销 = 有效带宽’，两个子节点完整覆盖了这一逻辑所需的两个关键变量计算，且KV Cache部分提供了不同量化下的取值以展示对带宽的影响，属于必要的参数展开而非冗余。）

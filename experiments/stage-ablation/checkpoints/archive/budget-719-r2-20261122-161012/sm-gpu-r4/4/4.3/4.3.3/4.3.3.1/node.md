# N218: 在 TP=2 双卡配置下，若采用 PCIe 4.0 连接，实测 Decode 延迟增加幅度约为 15-25%，主要归因于流水线同步等待和 PCIe 固定延迟，而

- **status**: verified
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N104

## Claim

在 TP=2 双卡配置下，若采用 PCIe 4.0 连接，实测 Decode 延迟增加幅度约为 15-25%，主要归因于流水线同步等待和 PCIe 固定延迟，而非数据传输时间。

## Corrected Claim

在 TP=2 双卡配置下，采用 PCIe 4.0 连接时，Decode 延迟会因流水线同步等待和 PCIe 固定延迟而增加，具体增幅需实测确定，通常显著高于单卡配置。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1聚焦于微观层面的延迟构成与计算公式（定量机制），子节点2聚焦于宏观层面的敏感性边界与优化条件（定性/范围机制）。两者在逻辑上互补且正交，共同完整解释了父节点中关于延迟增加幅度及其归因（同步等待vs传输）的结论，无冗余。）

## Search Query

Tensor Parallelism TP=2 PCIe latency overhead percentage benchmark vLLM

## Retrieval Sources

- {'url': 'https://rocm.blogs.amd.com/artificial-intelligence/tensor-parallelism/README.html&rut=35761cada621fdc086eabf4836206a5a95d38707687bbc1e9a7e0eb744c221d9', 'type': 'ddg', 'title': 'Analyzing the Impact of Tensor Parallelism Configurations on LLM ...'}
- {'url': 'https://github.com/vllm-project/vllm/issues/66873&rut=75892aa986f63710f617d060569c3145a74b80f0fd6f5ffaf5d3cb9b4c0e069a', 'type': 'ddg', 'title': '[RFC]: Replicate selected blocks across TP ranks for tensor parallelism ...'}

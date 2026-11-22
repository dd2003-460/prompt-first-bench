# N36: 多卡方案 (2x RTX 4090) 通过 Tensor Parallelism 运行 Qwen3-27B 时，由于 PCIe 4.0 x16 互联带宽 (约 

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

多卡方案 (2x RTX 4090) 通过 Tensor Parallelism 运行 Qwen3-27B 时，由于 PCIe 4.0 x16 互联带宽 (约 25-30 GB/s 有效双向) 远低于显存带宽，通信开销会导致吞吐量下降 15-25%。相比单卡 A100 (NVLink 或更高带宽互联，若为 PCIe 版本则同样受限但单卡带宽高)，2x4090 的总吞吐量通常低于单张 A100 或 H100。

## Corrected Claim

多卡方案 (2x RTX 4090) 通过 Tensor Parallelism 运行大模型时，由于 PCIe 4.0 x16 互联带宽远低于显存带宽，通信开销会导致吞吐量显著下降（具体比例视模型规模与实现而定，通常低于理想线性加速比）。相比单卡 A100 (NVLink 互联)，2x4090 的总吞吐量通常低于单张 A100 或 H100。

## Evidence

[质询]具体数值（15-25% 吞吐量下降）缺乏直接来源支持，且不同模型规模（如 27B vs 70B）及具体实现（vLLM vs 原生）下通信开销占比差异巨大，该数值可能过于精确或基于特定未披露场景。 | 来源 [3] 间接支持 PCIe 互联存在性能损耗（'PCIe coordination tax'）且无 NVLink 是限制因素，但未提供 15-25% 的具体数值；逻辑上 PCIe 带宽远低于显存带宽导致 TP 通信瓶颈符合物理直觉，但具体百分比属经验事实且缺直接数据支持。

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_33402252/article/details/169423201&rut=2c33a83f4b19524437926dfbf52ac6e91a644be08898c90d6d9ff0e68f69dfa7', 'type': 'ddg', 'title': 'Rtx 4090多卡配置实战：Ai训练与渲染优化指南 - Csdn博客'}
- {'url': 'https://blog.csdn.net/weixin_28949937/article/details/157282757&rut=cc1abb65081f1a3a6bbd1e7477909597e8752cb4e7437d087219e169b3874e64', 'type': 'ddg', 'title': 'ChatGLM3-6B多GPU部署教程：RTX 4090D双卡Tensor Parallel推理配置详解-CSDN博客'}
- {'url': 'https://gigagpu.com/rtx-4090-24gb-multi-card-pairing/&rut=b21936cb38d99d05f7c9aecccdda62d3088cc26d23ba4fd5af969ef8052bf19e', 'type': 'ddg', 'title': '2x RTX 4090 24GB Pairing for Tensor Parallel Inference'}

# N324: 2×RTX 3090 (48GB) 在 FP8 量化下运行 Qwen3-27B 的显存可行性：总显存 48GB > 29.6GB 需求，无需 Offload；但

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N118

## Claim

2×RTX 3090 (48GB) 在 FP8 量化下运行 Qwen3-27B 的显存可行性：总显存 48GB > 29.6GB 需求，无需 Offload；但 PCIe 4.0 互联下 Tensor Parallel 通信开销导致 Decode 阶段吞吐为单卡 4090 的 0.8-1.2 倍（12-18 tokens/s），Prefill 阶段因 All-Reduce 延迟增加 20-30%

## Corrected Claim

2×RTX 3090 (48GB) 在 FP8 量化下运行 Qwen3-27B 显存充足（总显存 48GB > 29.6GB 需求），无需 Offload；但在 PCIe 4.0 互联下，Tensor Parallel 通信开销会显著影响性能，Decode 阶段吞吐通常低于单卡高性能卡（如 4090）或接近其水平，Prefill 阶段因 All-Reduce 延迟会有明显增加。

## Evidence

[质询]数值量级与具体性能指标（如0.8-1.2倍、12-18 tokens/s、20-30%延迟）缺乏通用基准支持，且高度依赖具体硬件拓扑（NVLink vs PCIe）及软件栈优化，存在将特定实验结果泛化为普遍规律的风险。 | 先验知识/题面给定，逻辑校验通过：显存计算（27B模型FP8约13.5GB，双卡48GB充足）符合物理直觉；但具体吞吐倍数和延迟百分比属于经验性工程数据，虽逻辑自洽但缺乏通用基准直接支持，故降级为定性表述。

## Search Query

2x RTX 3090 tensor parallel FP8 27B model throughput PCIe bottleneck

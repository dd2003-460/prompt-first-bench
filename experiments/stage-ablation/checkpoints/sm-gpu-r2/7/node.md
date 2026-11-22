# N32: RTX 4090 (24GB) 在运行 Qwen3-27B FP8 量化模型时，受限于 1008 GB/s 显存带宽，理论最大解码吞吐量约为 15-20 tok

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

RTX 4090 (24GB) 在运行 Qwen3-27B FP8 量化模型时，受限于 1008 GB/s 显存带宽，理论最大解码吞吐量约为 15-20 tokens/s（基于 memory-bound 公式：Bandwidth / Model_Size_GB）；实测数据通常在 12-18 tokens/s 之间。

## Corrected Claim

RTX 4090 (24GB) 在运行 Qwen3-27B 时，若使用 FP8 量化，由于模型大小（~27GB）超过显存容量，需依赖 CPU 内存卸载或混合精度，实际解码吞吐量受限于系统内存带宽及 PCIe 传输，通常低于纯显存带宽理论值，实测数据需根据具体卸载策略而定，一般在 5-15 tokens/s 区间波动。

## Evidence

[质询]数值量级与具体参数存在偏差：RTX 4090 标准版显存带宽为 1008 GB/s，但 24GB 显存下 Qwen3-27B FP8 模型权重约 27GB，无法完整装入显存（需 Offload 或更低量化），导致实际吞吐量远低于纯显存带宽理论值；且来源中提及的是 Qwen3.8-27B 及 Q4 量化，与 claim 中的 FP8 及具体吞吐量数值（15-20 tokens/s）不完全匹配，FP8 在 24GB 卡上通常需混合精度或卸载，实测速度往往低于此范围或波动较大。 | 来源 [1] 和 [2] 确认了 RTX 4090/4090D 24GB 可运行 Qwen3.8-27B，但主要讨论 Q4 量化及部署流程，未直接提供 FP8 量化下的 15-20 tokens/s 实测数据；逻辑上 memory-bound 公式成立，但 24GB 显存无法容纳 27GB FP8 模型，实际性能受 CPU 内存带宽或混合精度影响，故降级为定性表述。

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2083555506732512359&rut=8fa78de888ac263b600c3c76a2f605da5d22c3a9ac7bbded9dfaedc0352e1d96', 'type': 'ddg', 'title': '24GB 显存榨干指南：RTX 4090D 部署 Qwen3.8-27B 全流程实测'}
- {'url': 'https://zhuanlan.zhihu.com/p/2078119870546309718&rut=7cadd6d87a11f21fe138f941b709013b122cbb0e1daeb776d481f59244fe664e', 'type': 'ddg', 'title': 'RTX 4090 24GB 能跑 Qwen3.8-27B 吗？该选什么量化和云GPU？'}

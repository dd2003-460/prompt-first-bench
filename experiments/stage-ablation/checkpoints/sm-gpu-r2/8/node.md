# N33: NVIDIA A100 80GB (PCIe) 显存带宽为 2039 GB/s，是 RTX 4090 的 2 倍以上。在运行 Qwen3-27B BF16 模型

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

NVIDIA A100 80GB (PCIe) 显存带宽为 2039 GB/s，是 RTX 4090 的 2 倍以上。在运行 Qwen3-27B BF16 模型时，其解码吞吐量可达 35-45 tokens/s，显著高于消费级显卡，主要得益于 HBM2e 的高带宽优势。

## Corrected Claim

NVIDIA A100 80GB (PCIe) 显存带宽约为 2039 GB/s，是 RTX 4090 的 2 倍以上。其高带宽优势（HBM2e）通常能显著提升大模型推理性能，但具体吞吐量取决于模型架构、批处理大小及软件优化，需参考具体基准测试数据。

## Evidence

[质询]陈述中关于 Qwen3-27B BF16 模型在 A100 上的具体解码吞吐量（35-45 tokens/s）属于特定负载下的经验性能数据，参考来源仅提供了硬件规格（带宽、TDP等），未包含任何针对该特定模型的性能基准测试数据，无法通过现有来源直接验证该数值。 | 来源 [2] 直接支持 A100 80GB 显存带宽超过 2 TB/s（即 2000+ GB/s），与陈述中的 2039 GB/s 量级一致且逻辑自洽；但关于 Qwen3-27B 的具体吞吐量数据在提供的来源中无直接证据支持，属于经验事实且缺乏来源覆盖。

## Retrieval Sources

- {'url': 'https://www.nvidia.com/content/dam/en-zz/Solutions/Data-Center/a100/pdf/PB-10577-001_v02.pdf&rut=0c79d1c9a2457fa92d8fad8b85044ecd8fd9efe3f99e573de43ea37673feb07d', 'type': 'ddg', 'title': 'PDF NVIDIA A100 80GB PCIe GPU'}
- {'url': 'https://www.nvidia.com/zh-tw/data-center/a100/&rut=cadd54030a56742894de95d233e144763b3e87d84289ab945f0cc8602100a19e', 'type': 'ddg', 'title': 'Nvidia A100 | Nvidia'}
- {'url': 'https://www.techpowerup.com/gpu-specs/a100-pcie-80-gb.c3821&rut=4ca038206139fdc4444db73ec486f4b96e6db7852b445f860714759ea7568b5c', 'type': 'ddg', 'title': 'NVIDIA A100 PCIe 80 GB Specs | TechPowerUp GPU Database'}

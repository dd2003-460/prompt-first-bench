# N502: RTX 4090 在 Qwen3-27B INT8 量化下的实测吞吐量需通过 vLLM 或 llama.cpp 基准测试获取，具体数值受上下文长度（32K）、批

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N159

## Claim

RTX 4090 在 Qwen3-27B INT8 量化下的实测吞吐量需通过 vLLM 或 llama.cpp 基准测试获取，具体数值受上下文长度（32K）、批处理大小（batch_size）、量化方法（GPTQ/AWQ）影响，典型值在 15-25 tokens/s 范围内，需引用具体测试报告或社区基准数据 [待核验]

## Corrected Claim

RTX 4090 (24GB) 无法直接容纳 Qwen3-27B INT8 量化模型（约 27GB），需使用 CPU offload 或更大显存显卡。若使用 offload，吞吐量将显著低于纯 GPU 推理，具体数值需根据 offload 比例和 PCIe 带宽实测，通常远低于 15-25 tokens/s 或需特定配置验证。

## Evidence

[质询]数值量级存疑：RTX 4090 拥有 24GB 显存和极高的显存带宽（1008 GB/s），Qwen3-27B INT8 量化后模型大小约为 27GB，理论上无法完整装入单张 4090 显存（除非使用 offload 或极低精度，但题目指定 INT8）。若强行运行，受限于 PCIe 带宽或 CPU 内存交换，吞吐量远低于 15-25 tokens/s 是可能的，但若假设能运行（如通过 vLLM 的 CPU offload 或假设模型更小/显存更大），15-25 tokens/s 对于 27B 模型在单卡 4090 上的推理速度而言，通常偏低（通常 7B-13B 模型在 4090 上可达 50-100+ tokens/s，27B 若能跑，速度取决于瓶颈，但 15-25 这个区间缺乏具体测试支撑，且前提条件（27B INT8 在 24GB 卡上）存在硬件兼容性矛盾）。 | 经验事实，逻辑自洽但缺来源支持；且存在硬件显存容量与模型大小的潜在矛盾（27B INT8 ≈ 27GB > 24GB VRAM），导致该陈述的前提条件在标准单卡配置下不成立或需特殊配置，数值缺乏依据。

## Search Query

RTX 4090 Qwen3-27B INT8 tokens per second benchmark vLLM llama.cpp

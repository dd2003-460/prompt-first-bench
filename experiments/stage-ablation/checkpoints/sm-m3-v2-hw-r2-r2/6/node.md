# N28: 4×V100-SXM2-16GB 集群在 HBM2 带宽限制下，Qwen3-27B NVFP4 量化模型的实际推理吞吐量上限约为 40-60 tokens/s 

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

4×V100-SXM2-16GB 集群在 HBM2 带宽限制下，Qwen3-27B NVFP4 量化模型的实际推理吞吐量上限约为 40-60 tokens/s (aggregate across 4 cards)，受限于 PCIe 3.0/4.0 传输瓶颈及 CPU-GPU 数据交换延迟，无法支持超过 2 个并发长序列生成而不显著增加延迟。

## Corrected Claim

4×V100-SXM2-16GB 集群在运行 Qwen3-27B NVFP4 量化模型时，受限于 HBM2 带宽及可能的互联瓶颈，其实际推理吞吐量可能在数十 tokens/s 量级（具体数值取决于软件优化与并发策略），高并发长序列生成可能会显著增加延迟。

## Evidence

[质询]该陈述包含具体的经验性能指标（40-60 tokens/s）和并发限制（2个长序列），这些数值高度依赖于具体的软件栈（如vLLM/TensorRT-LLM版本）、批处理策略、序列长度及硬件拓扑（NVLink vs PCIe），并非由硬件规格唯一确定的物理常数。此外，V100 SXM2通常配备NVLink，若集群配置正确，瓶颈可能不在PCIe而在计算或HBM带宽，具体吞吐量需实测验证，现有来源未提供此特定量化模型在该配置下的确切基准测试数据。 | 来源[1]提及V100 SXM2运行14B模型速度超50 tokens/s，与27B模型在4卡集群下达到40-60 tokens/s的量级在逻辑上兼容（模型更大但卡数更多），但缺乏针对Qwen3-27B NVFP4在4xV100集群上的直接基准测试支持，属于经验事实且仅有间接量级参考。

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1910043824199303266&rut=f987a0d9f0a84c0a1ecf2f576e87cb1f1b31b4e6034cb616d8eb895a2228e9f4', 'type': 'ddg', 'title': 'SXM2版V100显卡很麻烦但很香：14B大模型速度超50!附折腾攻略'}
- {'url': 'https://github.com/andrewleech/v100-llm-kit&rut=ad91f7c6bbeedf6a1f9afebecc27e12f4c8031013db29d8467d0eb0962def34c', 'type': 'ddg', 'title': 'GitHub - andrewleech/v100-llm-kit: Run local LLMs on a Tesla V100-SXM2 ...'}
- {'url': 'https://www.techpowerup.com/gpu-specs/tesla-v100-sxm2-16-gb.c3018&rut=a896ed92d17887b4fcfae818bac84fd70439f69b07e1e880d61be206ee34ce98', 'type': 'ddg', 'title': 'NVIDIA Tesla V100 SXM2 16 GB Specs - TechPowerUp'}

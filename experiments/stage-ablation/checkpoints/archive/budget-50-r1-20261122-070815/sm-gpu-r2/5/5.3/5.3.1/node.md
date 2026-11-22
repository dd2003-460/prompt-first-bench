# N125: vLLM 官方基准测试报告中使用的 CUDA 版本 (如 12.1 vs 12.4) 和驱动版本对 RTX 4090 和 A100 推理吞吐量 (tokens/

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N29

## Claim

vLLM 官方基准测试报告中使用的 CUDA 版本 (如 12.1 vs 12.4) 和驱动版本对 RTX 4090 和 A100 推理吞吐量 (tokens/s) 的具体影响百分比，需查找 vLLM GitHub 仓库的 release notes 或性能对比图表，以确定当前环境 (CUDA 12.4+) 与基准数据之间的修正系数。

## Corrected Claim

vLLM 的推理吞吐量受 CUDA 版本和驱动版本影响，但具体影响百分比需查阅 vLLM 官方特定版本的基准测试报告或进行本地实测，当前参考来源未提供相关量化数据。

## Evidence

[质询]该陈述试图量化特定软件版本（vLLM）与硬件驱动/CUDA版本组合下的性能差异百分比，属于高度依赖具体实验环境的经验事实。参考来源仅涉及CUDA计算能力定义和安装报错，完全未包含任何吞吐量基准数据或性能对比图表，无法支持具体的‘影响百分比’或‘修正系数’。 | 经验事实，逻辑自洽但缺来源支持（来源[1]为通用文档，来源[2]为安装问题，均无性能数据）

## Search Query

vLLM CUDA version impact on RTX 4090 A100 inference throughput performance difference percentage

## Retrieval Sources

- {'url': 'https://developer.nvidia.com/cuda/gpus&rut=783b1ee48db2af9b423d58fdb5ff1f57cb147f68f2af6434f05859ada92672e4', 'type': 'ddg', 'title': 'CUDA GPU Compute Capability | NVIDIA Developer'}
- {'url': 'https://github.com/vllm-project/vllm/issues/15531&rut=c67340660abcaf4793df4d116205fb6b4d2fcf091faf63b4c1eeb2995cbeabc6', 'type': 'ddg', 'title': '[Installation]: install vllm with CUDA 12.8 in 5090D error'}

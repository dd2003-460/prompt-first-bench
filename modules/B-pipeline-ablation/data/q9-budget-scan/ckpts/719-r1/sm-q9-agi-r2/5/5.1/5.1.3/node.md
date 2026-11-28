# N68: 工作点A在 max-model-len=262144 和 max-num-seqs=8 配置下，Qwen3.8-27B NVFP4 的实际吞吐量（tokens/

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N19, N20, N21

## Claim

工作点A在 max-model-len=262144 和 max-num-seqs=8 配置下，Qwen3.8-27B NVFP4 的实际吞吐量（tokens/sec）受限于 AllReduce 通信开销，需通过 vLLM benchmark 工具实测，预估在 4x V100 上约为 50-100 tokens/sec（单请求），并发8路时总吞吐约为 150-300 tokens/sec

## Corrected Claim

工作点A在 max-model-len=262144 和 max-num-seqs=8 配置下，Qwen3.8-27B NVFP4 的实际吞吐量需通过 vLLM benchmark 工具实测。由于 V100 不支持 FP4 格式，该配置在 4x V100 上无法运行；若使用支持 FP4 的硬件（如 H100），吞吐量预估需重新评估。

## Evidence

[质询]V100 GPU 不支持 FP4 数据格式（NVFP4 需要 Hopper 架构如 H100/H200 或 Blackwell 架构支持），在 V100 上运行 Qwen3.8-27B NVFP4 模型在硬件层面不可行，因此基于 V100 的吞吐量预估缺乏物理基础。 | 经验事实，逻辑不自洽（V100 不支持 FP4），且无可用外部证据支持。

## Search Query

vLLM benchmark throughput 4x V100 TP4 27B model long context

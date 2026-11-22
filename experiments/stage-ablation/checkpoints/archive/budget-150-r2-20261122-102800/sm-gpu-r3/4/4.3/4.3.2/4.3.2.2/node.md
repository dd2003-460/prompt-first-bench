# N277: RX 7900 XTX 在 ROCm 6.1.2 下运行 Qwen3-27B BF16 推理时，由于缺乏原生 BF16 硬件加速，实际吞吐量约为 FP16 路径

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N105

## Claim

RX 7900 XTX 在 ROCm 6.1.2 下运行 Qwen3-27B BF16 推理时，由于缺乏原生 BF16 硬件加速，实际吞吐量约为 FP16 路径的 45%-55%，对应有效算力为 27.3-33.3 TFLOPS

## Corrected Claim

RX 7900 XTX 在 ROCm 6.1.2 下运行 Qwen3-27B BF16 推理时，受软件栈优化程度影响，实际吞吐量可能低于 FP16 路径，具体性能需实测验证。

## Evidence

[质询]RX 7900 XTX (RDNA 3) 架构原生支持 BF16 格式，称其“缺乏原生 BF16 硬件加速”在硬件架构层面存在事实性错误；此外，45%-55% 的吞吐量比例及 27.3-33.3 TFLOPS 的具体数值属于特定软件栈（ROCm 6.1.2）下的经验性能数据，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持；且“缺乏原生 BF16 硬件加速”的表述与 RDNA 3 架构特性存在潜在矛盾，需降级为定性表述。

## Search Query

RX 7900 XTX ROCm 6.1.2 Qwen3-27B BF16 inference throughput FP16 comparison

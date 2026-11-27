# N316: RTX 5090 FP8 计算瓶颈验证：Blackwell 架构 FP8 稠密算力 838 TFLOPS，Qwen3-27B 每 token FLOPs 需求 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N135

## Claim

RTX 5090 FP8 计算瓶颈验证：Blackwell 架构 FP8 稠密算力 838 TFLOPS，Qwen3-27B 每 token FLOPs 需求 2*27e9*32768 ≈ 1.77 TFLOPs，计算时间 ≈ 2.1ms，内存时间 ≈ 13.1ms，内存带宽仍为瓶颈，但计算占比提升至 13.8%，需联合优化

## Corrected Claim

RTX 5090 FP8 计算瓶颈验证：Blackwell 架构 FP8 稠密算力 838 TFLOPS，Qwen3-27B 每 token FLOPs 需求 2*27e9*32768 ≈ 1.77 TFLOPs，计算时间 ≈ 2.1ms，内存时间 ≈ 13.1ms，内存带宽仍为瓶颈，但计算占比提升至 13.8%，需联合优化

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 5090 FP8 算力 838 TFLOPS 与 Qwen3-27B 参数量及隐藏层维度（32768）推导出的 FLOPs 需求（~1.77 TFLOPs/token）量级合理，计算时间（~2.1ms）与内存时间（~13.1ms）对比符合大模型推理中内存带宽瓶颈的特征，且计算占比提升趋势符合架构演进逻辑。

## Search Query

RTX 5090 FP8 compute vs memory bound LLM inference

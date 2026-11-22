# N47: RTX 4090 (Ada Lovelace) 架构不支持原生 FP8 硬件指令集，使用 FP8 权重需通过 TensorRT-LLM 或 vLLM 进行软件模

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N10

## Claim

RTX 4090 (Ada Lovelace) 架构不支持原生 FP8 硬件指令集，使用 FP8 权重需通过 TensorRT-LLM 或 vLLM 进行软件模拟 (dequantize to FP32/BF16 for compute)，导致 Decode 吞吐量相比原生 FP8 硬件 (H100) 下降约 40-50% [待核验：具体框架版本下的实测吞吐对比]。

## Corrected Claim

RTX 4090 (Ada Lovelace) 架构的 Tensor Core 不支持 Hopper 架构原生的 FP8 矩阵乘法硬件加速指令，使用 FP8 权重通常需通过软件库（如 TensorRT-LLM）进行支持，其 Decode 吞吐量相比 H100 原生 FP8 硬件存在显著差距（具体幅度依工作负载而定，通常估计在 30-50% 区间）。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点逻辑清晰且正交：节点1纠正了父节点关于硬件架构支持性的核心事实错误（Fact Correction）；节点2基于正确架构分析了实际性能瓶颈与吞吐表现（Performance Analysis）；节点3针对父节点中假设成立的极端情况进行了条件性分析（Conditional Counter-factual）。三者分别覆盖了‘硬件事实’、‘实际性能’和‘错误前提下的理论推导’，无重复且共同构成了对父节点错误结论的全面解构与修正，完备性良好。）

## Search Query

RTX 4090 FP8 inference performance penalty TensorRT-LLM

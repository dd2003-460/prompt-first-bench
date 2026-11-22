# N768: 工作点 3 (低带宽利用率)：在 TensorRT-LLM 框架下，RTX 4090 运行 Qwen3-27B BF16 且 Batch Size=8 时，由于

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N272, N273, N274

## Claim

工作点 3 (低带宽利用率)：在 TensorRT-LLM 框架下，RTX 4090 运行 Qwen3-27B BF16 且 Batch Size=8 时，由于并发 KV Cache 读写冲突及 PCIe 传输瓶颈，实测有效内存带宽利用率 η_mem ≈ 0.55，此时系统进入内存带宽受限区，吞吐量线性增长失效。

## Corrected Claim

在 TensorRT-LLM 框架下，RTX 4090 运行 Qwen3-27B BF16 且 Batch Size=8 时，受并发 KV Cache 读写冲突及 PCIe 传输瓶颈影响，系统可能进入内存带宽受限区，导致吞吐量线性增长失效，有效内存带宽利用率显著低于理论峰值（具体数值需实测确定）。

## Evidence

[质询]该陈述包含具体的实测数值（η_mem ≈ 0.55）和特定的硬件/软件配置（RTX 4090, TensorRT-LLM, Qwen3-27B, BS=8），属于经验事实。在缺乏任何参考来源支持的情况下，无法验证该具体数值的准确性，且不同实现细节（如KV Cache量化、具体算子优化）可能导致利用率显著波动，存在将特定实验结果泛化为固定参数的风险。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）。

## Search Query

TensorRT-LLM RTX 4090 Qwen3-27B BF16 batch size 8 memory bandwidth bottleneck

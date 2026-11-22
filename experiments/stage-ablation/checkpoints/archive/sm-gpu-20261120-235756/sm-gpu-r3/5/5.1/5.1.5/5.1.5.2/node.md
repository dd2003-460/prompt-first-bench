# N287: RTX 4090 上 Qwen3-27B FP8 的 vLLM 基线吞吐实测值：Tokens/s = 1 / TPOT，其中 TPOT 受限于内存带宽 (100

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N103

## Claim

RTX 4090 上 Qwen3-27B FP8 的 vLLM 基线吞吐实测值：Tokens/s = 1 / TPOT，其中 TPOT 受限于内存带宽 (1008 GB/s) 和 MoE 路由开销，理论上限约 300-400 Tokens/s，实际 vLLM 基准测试数据需在 2024 Q4 后的 LLM 推理基准中查找，若缺失则标记 [待核验]。

## Corrected Claim

RTX 4090 上 Qwen3-27B FP8 的 vLLM 基线吞吐实测值：Tokens/s = 1 / TPOT。受限于内存带宽 (1008 GB/s) 和 MoE 路由开销，在典型 Batch Size 下理论上限估计在数百 Tokens/s 量级，具体数值需依据实际基准测试数据确定，当前标记为 [待核验]。

## Evidence

[质询]该陈述包含具体的硬件规格（RTX 4090 内存带宽 1008 GB/s）和特定模型（Qwen3-27B）在特定软件栈（vLLM）下的性能预测，属于经验事实。虽然 1008 GB/s 是 RTX 4090 的标称带宽，但 '300-400 Tokens/s' 的理论上限依赖于具体的 Batch Size、序列长度、KV Cache 大小以及 MoE 路由的具体实现效率，这些变量未定义，导致该数值范围缺乏严谨的推导基础，且 Qwen3-27B 的具体 MoE 架构细节（如专家数量、激活比例）未明确，使得基于带宽的简单估算可能产生较大偏差。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该数值为依赖具体配置的经验性估算，非第一性原理可严格推导的恒定值）

## Search Query

vLLM Qwen3-27B FP8 RTX 4090 tokens per second benchmark 2024

# N421: Qwen3-27B 在 RTX 4090 上通过 vLLM FP8 模拟（或 Marlin kernel）运行的实测吞吐量（tokens/s），需确认所用内核是

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N146

## Claim

Qwen3-27B 在 RTX 4090 上通过 vLLM FP8 模拟（或 Marlin kernel）运行的实测吞吐量（tokens/s），需确认所用内核是否针对 Qwen3 混合注意力架构进行了优化，否则性能可能因回退到通用 GEMM 而显著下降。

## Corrected Claim

Qwen3-27B 在 RTX 4090 上通过 vLLM FP8 或 Marlin kernel 运行的性能取决于内核是否针对其混合注意力架构进行了优化；若未优化，可能因回退到通用 GEMM 导致性能下降，但具体吞吐量需实测确认。

## Evidence

[质询]该陈述包含具体的硬件（RTX 4090）、软件栈（vLLM FP8/Marlin）及模型（Qwen3-27B）的性能预期，属于经验事实。由于缺乏实测数据支持，无法确认具体吞吐量数值或内核优化状态，且‘显著下降’的程度缺乏量化依据。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）。

## Search Query

Qwen3-27B RTX 4090 FP8 emulation vLLM Marlin kernel throughput

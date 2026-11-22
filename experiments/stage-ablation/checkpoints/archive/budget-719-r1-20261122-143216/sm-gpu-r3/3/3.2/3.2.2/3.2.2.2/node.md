# N236: 在启用 vLLM PagedAttention 和 FlashAttention-2 的最优软件栈配置下，RTX 5090 的内存带宽利用率可提升至 0.8-0

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N83

## Claim

在启用 vLLM PagedAttention 和 FlashAttention-2 的最优软件栈配置下，RTX 5090 的内存带宽利用率可提升至 0.8-0.85，使 FP8 实际吞吐量达到 50-53 tokens/s，此工作点代表通过算子融合消除非权重读取开销后的理论峰值逼近值。

## Corrected Claim

在启用 vLLM PagedAttention 和 FlashAttention-2 的最优软件栈配置下，RTX 5090 的内存带宽利用率可显著提升，使 FP8 实际吞吐量达到较高水平，此工作点代表通过算子融合消除非权重读取开销后的理论峰值逼近值。

## Evidence

[质询]数值量级与具体参数缺乏来源支持：RTX 5090 的 FP8 吞吐量具体数值（50-53 tokens/s）及内存带宽利用率（0.8-0.85）属于经验事实，且不同模型规模、序列长度下差异巨大，无法仅凭逻辑推导得出精确区间。 | 经验事实，逻辑自洽但缺来源支持

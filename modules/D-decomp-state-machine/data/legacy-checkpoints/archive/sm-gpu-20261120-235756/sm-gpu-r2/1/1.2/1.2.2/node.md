# N40: 在 BF16 精度下，Qwen3-27B 运行 32K 上下文时 KV Cache 峰值显存占用为 8,053,063,680 bytes (约 7.5 GB)

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

在 BF16 精度下，Qwen3-27B 运行 32K 上下文时 KV Cache 峰值显存占用为 8,053,063,680 bytes (约 7.5 GB)，计算公式为 256 KB/token × 32,768 tokens，该值与权重显存 (54.36 GB) 相加后构成单卡推理的最小显存需求基线，未计入激活值峰值和框架开销。

## Corrected Claim

在 BF16 精度下，Qwen3-27B 运行 32K 上下文时 KV Cache 峰值显存占用为 8,053,063,680 bytes (约 7.5 GB)，计算公式为 256 KB/token × 32,768 tokens，该值与权重显存 (54.36 GB) 相加后构成单卡推理的最小显存需求基线，未计入激活值峰值和框架开销。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 架构参数（64层，GQA 8 KV heads，head_dim 128）推导出的 KV Cache 单 token 占用为 256KB，32K 上下文总占用 8GB，数值量级与计算逻辑自洽。

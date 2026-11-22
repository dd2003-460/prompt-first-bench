# N189: A100 80GB 在 27B INT8 推理下的 TPS 约为 80-100 tokens/s (基于 2039 GB/s HBM2e 带宽)，相比 RTX 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N57

## Claim

A100 80GB 在 27B INT8 推理下的 TPS 约为 80-100 tokens/s (基于 2039 GB/s HBM2e 带宽)，相比 RTX 5090 (60-70 TPS) 高 20-40%；其 Cost_Per_Token = ($9500 + $525) / (8760h * 8h/day * 90 TPS) ≈ $0.0015/token，需与 RTX 5090 的 Cost_Per_Token 对比以确定 TCO 优势边界。

## Corrected Claim

A100 80GB 在 27B INT8 推理下的 TPS 约为 20-40 tokens/s (基于 2039 GB/s HBM2e 带宽)，相比 RTX 5090 (60-70 TPS) 可能更低或持平（取决于具体实现和 batch size）；其 Cost_Per_Token 计算需修正分母为实际运行小时数（如 8760h/年 或 720h/月），而非 8760h * 8h/day。

## Evidence

[质询]Cost_Per_Token 计算公式存在严重的逻辑与量纲错误：分母中 '8760h * 8h/day' 将年小时数与日工作小时数相乘，导致量纲变为 h²，且数值巨大（约 70,080），这不符合 TCO 计算逻辑（通常应为 年总小时数 或 月总小时数）。此外，A100 80GB 在 27B INT8 下的 TPS 80-100 也显著高于实际硬件极限（受限于 HBM 带宽和计算单元，通常远低于此值，除非是极小 batch 且仅看单流延迟，但即便单流，27B 模型在 A100 上通常也在 20-40 TPS 左右，80-100 TPS 过于乐观）。 | 经验事实，逻辑自洽但缺来源支持；且 Cost_Per_Token 公式存在量纲错误（h * h），TPS 数值量级存疑。

## Search Query

NVIDIA A100 Qwen 27B INT8 inference tokens per second benchmark

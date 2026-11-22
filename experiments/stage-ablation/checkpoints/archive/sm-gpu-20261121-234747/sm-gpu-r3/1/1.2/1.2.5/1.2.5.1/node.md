# N186: NVIDIA A100 40GB 在运行 Qwen3-27B INT8 时的显存溢出风险验证：权重 27GB + 32K 上下文 KV Cache (BF16)

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N41

## Claim

NVIDIA A100 40GB 在运行 Qwen3-27B INT8 时的显存溢出风险验证：权重 27GB + 32K 上下文 KV Cache (BF16) 约 16GB + 激活值约 3GB，总计约 46GB > 40GB，导致必须使用 FP8 KV Cache 或降低上下文长度至 16K，或启用 CPU Offloading，量化 Offloading 对 Decode 延迟的影响系数（通常增加 2-5 倍延迟）。

## Corrected Claim

NVIDIA A100 40GB 在运行 Qwen3-27B INT8 时存在显存溢出风险：权重约 27GB + 32K 上下文 KV Cache (BF16) 约 13-16GB + 激活值约 3GB，总计约 43-46GB > 40GB。需使用 FP8 KV Cache、降低上下文长度或启用 CPU Offloading。CPU Offloading 通常会导致 Decode 延迟显著增加（具体倍数取决于硬件带宽与实现，通常为 2-5 倍或更高）。

## Evidence

[质询]KV Cache 数值估算存在量级偏差：Qwen3-27B 若采用 GQA（如 8 KV heads, head_dim 128），32K 上下文 BF16 KV Cache 理论值约为 12.8GB，而非 16GB；此外，'量化 Offloading 对 Decode 延迟增加 2-5 倍' 属于高度依赖具体实现（如 PCIe 带宽、Offload 策略）的经验数据，缺乏通用性，且 46GB 的总显存需求未包含 CUDA Context 等基础开销，实际溢出风险更高，但具体数值需根据实际配置验证。 | 先验知识/题面给定，逻辑校验通过：显存溢出结论（46GB > 40GB）在量级上成立，但 KV Cache 具体数值（16GB）与典型 GQA 架构理论值（~12.8GB）存在偏差，且延迟倍数属于经验性估计，缺乏精确来源支持，故降级为定性表述。

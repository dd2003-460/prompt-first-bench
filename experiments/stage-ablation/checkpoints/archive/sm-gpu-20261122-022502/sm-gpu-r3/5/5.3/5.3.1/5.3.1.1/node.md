# N240: W4A8 量化在 Qwen3-27B 上的显存占用精确计算：权重 = 27B * 0.5 bytes (W4) = 13.5GB; KV Cache (BF16

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N78

## Claim

W4A8 量化在 Qwen3-27B 上的显存占用精确计算：权重 = 27B * 0.5 bytes (W4) = 13.5GB; KV Cache (BF16, 32K ctx) = 32768 * 2 (K+V) * 32 (heads) * 128 (dim) * 2 bytes / 1e9 ≈ 5.37GB (若无 GQA) 或 1.34GB (若 GQA 4:1); 激活值缓冲 ≈ 2GB; 总显存 ≈ 13.5 + 5.37 + 2 = 20.87GB (无 GQA) 或 16.84GB (有 GQA)，均在 24GB 显存范围内，无需 Offload。

## Corrected Claim

W4A8 量化在 Qwen3-27B 上的显存占用估算：权重约 13.5GB；KV Cache 取决于具体 GQA 配置（若为 32 heads/128 dim 则约 5.37GB，若 GQA 4:1 则约 1.34GB）；激活值缓冲随 batch size 和序列长度动态变化（32K ctx 下可能显著高于 2GB）。总显存需根据实际部署参数（batch size, GQA ratio）精确计算，粗略估算可能在 16-25GB 之间，是否需 Offload 取决于具体配置。

## Evidence

[质询]KV Cache 计算中假设 Qwen3-27B 拥有 32 个注意力头（heads）和 128 维头维度（dim），这与 Qwen 系列模型（包括 Qwen2/3 的 27B 级别）通常采用的 GQA（Grouped Query Attention）架构及具体超参数（如 Qwen2-72B 为 64 heads, head_dim 128; Qwen2-7B 为 28 heads, head_dim 128）可能存在偏差。若实际 head 数量或 head_dim 不同，KV Cache 数值将显著变化。此外，'激活值缓冲 ≈ 2GB' 是一个高度依赖 batch size 和序列长度的经验估算值，并非固定常数，在长上下文（32K）下可能远超 2GB 或远低于此值，导致总显存估算不准确。 | 先验知识/题面给定，逻辑校验通过。虽然算术逻辑自洽（13.5+5.37+2=20.87），但 KV Cache 的具体参数（heads/dim）和激活值估算缺乏针对 Qwen3-27B 的确切来源支持，且激活值估算过于简化，属于经验事实且存在参数不确定性，故降级。

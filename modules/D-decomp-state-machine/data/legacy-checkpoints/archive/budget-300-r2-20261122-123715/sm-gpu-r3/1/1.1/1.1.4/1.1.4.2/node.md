# N130: Qwen3-27B 在 32K 上下文长度下，GQA 配置 (KV_heads=4, head_dim=256, layers=64) 的 KV Cache 显

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N31

## Claim

Qwen3-27B 在 32K 上下文长度下，GQA 配置 (KV_heads=4, head_dim=256, layers=64) 的 KV Cache 显存占用在 BF16 精度下为 2 * 64 * 4 * 256 * 32768 * 2 bytes / 1024^3 ≈ 16.0 GB；若 KV Cache 也量化至 INT8 则为 8.0 GB，需明确 N31 中 4.5GB 数值的计算依据或修正

## Corrected Claim

Qwen3-27B 在 32K 上下文长度下，GQA 配置 (KV_heads=4, head_dim=256, layers=64) 的 KV Cache 显存占用在 BF16 精度下为 2 * 64 * 4 * 256 * 32768 * 2 bytes / 1024^3 ≈ 8.0 GB；若 KV Cache 也量化至 INT8 则为 4.0 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 显存计算公式为 2 (K/V) * layers * kv_heads * head_dim * seq_len * bytes_per_element。代入数值：2 * 64 * 4 * 256 * 32768 * 2 bytes = 8,589,934,592 bytes。转换为 GB (1024^3)：8,589,934,592 / 1,073,741,824 = 8.0 GB。等等，这里发现计算错误。让我重新计算：
2 * 64 * 4 * 256 * 32768 * 2 = 8,589,934,592 bytes。
8,589,934,592 / 1024 / 1024 / 1024 = 8.0 GB。
原陈述称 BF16 下为 16.0 GB，INT8 下为 8.0 GB。这与计算结果不符。BF16 是 2 bytes，INT8 是 1 byte。
如果 BF16 是 8.0 GB，那么 INT8 应该是 4.0 GB。
原陈述说 BF16 是 16.0 GB，这意味着它可能误用了 4 bytes (FP32) 或者计算错误。
让我们再检查一遍公式：
KV Cache size = 2 * L * H_kv * D_head * S * B
L=64, H_kv=4, D_head=256, S=32768, B=2 (BF16)
Size = 2 * 64 * 4 * 256 * 32768 * 2 = 8,589,934,592 bytes = 8 GB.
原陈述声称 BF16 为 16.0 GB，这是错误的（应该是 8.0 GB）。
原陈述声称 INT8 为 8.0 GB，这也是错误的（应该是 4.0 GB）。
因此，该陈述存在硬逻辑/计算错误。

## Search Query

Qwen3-27B GQA KV cache size calculation 32k context BF16

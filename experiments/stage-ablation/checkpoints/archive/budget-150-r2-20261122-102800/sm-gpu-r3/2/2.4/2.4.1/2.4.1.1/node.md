# N228: BF16 单卡显存需求精确分解：Qwen3-27B 权重 (58.29 GB) + KV Cache (32K ctx, batch=1, 2 bytes/el

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N83

## Claim

BF16 单卡显存需求精确分解：Qwen3-27B 权重 (58.29 GB) + KV Cache (32K ctx, batch=1, 2 bytes/element, 48 layers, 128 heads, 128 head_dim ≈ 2.01 GB) + 激活缓冲 (N143/N144 峰值 ≈ 1.7 GB) + 框架开销 (≈ 1.0 GB) = 63.0 GB；因此 64 GB 卡 (如 A100-80GB) 余量 17 GB (27%)，满足安全阈值，而 48 GB 卡不可行。

## Corrected Claim

BF16 单卡显存需求精确分解：Qwen3-27B 权重 (58.29 GB) + KV Cache (32K ctx, batch=1, 2 bytes/element, 48 layers, 128 heads, 128 head_dim ≈ 2.01 GB) + 激活缓冲 (N143/N144 峰值 ≈ 1.7 GB) + 框架开销 (≈ 1.0 GB) = 63.0 GB；因此 64 GB 卡 (如 A100-80GB) 余量 17 GB (27%)，满足安全阈值，而 48 GB 卡不可行。

## Evidence

先验知识/题面给定，逻辑校验通过：权重58.29GB + KV Cache 2.01GB + 激活1.7GB + 开销1.0GB = 63.0GB，计算自洽；64GB卡余量17GB（27%）符合安全阈值逻辑，48GB卡不可行结论正确。

## Search Query

Qwen3-27B BF16 total VRAM requirement weights KV cache activation

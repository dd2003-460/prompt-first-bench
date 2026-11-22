# N312: RTX 4090 单卡 32K 上下文下，batch_size=1 时的激活值峰值为 0.54GB (4096 * 32768 * 2 * 2 / 1e9)，C

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N110, N111, N112

## Claim

RTX 4090 单卡 32K 上下文下，batch_size=1 时的激活值峰值为 0.54GB (4096 * 32768 * 2 * 2 / 1e9)，CUDA Context 开销为 0.8GB，框架缓冲区为 0.5GB，总余量需求 1.84GB < 4.21GB 可用余量，无 OOM 风险。

## Corrected Claim

RTX 4090 单卡 32K 上下文下，batch_size=1 时的激活值峰值为 0.54GB (4096 * 32768 * 2 * 2 / 1e9)，CUDA Context 开销为 0.8GB，框架缓冲区为 0.5GB，总余量需求 1.84GB < 4.21GB 可用余量，无 OOM 风险。

## Evidence

先验知识/题面给定，逻辑校验通过：激活值计算 4096*32768*2*2/1e9 ≈ 0.54GB 正确，总需求 1.84GB 小于可用余量 4.21GB，无 OOM 风险结论成立。

## Search Query

RTX 4090 activation memory batch size 1 32k context

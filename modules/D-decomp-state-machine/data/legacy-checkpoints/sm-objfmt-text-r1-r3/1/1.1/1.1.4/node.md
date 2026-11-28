# N28: 在 32K 上下文长度下，Qwen3-27B 单请求 KV Cache 的理论峰值显存占用计算结果为 64 * 8 * 128 * 32768 * 2 byte

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N7, N8, N9

## Claim

在 32K 上下文长度下，Qwen3-27B 单请求 KV Cache 的理论峰值显存占用计算结果为 64 * 8 * 128 * 32768 * 2 bytes * 2 (K&V) = 8.59 GB

## Corrected Claim

在 32K 上下文长度下，Qwen3-27B 单请求 KV Cache 的理论峰值显存占用计算结果为 64 * 8 * 128 * 32768 * 2 bytes * 2 (K&V) = 8.59 GB

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点1主要功能是纠错（指出父节点数值错误并给出正确值17.18GB），子节点2则直接陈述了该正确值（17.18GB）及其他精度下的数值。两者在‘BF16下KV Cache占用17.18GB’这一核心事实上高度重叠，导致信息冗余。此外，子节点1侧重于‘为什么父节点错了’，子节点2侧重于‘不同精度下的具体值’，虽然角度略有不同，但核心数据点重复。）

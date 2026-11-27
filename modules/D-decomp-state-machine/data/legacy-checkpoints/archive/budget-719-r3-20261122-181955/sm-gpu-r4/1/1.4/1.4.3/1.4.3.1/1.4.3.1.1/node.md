# N556: Qwen3-27B 官方技术报告确认采用 GQA 架构，具体参数为 num_layers=64, n_kv_heads=8, n_heads=32, head_

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N194

## Claim

Qwen3-27B 官方技术报告确认采用 GQA 架构，具体参数为 num_layers=64, n_kv_heads=8, n_heads=32, head_dim=128；此参数组合下，BF16 单 token KV Cache 大小 = 2 * 64 * 8 * 128 * 2 bytes = 256 KB。

## Corrected Claim

Qwen3-27B 采用 GQA 架构。若其参数为 num_layers=64, n_kv_heads=8, n_heads=32, head_dim=128，则 BF16 单 token KV Cache 大小为 256 KB。（注：具体参数值需以官方技术报告为准，当前缺乏直接来源确认）

## Evidence

[质询]该陈述包含具体的模型架构参数（如 n_kv_heads=8, n_heads=32 等），属于经验事实。虽然 Qwen3-27B 确实存在且通常采用 GQA，但具体的头数配置（例如是否为 8 个 KV 头而非 4 或 16 个）需要官方技术报告或配置文件的直接证据支持。当前检索无可用来源，无法确认这些具体数值是否准确，存在参数记忆偏差的风险。 | 经验事实，逻辑自洽但缺来源支持。数学计算部分（2 * 64 * 8 * 128 * 2 = 256 KB）正确，但架构参数本身缺乏外部证据验证。

## Search Query

Qwen3-27B technical report architecture parameters n_kv_heads num_layers head_dim

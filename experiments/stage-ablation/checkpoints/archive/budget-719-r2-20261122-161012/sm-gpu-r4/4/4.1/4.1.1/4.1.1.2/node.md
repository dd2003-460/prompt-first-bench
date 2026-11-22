# N197: KV Cache 单 token 大小计算公式修正验证：2 (K/V) * num_layers(64) * num_kv_heads(8) * head_di

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N97

## Claim

KV Cache 单 token 大小计算公式修正验证：2 (K/V) * num_layers(64) * num_kv_heads(8) * head_dim(128) * bytes_per_element(2 for BF16) = 262,144 bytes = 256 KB/token，该计算排除了 N20 中错误的 1.2MB 假设（可能误用了 full attention 而非 GQA），确认 GQA 机制将 KV 内存需求降低至 MHA 的 1/8

## Corrected Claim

KV Cache 单 token 大小计算公式修正验证：2 (K/V) * num_layers(64) * num_kv_heads(8) * head_dim(128) * bytes_per_element(2 for BF16) = 262,144 bytes = 256 KB/token，该计算排除了 N20 中错误的 1.2MB 假设（可能误用了 full attention 而非 GQA），确认 GQA 机制将 KV 内存需求降低至 MHA 的 1/8

## Evidence

父节点级核验未通过：非正交, 不完备（1. 正交性违背：父节点明确给出计算结果为 256 KB/token 并确认该值正确（排除1.2MB错误），但子节点1声称 256 KB 是“计算错误”，正确值应为 128 KB，两者存在直接事实矛盾。2. 完备性缺失：父节点的核心论点是“确认 GQA 机制将 KV 内存需求降低至 MHA 的 1/8”，但子节点仅关注数值计算和量化影响，完全未覆盖 GQA 与 MHA 对比这一关键机制验证。3. 逻辑连贯性：子节点2基于子节点1的“128KB”进行推导，虽然内部一致，但整体与父节点语境冲突。）

# N489: 并发连接数上限 C_max 的硬件限制：C_max = min(ulimit_nproc, fd_limit, memory_per_conn * RAM_to

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N157

## Claim

并发连接数上限 C_max 的硬件限制：C_max = min(ulimit_nproc, fd_limit, memory_per_conn * RAM_total / conn_size)；典型 Nginx 配置 fd_limit = 65535，但受限于内存（每连接 ~1KB），若 RAM = 64GB，C_max ≈ 64000；实际有效 C_max 需通过压测确定，通常设为 fd_limit 的 80% 即 52428。

## Corrected Claim

并发连接数上限 C_max 的硬件限制：C_max = min(ulimit_nproc, fd_limit, RAM_total / memory_per_conn)；典型 Nginx 配置 fd_limit = 65535，若 RAM = 64GB 且每连接内存占用 ~1KB，则内存理论上限为 64M，远高于 fd_limit，因此实际 C_max 主要由 fd_limit 决定，通常设为 fd_limit 的 80% 即 52428。

## Evidence

[质询]公式逻辑错误：C_max 不应受限于 'memory_per_conn * RAM_total / conn_size'，该表达式量纲和逻辑均不合理（内存限制应为 RAM_total / memory_per_conn，而非乘以内存再除以连接大小）；且 64GB 内存下每连接 1KB 的理论上限为 64M，远高于 fd_limit 65535，因此内存并非瓶颈，实际 C_max 主要由 fd_limit 决定，而非内存计算值。 | 先验知识/题面给定，逻辑校验未通过：公式中内存限制项量纲错误，且数值推导与 fd_limit 瓶颈矛盾

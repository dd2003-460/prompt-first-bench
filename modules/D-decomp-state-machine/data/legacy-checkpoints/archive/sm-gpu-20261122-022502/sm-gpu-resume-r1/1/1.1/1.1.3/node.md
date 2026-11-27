# N39: INT4 (AWQ/GPTQ) 量化中 3GB 额外开销的构成：包括 128 个 group 的 scale/zero-point 参数（27B params 

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7, N8, N9

## Claim

INT4 (AWQ/GPTQ) 量化中 3GB 额外开销的构成：包括 128 个 group 的 scale/zero-point 参数（27B params / 128 * 2 bytes * 2 ≈ 0.84GB）以及量化校准所需的静态查找表或临时缓冲（约 2.16GB），导致总占用从理论 13.5GB 升至 16.5GB（若按 3GB 固定开销计）或需根据具体量化粒度重新计算。

## Corrected Claim

INT4 (AWQ/GPTQ) 量化中 3GB 额外开销的构成：包括 128 个 group 的 scale/zero-point 参数（27B params / 128 * 2 bytes * 2 ≈ 0.84GB）以及量化校准所需的静态查找表或临时缓冲（约 2.16GB），导致总占用从理论 13.5GB 升至 16.5GB（若按 3GB 固定开销计）或需根据具体量化粒度重新计算。

## Evidence

父节点级核验未通过：不完备（子节点之间正交，分别讨论了不同 group_size 下的参数开销和运行时缓冲开销。但存在不完备性：父节点明确指出 3GB 开销由 '0.84GB (scale/zero)' 和 '2.16GB (静态查找表/临时缓冲)' 组成。子节点 1 覆盖了 0.84GB 部分，子节点 3 仅覆盖了 0.5-1.0GB 的临时缓冲，剩余约 1.16GB 的 '静态查找表' 或 '校准临时缓冲' 未被任何子节点明确解释或覆盖，导致无法完全重构父节点的 3GB 总额。此外，子节点 2 引入了 group_size=64 的情况，虽与正交性无冲突，但属于扩展信息，若父节点仅关注 3GB 开销的构成（通常基于默认或特定配置），该子节点可能略微偏离核心分解目标，但不构成严重冗余。）

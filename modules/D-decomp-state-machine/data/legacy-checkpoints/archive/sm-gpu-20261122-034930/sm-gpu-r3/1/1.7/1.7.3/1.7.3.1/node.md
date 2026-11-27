# N202: macOS 对 GPU 可用内存的限制由 `default_wired_limit_mb` 和 `metal_max_alloc` 参数控制。默认情况下，GPU

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N66

## Claim

macOS 对 GPU 可用内存的限制由 `default_wired_limit_mb` 和 `metal_max_alloc` 参数控制。默认情况下，GPU 可访问内存上限为系统总内存的 65%。对于 192GB M2 Ultra，GPU 可用内存约为 124.8GB。若需运行 BF16 Qwen3-27B (需 ~68.7GB)，在物理上可行，但需通过 `sudo sysctl iogpu.wired_limit_mb=196608` 或调整 Metal 配置来解除限制，否则可能触发 OOM。

## Corrected Claim

macOS 对 GPU 可用内存存在限制，通常与系统总内存比例相关（常见说法约为 65% 或 2/3）。对于 192GB M2 Ultra，若限制为 65%，则 GPU 可用内存约为 124.8GB，足以容纳 ~68.7GB 的模型。但具体的解除限制方法（如 sysctl 参数或 Metal 配置）需查阅最新 macOS 技术文档确认，因为内核参数可能随版本变化。

## Evidence

[质询]该陈述包含具体的系统参数名称（`default_wired_limit_mb`, `metal_max_alloc`）、特定的百分比阈值（65%）以及具体的 sysctl 命令路径（`iogpu.wired_limit_mb`）。这些属于 macOS 内部实现细节和经验性硬件/软件配置参数，并非第一性原理可推导的数学或物理事实。由于检索失败，无法验证这些参数名称是否准确、65% 是否为当前 macOS 版本的默认硬限制，以及该 sysctl 键值是否真实存在且有效。 | 经验事实，逻辑自洽但缺来源支持。数值计算（192GB * 65% = 124.8GB）正确，且 124.8GB > 68.7GB 的物理可行性推断在逻辑上成立，但具体的系统限制机制和参数名称无法通过现有证据验证。

## Search Query

macOS Metal GPU memory limit 192GB M2 Ultra sysctl iogpu.wired_limit

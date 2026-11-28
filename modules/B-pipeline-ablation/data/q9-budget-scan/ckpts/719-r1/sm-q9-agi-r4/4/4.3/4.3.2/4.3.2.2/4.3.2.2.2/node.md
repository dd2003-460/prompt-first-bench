# N632: 双向同步（读+写）总耗时 T_bidir = 2 * T_transfer + T_sync_overhead；若 T_transfer=87ms，且同步开销 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N225

## Claim

双向同步（读+写）总耗时 T_bidir = 2 * T_transfer + T_sync_overhead；若 T_transfer=87ms，且同步开销 T_sync_overhead（含 PCIe 事务层处理）约为 5ms，则 T_bidir ≈ 179ms；比原估 160ms 高 11.875%，需验证是否在关键路径上，若为异步操作则可部分隐藏，但若为阻塞式同步则显著增加延迟。

## Corrected Claim

双向同步（读+写）总耗时 T_bidir = 2 * T_transfer + T_sync_overhead；若 T_transfer=87ms，且同步开销 T_sync_overhead（含 PCIe 事务层处理）约为 5ms，则 T_bidir ≈ 179ms；比原估 160ms 高 11.875%，需验证是否在关键路径上，若为异步操作则可部分隐藏，但若为阻塞式同步则显著增加延迟。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（2*87+5=179，(179-160)/160≈11.875%），公式结构符合双向同步的基本逻辑模型。

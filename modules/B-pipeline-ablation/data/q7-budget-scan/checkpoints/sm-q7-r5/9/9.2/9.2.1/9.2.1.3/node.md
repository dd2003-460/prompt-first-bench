# N673: N63 定义的 60% Spin-down 占比是基于理想冷数据模型，实际生产环境中因监控探针、日志扫描等后台任务，真实 Spin-down 占比通常在 45%

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N278, N279, N280

## Claim

N63 定义的 60% Spin-down 占比是基于理想冷数据模型，实际生产环境中因监控探针、日志扫描等后台任务，真实 Spin-down 占比通常在 45%-55% 之间，这会导致 W_HDD_avg 从 3.025W 上升至约 3.4-3.6W，进而使 HDD 层年化电力成本增加 15-20%。

## Corrected Claim

N63 定义的 60% Spin-down 占比是基于理想冷数据模型，实际生产环境中因监控探针、日志扫描等后台任务，真实 Spin-down 占比通常在 45%-55% 之间，这会导致 W_HDD_avg 从 3.025W 上升至约 3.4-3.6W，进而使 HDD 层年化电力成本增加 15-20%。

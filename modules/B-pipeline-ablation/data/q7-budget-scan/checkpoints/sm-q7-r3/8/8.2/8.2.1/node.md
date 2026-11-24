# N265: NVMe SSD 空闲功耗 W_idle 修正：7.68TB 企业级 NVMe SSD 在无 I/O 且 DRAM 缓存未刷新时的典型待机功耗为 1.0-1.5

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N128

## Claim

NVMe SSD 空闲功耗 W_idle 修正：7.68TB 企业级 NVMe SSD 在无 I/O 且 DRAM 缓存未刷新时的典型待机功耗为 1.0-1.5W，而非 2.5W（N128 原估偏高，因混淆了部分休眠与完全待机状态）

## Corrected Claim

NVMe SSD 空闲功耗 W_idle 修正：7.68TB 企业级 NVMe SSD 在无 I/O 且 DRAM 缓存未刷新时的典型待机功耗为 1.0-1.5W，而非 2.5W（N128 原估偏高，因混淆了部分休眠与完全待机状态）

## Evidence

先验知识/题面给定，逻辑校验通过：7.68TB企业级NVMe SSD在完全待机（Idle）状态下功耗通常为1.0-1.5W，2.5W通常对应Active Idle或包含DRAM刷新的状态，原估2.5W确实偏高，修正符合行业典型规格。

## Search Query

enterprise nvme ssd 7.68tb idle power consumption watts spec sheet

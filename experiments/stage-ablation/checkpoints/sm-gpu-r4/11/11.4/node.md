# N303: 非典型方案（如 Apple Silicon）的排除/纳入判据：若任务对延迟敏感 (TTFT < 2s)，则 Apple Silicon 因 TTFT 较高 (约

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N120

## Claim

非典型方案（如 Apple Silicon）的排除/纳入判据：若任务对延迟敏感 (TTFT < 2s)，则 Apple Silicon 因 TTFT 较高 (约 5-10s) 而被排除；若任务对吞吐量不敏感 (如离线批处理)，则 Apple Silicon 因低 TCO 而被纳入。

## Corrected Claim

非典型方案（如 Apple Silicon）的排除/纳入判据：若任务对延迟敏感 (TTFT < 2s)，则 Apple Silicon 因 TTFT 较高 (约 5-10s) 而被排除；若任务对吞吐量不敏感 (如离线批处理)，则 Apple Silicon 因低 TCO 而被纳入。

## Evidence

先验知识/题面给定，逻辑校验通过

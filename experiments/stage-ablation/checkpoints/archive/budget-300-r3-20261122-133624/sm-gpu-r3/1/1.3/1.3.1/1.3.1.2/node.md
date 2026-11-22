# N193: RTX 5090 上由于 Blackwell 架构驱动更新，CUDA Context 基础开销预计与 Ada Lovelace 持平或略高，约为 0.9-1.3

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N49

## Claim

RTX 5090 上由于 Blackwell 架构驱动更新，CUDA Context 基础开销预计与 Ada Lovelace 持平或略高，约为 0.9-1.3GB，需通过实际部署 nvidia-smi 监控确认，暂按 1.0GB 保守估算。

## Corrected Claim

RTX 5090 上 CUDA Context 基础开销预计与 Ada Lovelace 架构相当，具体数值需通过实际部署 nvidia-smi 监控确认，暂按 1.0GB 保守估算。

## Evidence

[质询]该陈述包含具体的经验性数值范围（0.9-1.3GB）和特定架构（Blackwell/RTX 5090）的性能对比结论，属于经验事实。由于缺乏外部来源支持，无法验证该具体数值范围是否准确，且‘持平或略高’的定性判断缺乏数据支撑。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）。

## Search Query

RTX 5090 vLLM base memory usage nvidia-smi

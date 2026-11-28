# N452: GVisor 与原生 Linux 在内核态系统调用（如 open, close）上的性能差异倍率：基准测试显示 GVisor 的 syscall 路径比原生 L

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N154

## Claim

GVisor 与原生 Linux 在内核态系统调用（如 open, close）上的性能差异倍率：基准测试显示 GVisor 的 syscall 路径比原生 Linux 慢 3-5 倍（由于 Go 语言实现的用户态内核额外转换层），但绝对延迟仍在微秒级（<20μs），对总耗时 <2.5s 的结论影响可忽略

## Corrected Claim

GVisor 与原生 Linux 在内核态系统调用上的性能存在显著差异，通常慢数倍，但绝对延迟仍在微秒级，对总耗时影响较小

## Evidence

[质询]具体数值（3-5倍、<20μs）属于经验事实，缺乏来源支持，且不同负载下差异可能波动较大 | 经验事实，逻辑自洽但缺来源支持

## Search Query

GVisor vs native linux syscall performance benchmark ratio

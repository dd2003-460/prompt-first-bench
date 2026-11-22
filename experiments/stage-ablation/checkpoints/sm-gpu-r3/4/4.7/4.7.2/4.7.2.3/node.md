# N255: RTX 4090 显存带宽 1008 GB/s 下，读取 1.0 GB KV Cache 的时间为 1.0 GB / 1008 GB/s ≈ 0.99 ms。由

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N115

## Claim

RTX 4090 显存带宽 1008 GB/s 下，读取 1.0 GB KV Cache 的时间为 1.0 GB / 1008 GB/s ≈ 0.99 ms。由于 GPU 显存访问延迟远低于统一内存（因专用 HBM/GDDR 控制器），实际有效延迟接近理论值，无需额外修正系数。

## Corrected Claim

RTX 4090 显存带宽 1008 GB/s 下，读取 1.0 GB KV Cache 的理论带宽限制时间为 1.0 GB / 1008 GB/s ≈ 0.99 ms。由于 GPU 显存访问延迟远低于统一内存，实际有效延迟通常略高于此理论值（受控制器调度及内核开销影响），但在宏观估算中可近似视为接近理论值。

## Evidence

[质询]陈述中关于“实际有效延迟接近理论值，无需额外修正系数”的断言过于绝对。在真实GPU架构中，显存带宽（Bandwidth）与延迟（Latency）是两个不同的指标。虽然HBM/GDDR的延迟远低于统一内存，但读取1.0GB数据时，受限于内存控制器调度、TLB miss、以及GPU内核启动开销（kernel launch overhead）等因素，实际耗时通常会高于纯带宽计算的理论下限（即存在修正系数，实际时间 > 理论时间）。此外，RTX 4090使用的是GDDR6X而非HBM，虽然带宽高，但“无需额外修正系数”这一工程简化在严谨的性能建模中是不成立的。 | source=knowledge，逻辑校验通过（1.0/1008≈0.00099s=0.99ms计算正确），但“无需额外修正系数”属于经验性工程假设，缺乏绝对严谨性，故降级。

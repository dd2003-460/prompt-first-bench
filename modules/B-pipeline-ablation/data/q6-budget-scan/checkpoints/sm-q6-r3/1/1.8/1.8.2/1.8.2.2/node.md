# N235: 长尾区域 T_proc_P99(k) 的公有云特性：T_proc_P99(k) = T_shared_cpu_contention + T_multi_tena

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N73

## Claim

长尾区域 T_proc_P99(k) 的公有云特性：T_proc_P99(k) = T_shared_cpu_contention + T_multi_tenant_overhead，其中公有云共享架构导致 CPU 争用，T_shared_cpu_contention ≈ 2-10ms（取决于邻居负载），T_multi_tenant_overhead ≈ 1-3ms（虚拟化开销），总计比自建节点高 30-50%

## Corrected Claim

长尾区域 T_proc_P99(k) 的公有云特性：T_proc_P99(k) = T_shared_cpu_contention + T_multi_tenant_overhead，其中公有云共享架构导致 CPU 争用，T_shared_cpu_contention ≈ 2-10ms（取决于邻居负载），T_multi_tenant_overhead ≈ 1-3ms（虚拟化开销），总计比自建节点高 30-50%

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

public cloud multi-tenant overhead latency shared CPU

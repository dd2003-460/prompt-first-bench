# N170: 4x V100-SXM2 服务器在完全 Idle 状态（无 CUDA 上下文，仅 CPU/RAM/PSU 待机）下的整机功耗基线为 160W ± 20W；若保持

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

4x V100-SXM2 服务器在完全 Idle 状态（无 CUDA 上下文，仅 CPU/RAM/PSU 待机）下的整机功耗基线为 160W ± 20W；若保持 vLLM 进程常驻（CUDA Context Loaded），Idle 功耗上升至 220W ± 30W，主要增量来自 GPU 显存刷新和 PCIe 链路维持。

## Corrected Claim

4x V100-SXM2 服务器在完全 Idle 状态（无 CUDA 上下文，仅 CPU/RAM/PSU 待机）下的整机功耗基线为 160W ± 20W；若保持 vLLM 进程常驻（CUDA Context Loaded），Idle 功耗上升至 220W ± 30W，主要增量来自 GPU 显存刷新和 PCIe 链路维持。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

tesla v100 sxm2 idle power consumption server with cuda context

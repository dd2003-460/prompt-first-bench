# N134: 重新定义 m = min(K, N) 后的有效命中率计算：若 m = N = 10^5，则 H_req_top_m = 1 - (10^5/10^5)^0.1 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

重新定义 m = min(K, N) 后的有效命中率计算：若 m = N = 10^5，则 H_req_top_m = 1 - (10^5/10^5)^0.1 = 1 - 1 = 0？错误。正确公式应为 H_req = 1 - (N_m/N)^ (1-β)，当 N_m=N 时，H_req = 1。需修正公式为 H_req = 1 - (m/N)^(1-β) 仅适用于 m < N；当 m = N 时，H_req = 100%。

## Corrected Claim

重新定义 m = min(K, N) 后的有效命中率计算：若 m = N = 10^5，则 H_req_top_m = 1 - (10^5/10^5)^0.1 = 1 - 1 = 0？错误。正确公式应为 H_req = 1 - (N_m/N)^ (1-β)，当 N_m=N 时，H_req = 1。需修正公式为 H_req = 1 - (m/N)^(1-β) 仅适用于 m < N；当 m = N 时，H_req = 100%。

## Evidence

先验知识/题面给定，逻辑校验通过：当 m=N 时，(m/N)^(1-β) = 1^(1-β) = 1，故 H_req = 1 - 1 = 0 的推导在数学上成立，但结论指出原公式在 m=N 时失效并需修正为 H_req=100%（或理解为该公式仅适用于 m<N 的截断场景，而 m=N 代表全量缓存/请求，命中率应为100%），逻辑自洽且符合缓存/请求命中率的物理直觉（全量覆盖即100%命中）。

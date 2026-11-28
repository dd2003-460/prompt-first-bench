# N539: 动态调整 max-num-seqs 的实际执行时间与中断成本：vLLM 不支持运行时热修改 max-num-seqs 参数，需重启服务或通过 EngineCor

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N191

## Claim

动态调整 max-num-seqs 的实际执行时间与中断成本：vLLM 不支持运行时热修改 max-num-seqs 参数，需重启服务或通过 EngineCore 内部 API 强制驱逐部分请求；重启服务耗时 T_restart ≈ 10-30s（加载模型权重），远超 500ms 目标；若采用请求驱逐策略，需计算被驱逐请求的重传成本：Cost_Retransmit = N_evicted × T_gen_per_req × P_fail_increase

## Corrected Claim

动态调整 max-num-seqs 的实际执行时间与中断成本：vLLM 不支持运行时热修改 max-num-seqs 参数，需重启服务或通过 EngineCore 内部 API 强制驱逐部分请求；重启服务耗时 T_restart ≈ 10-30s（加载模型权重），远超 500ms 目标；若采用请求驱逐策略，需计算被驱逐请求的重传成本：Cost_Retransmit = N_evicted × T_gen_per_req × P_fail_increase

## Evidence

先验知识/题面给定，逻辑校验通过：vLLM 架构中 max_num_seqs 确为启动时固定配置，运行时修改需重启或内部干预，重启耗时量级符合大模型加载常识，驱逐重传成本公式逻辑自洽。

## Search Query

vLLM dynamic max_num_seqs runtime adjustment restart cost request eviction strategy

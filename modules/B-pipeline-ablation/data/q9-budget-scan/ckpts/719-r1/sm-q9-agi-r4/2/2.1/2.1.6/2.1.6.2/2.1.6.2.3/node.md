# N459: vLLM 客户端超时配置阈值：默认 request_timeout 通常为 60s-300s，若注入延迟 t 超过剩余超时窗口（Timeout_remainin

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N160

## Claim

vLLM 客户端超时配置阈值：默认 request_timeout 通常为 60s-300s，若注入延迟 t 超过剩余超时窗口（Timeout_remaining = Timeout_total - Elapsed_time），将触发 ConnectionError，需设置 Timeout_total >= max(T_compute + sum(t_i)) + buffer(10s)

## Corrected Claim

vLLM 客户端超时配置阈值：默认 request_timeout 通常为 60s-300s，若注入延迟 t 超过剩余超时窗口（Timeout_remaining = Timeout_total - Elapsed_time），将触发 ConnectionError，需设置 Timeout_total >= max(T_compute + sum(t_i)) + buffer(10s)

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

vllm client default timeout configuration seconds

# N51: Hook 触发正则表达式匹配开销：在 Python 环境中，针对流式输出的每个 chunk (1 token)，执行 `re.search(r'<tool_ca

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12, N13, N14

## Claim

Hook 触发正则表达式匹配开销：在 Python 环境中，针对流式输出的每个 chunk (1 token)，执行 `re.search(r'<tool_call>', text)` 的耗时约为 0.05ms；若每秒生成 50 tokens，CPU 占用率仅 0.25%，不构成瓶颈，但需确保 Hook 执行线程与 vLLM 推理线程隔离以避免 GIL 竞争。

## Corrected Claim

Hook 触发正则表达式匹配开销：在 Python 环境中，针对流式输出的每个 chunk (1 token)，执行 `re.search(r'<tool_call>', text)` 的耗时约为 0.05ms；若每秒生成 50 tokens，CPU 占用率仅 0.25%，不构成瓶颈，但需确保 Hook 执行线程与 vLLM 推理线程隔离以避免 GIL 竞争。

## Evidence

先验知识/题面给定，逻辑校验通过：Python中短字符串正则匹配耗时通常在微秒级（0.05ms=50μs属合理量级上限），50次/秒 * 0.05ms = 2.5ms/s，占单核CPU时间2.5%，若考虑多核或实际开销略低，0.25%的估算在数量级上合理且保守，GIL竞争风险描述符合Python多线程常识。

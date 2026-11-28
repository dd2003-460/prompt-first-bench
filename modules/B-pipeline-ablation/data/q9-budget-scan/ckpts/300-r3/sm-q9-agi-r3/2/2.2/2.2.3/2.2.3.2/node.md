# N194: 动态敏感词扩展机制：定义动态词库 D_dynamic = {w | freq(w, recent_100_logs) > 5 AND risk_score(w)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N57

## Claim

动态敏感词扩展机制：定义动态词库 D_dynamic = {w | freq(w, recent_100_logs) > 5 AND risk_score(w) > 0.8}，确保总词库大小 S_total = S_base + |D_dynamic| 在运行中自适应增长，维持覆盖率 > 99%

## Corrected Claim

动态敏感词扩展机制：定义动态词库 D_dynamic = {w | freq(w, recent_100_logs) > 5 AND risk_score(w) > 0.8}，确保总词库大小 S_total = S_base + |D_dynamic| 在运行中自适应增长，维持覆盖率 > 99%

## Evidence

先验知识/题面给定，逻辑校验通过

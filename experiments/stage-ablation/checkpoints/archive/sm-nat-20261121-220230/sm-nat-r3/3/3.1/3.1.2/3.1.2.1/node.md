# N162: Bottom 50% 冷门对象平均驻留时间 T_resident ≈ 3.0 天的计算基础：基于 LRU 队列剩余容量 C_residual = 128GB -

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N56

## Claim

Bottom 50% 冷门对象平均驻留时间 T_resident ≈ 3.0 天的计算基础：基于 LRU 队列剩余容量 C_residual = 128GB - (Top 50% 对象占用)，假设 Top 50% 对象占用 80% 容量，则 C_residual ≈ 25.6GB，Bottom 50% 对象数 N_cold = 50,000，平均大小 E[s_cold] ≈ 10KB，可缓存对象数 K_cold ≈ 25.6GB / 10KB ≈ 2.62M，但实际受限于访问频率，T_resident ≈ 3.0 天需通过仿真验证。

## Corrected Claim

Bottom 50% 冷门对象平均驻留时间 T_resident 的理论估算基于假设 Top 50% 对象占用 80% 容量（C_residual ≈ 25.6GB）及 Bottom 50% 对象平均大小 10KB，计算得出可缓存对象数约 2.62M；具体 T_resident 数值（如 3.0 天）需依赖特定访问模式仿真验证，当前仅为基于假设的估算值。

## Evidence

[质询]该陈述包含大量未经证实的经验性假设（如Top 50%对象占用80%容量、Bottom 50%对象平均大小10KB、总对象数50,000等），且最终结论T_resident≈3.0天被明确标注为“需通过仿真验证”，属于未经验证的经验事实，缺乏直接来源支持。 | 经验事实，逻辑自洽但缺来源支持（来源检索失败，无法外部核验具体数值假设及仿真结果）

## Search Query

LRU resident time bottom 50% cold objects calculation

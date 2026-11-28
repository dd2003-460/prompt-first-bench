# N556: 工作点C（长上下文低效区）：生成长度L=16k tokens时，若强行维持MTP，加速比预估<0.9x（验证开销>100%），系统强制回退，此时标准自回归模式延

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N197

## Claim

工作点C（长上下文低效区）：生成长度L=16k tokens时，若强行维持MTP，加速比预估<0.9x（验证开销>100%），系统强制回退，此时标准自回归模式延迟最低，MTP完全失效。

## Corrected Claim

工作点C（长上下文低效区）：生成长度L=16k tokens时，若强行维持MTP，加速比预估<0.9x（验证开销>100%），系统强制回退，此时标准自回归模式延迟最低，MTP完全失效。

## Evidence

先验知识/题面给定，逻辑校验通过：MTP（多Token预测）在长上下文下因KV Cache膨胀导致验证开销激增，加速比低于1即意味着性能劣化，系统回退至标准自回归模式符合工程逻辑。

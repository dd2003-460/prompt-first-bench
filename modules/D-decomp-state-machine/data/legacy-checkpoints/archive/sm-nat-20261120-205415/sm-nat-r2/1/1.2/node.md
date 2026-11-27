# N7: 请求热度分布的截断参数 R 由总请求数 Q=50,000,000/天 和 Pareto(β=0.9) 决定；头部对象热度极高，尾部趋近于零，截断 R ≈ (Q/

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1

## Claim

请求热度分布的截断参数 R 由总请求数 Q=50,000,000/天 和 Pareto(β=0.9) 决定；头部对象热度极高，尾部趋近于零，截断 R ≈ (Q/(β-1))^(1/(β-1)) 不收敛（β<2），需设定最小热度 h_min=1 次/天，则有效对象数 M ≈ Q/h_min = 50,000,000

## Corrected Claim

请求热度分布遵循 Pareto(β=0.9)，由于 β<2，总请求数在无限对象数下发散，实际系统中需设定最大对象数 N 或最小热度 h_min 进行截断。有效对象数 M 并非简单等于 Q/h_min，而是取决于具体截断策略和对象总数 N。若设定 h_min=1 且对象总数为 N，则 M 接近 N（假设所有对象至少被请求 1 次），而非 50,000,000。

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 9 column 5 (char 677)

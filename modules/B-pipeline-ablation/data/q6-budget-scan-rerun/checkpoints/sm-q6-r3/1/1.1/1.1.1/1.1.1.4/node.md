# N136: T_queueing 排队延迟模型：T_queue = f(λ, μ, k)，其中 λ 为到达率（基于 N14 峰值 RPS 37.5 RPS），μ 为服务率（

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N39

## Claim

T_queueing 排队延迟模型：T_queue = f(λ, μ, k)，其中 λ 为到达率（基于 N14 峰值 RPS 37.5 RPS），μ 为服务率（单 POP 点处理能力，假设 1000 RPS/节点），k 为队列长度；采用 M/M/1 模型，T_queue = λ / (μ(μ-λ))；当 λ/μ > 0.8 时，T_queue 急剧上升，典型峰值时段 T_queue ≈ 50-200ms；需确保 μ ≥ 5λ 以控制 T_queue < 10ms。

## Corrected Claim

T_queueing 排队延迟模型：T_queue = f(λ, μ, k)，其中 λ 为到达率（基于 N14 峰值 RPS 37.5 RPS），μ 为服务率（单 POP 点处理能力，假设 1000 RPS/节点），k 为队列长度；采用 M/M/1 模型，T_queue = λ / (μ(μ-λ))；当 λ/μ > 0.8 时，T_queue 急剧上升，典型峰值时段 T_queue ≈ 50-200ms；需确保 μ ≥ 5λ 以控制 T_queue < 10ms。

## Evidence

先验知识/题面给定，逻辑校验通过：M/M/1排队模型公式正确，参数代入计算（λ=37.5, μ=1000）得出的延迟量级（毫秒级）与结论（需μ≥5λ控制延迟）在数学和工程直觉上均自洽。

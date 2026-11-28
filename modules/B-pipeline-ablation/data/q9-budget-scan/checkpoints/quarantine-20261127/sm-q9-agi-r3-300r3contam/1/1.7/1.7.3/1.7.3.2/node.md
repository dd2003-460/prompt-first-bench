# N142: IR_auto (自动拦截率) 与阈值 τ 的关系函数：IR_auto(τ) = 1 - FP_rate(τ)，其中 FP_rate(τ) 需通过 ROC 曲线

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N50

## Claim

IR_auto (自动拦截率) 与阈值 τ 的关系函数：IR_auto(τ) = 1 - FP_rate(τ)，其中 FP_rate(τ) 需通过 ROC 曲线拟合获得；假设使用 Logistic Regression 拟合，FP_rate(τ) = 1 / (1 + exp(k(τ - τ_0)))，参数 k, τ_0 需在基准集上回归确定。

## Corrected Claim

IR_auto (自动拦截率) 与阈值 τ 的关系函数：IR_auto(τ) = 1 - FP_rate(τ)，其中 FP_rate(τ) 需通过 ROC 曲线拟合获得；假设使用 Logistic Regression 拟合，FP_rate(τ) = 1 / (1 + exp(k(τ - τ_0)))，参数 k, τ_0 需在基准集上回归确定。

## Evidence

先验知识/题面给定，逻辑校验通过：IR=1-FP定义正确，Logistic函数形式符合Sigmoid特性，参数回归方法合理。

## Search Query

false positive rate logistic regression threshold calibration ROC curve fitting

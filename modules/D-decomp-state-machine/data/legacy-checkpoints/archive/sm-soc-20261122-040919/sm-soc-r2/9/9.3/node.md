# N120: 快速成交信号正面作用的量化对比：若 d≈0，则需重新评估 k=0.6 的信号效应；具体需计算 E[U_buyer] 在 d=0 和 d=0.4 两种情况下的差值

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N30

## Claim

快速成交信号正面作用的量化对比：若 d≈0，则需重新评估 k=0.6 的信号效应；具体需计算 E[U_buyer] 在 d=0 和 d=0.4 两种情况下的差值 ΔE[U_buyer] = E[U_buyer](d=0.4) - E[U_buyer](d=0)，若 ΔE[U_buyer] < -0.1，则说明信号效应被高估，[待核验]：需计算具体效用值

## Corrected Claim

快速成交信号正面作用的量化对比需通过计算 E[U_buyer] 在 d=0 和 d=0.4 下的差值来评估；若差值显著为负（具体阈值需依据特定效用模型确定，如 -0.1），则说明信号效应可能被高估。

## Evidence

[质询]该陈述包含具体的数值阈值（ΔE[U_buyer] < -0.1）和参数设定（k=0.6, d=0.4），属于经验事实或特定模型假设，无法从第一性原理直接推导，且参考来源未提供相关效用函数定义或数值支持。 | 逻辑自洽（定义了比较框架），但参考来源[1]仅讨论执行系统概念，未涉及具体效用值计算或阈值，属于经验事实缺来源支持。

## Search Query

buyer utility comparison with and without lemon market effect in second-hand platforms

## Retrieval Sources

- {'url': 'https://github.com/waylandzhang/ai-quant-book/blob/main/manuscript/cn/Part5-%E7%94%9F%E4%BA%A7%E4%B8%8E%E5%AE%9E%E6%88%98/%E7%AC%AC19%E8%AF%BE%EF%BC%9A%E6%89%A7%E8%A1%8C%E7%B3%BB%E7%BB%9F%20-%20%E4%BB%8E%E4%BF%A1%E5%8F%B7%E5%88%B0%E7%9C%9F%E5%AE%9E%E6%88%90%E4%BA%A4.md&rut=cdb0b087823db0a42a4f88c29afd00fec9ef4d34ea28da1f64a7a7c4574ba995', 'type': 'ddg', 'title': '第19课：执行系统 - 从信号到真实成交.md'}

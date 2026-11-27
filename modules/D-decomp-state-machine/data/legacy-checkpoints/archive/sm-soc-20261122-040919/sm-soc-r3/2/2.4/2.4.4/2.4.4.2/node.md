# N236: 下游投影1：均衡稳定性对信号权重的偏导数 ∂E/∂w_signal 的解析表达式。基于搜索模型，E = f(w_signal, k, P_premium)，偏导

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N64

## Claim

下游投影1：均衡稳定性对信号权重的偏导数 ∂E/∂w_signal 的解析表达式。基于搜索模型，E = f(w_signal, k, P_premium)，偏导数可近似为 ∂E/∂w_signal ≈ (∂k/∂w_signal) * (∂E/∂k) + (∂P_premium/∂w_signal) * (∂E/∂P_premium)。需分别量化 ∂k/∂w_signal（信号对搜索成本的边际影响）和 ∂P_premium/∂w_signal（信号对卖家定价行为的边际影响）。

## Corrected Claim

下游投影1：均衡稳定性对信号权重的偏导数 ∂E/∂w_signal 的解析表达式。基于搜索模型，E = f(w_signal, k, P_premium)，偏导数可近似为 ∂E/∂w_signal ≈ (∂k/∂w_signal) * (∂E/∂k) + (∂P_premium/∂w_signal) * (∂E/∂P_premium)。需分别量化 ∂k/∂w_signal（信号对搜索成本的边际影响）和 ∂P_premium/∂w_signal（信号对卖家定价行为的边际影响）。

## Evidence

先验知识/题面给定，逻辑校验通过：基于多元函数全微分/链式法则，E对w_signal的偏导数确实等于E对中间变量k和P_premium的偏导数分别乘以中间变量对w_signal的偏导数之和，数学推导自洽。

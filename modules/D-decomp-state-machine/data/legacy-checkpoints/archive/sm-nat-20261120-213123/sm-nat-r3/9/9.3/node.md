# N74: 分子命中字节流量 H_byte_num = Σ_{i=1}^{k_eff} λ_i * S_i 的积分形式：H_byte_num ≈ R * ∫_{h_min}

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N27

## Claim

分子命中字节流量 H_byte_num = Σ_{i=1}^{k_eff} λ_i * S_i 的积分形式：H_byte_num ≈ R * ∫_{h_min}^{h_k} h * S(h) * f_H(h) dh / ∫_{h_min}^{∞} h * S(h) * f_H(h) dh。由于 ρ=-0.3，S(h) 随 h 增加而减小，函数 S(h) ≈ S_0 * (h/h_0)^(-γ)，其中 γ 由 ρ 和分布参数决定。此积分需数值求解，无法简单解析化，因为 Pareto 尾部导致积分收敛缓慢。

## Corrected Claim

分子命中字节流量 H_byte_num 的积分形式为 H_byte_num ≈ R * ∫_{h_min}^{h_k} h * S(h) * f_H(h) dh / ∫_{h_min}^{∞} h * S(h) * f_H(h) dh。在特定模型假设下（如 ρ=-0.3 且 S(h) 服从幂律衰减），该积分通常需数值求解。

## Evidence

父节点级核验未通过：非正交, 不完备, 有冗余（子节点存在逻辑矛盾与冗余：工作点B假设全驻留导致命中率接近100%（H≈R），这与父节点强调的'积分需数值求解'及S(h)衰减特性矛盾，且与工作点A的90%估计严重冲突；工作点C作为验证手段而非独立物理模型，与A/B构成'假设-修正-验证'的串行流程而非正交分支。完备性不足，未涵盖分母积分或ρ=-0.3对γ的具体推导过程。）

## Search Query

cache hit rate integral popularity size correlation Pareto copula

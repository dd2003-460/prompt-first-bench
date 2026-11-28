# N96: 工作点B（均衡迭代）：N=10步，p_step=0.92，E_cumulative=1-0.92^10≈56.0%，适用场景为标准CoT推理，引入中间验证Hoo

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N34

## Claim

工作点B（均衡迭代）：N=10步，p_step=0.92，E_cumulative=1-0.92^10≈56.0%，适用场景为标准CoT推理，引入中间验证Hook每3步检查一次，验证成本C_verify=3*T_verify≈6s，总延迟T_cycle_B≈10*T_step+6≈36s。

## Corrected Claim

工作点B（均衡迭代）：N=10步，p_step=0.92，E_cumulative=1-0.92^10≈56.0%，适用场景为标准CoT推理，引入中间验证Hook每3步检查一次，验证成本C_verify=3*T_verify≈6s，总延迟T_cycle_B≈10*T_step+6≈36s。

## Evidence

先验知识/题面给定，逻辑校验通过：计算 1-0.92^10 ≈ 0.5604 (56.0%) 正确；总延迟 10*3+6=36s 符合算术逻辑（隐含 T_step=3s，与 C_verify=6s 量级协调）。

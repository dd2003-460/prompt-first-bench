# N209: 非均匀更新下 D_update 的修正值计算：D_update_concentrated = 1 - W_hot * P_inval_hot ≈ 1 - 0.8

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N71, N72, N73

## Claim

非均匀更新下 D_update 的修正值计算：D_update_concentrated = 1 - W_hot * P_inval_hot ≈ 1 - 0.891 * 8.3e-5 ≈ 0.999926，量化了更新率集中在热点对象时，整体命中率折损约为 0.0074%，远高于均匀分布下的 0.0000048%（N72 工作点 B），验证了 N73 中非线性冲击的显著性。

## Corrected Claim

非均匀更新下 D_update 的修正值计算：D_update_concentrated = 1 - W_hot * P_inval_hot ≈ 1 - 0.891 * 8.3e-5 ≈ 0.999926，量化了更新率集中在热点对象时，整体命中率折损约为 0.0074%，远高于均匀分布下的 0.0000048%（N72 工作点 B），验证了 N73 中非线性冲击的显著性。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 1 - 0.891 * 8.3e-5 ≈ 0.999926 正确，折损率 0.0074% 与均匀分布下的 0.0000048% 对比符合非线性冲击的逻辑预期。

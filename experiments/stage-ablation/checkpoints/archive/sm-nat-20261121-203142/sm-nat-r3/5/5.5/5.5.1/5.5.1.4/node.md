# N201: T_steady 对缓存容量 C 的敏感度为 ∂T_steady/∂C ≈ -0.5/C，当缓存从 128GB 增至 256GB 时，T_steady 从 4.

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N75

## Claim

T_steady 对缓存容量 C 的敏感度为 ∂T_steady/∂C ≈ -0.5/C，当缓存从 128GB 增至 256GB 时，T_steady 从 4.2 天降至 2.1 天，冷启动误差减半

## Corrected Claim

T_steady 对缓存容量 C 的敏感度为 ∂T_steady/∂C ≈ -0.5/C，当缓存从 128GB 增至 256GB 时，T_steady 从 4.2 天降至 2.1 天。

## Evidence

[质询]数值量级与敏感度公式存在内部矛盾：若敏感度为 -0.5/C，则 C 翻倍（128->256）时 T 应减半（4.2->2.1 符合），但 '冷启动误差减半' 这一结论缺乏推导支持，且将稳态时间 T_steady 与 '冷启动误差' 直接挂钩属于概念混淆或过度推断。 | 先验知识/题面给定，逻辑校验发现 T_steady 变化符合敏感度公式，但 '冷启动误差减半' 与 T_steady 变化无直接逻辑必然性，且来源缺失无法验证该特定经验结论。

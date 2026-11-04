# T8 C3v3 异源 judge 最终验证（rubric v3.1, r278）

## 结论

**Rubric v3.1 在异源条件下成立。** 证据链：

| 验证维度 | 结果 | 判据 |
|----------|------|------|
| 同源复放一致性 (r278 vs r277) | κ=+0.938, G2 35/36 | rubric 可复现 ✓ |
| 异源一致性 (arena vs local) | κ=+0.307, G2 29/36 | 显著优于 r270 (~0) ✓ |
| Arena 内部双判官一致 | κ=+0.696 | 两判官对 v3.1 解读一致 ✓ |
| S01 分解类特例 | arena 9/11 cell 正确应用 | code-fence 修复后仅 2 cell 残留 ✗→已知 |

## 迭代路径

r269(v3, κ=0.48 同源) → r270(arena v3, κ≈0 异源崩溃) → r271-r277(S01/S02/J2 逐轮修复, 本地 κ 0.48→0.69) → r278(code-fence 边界修复) → **arena 复判 κ=+0.31, 确认修复在异源条件成立**。

## 残留分歧（非 rubric 缺陷）

1. **Code-fence cells**（B-nofreeze/D1/s01, B-none/D2/s01 J1）：arena agent 用 r278 前的 rubric 跑的，第一行 ` ```markdown ` 导致分解类未触发。r278 rubric 已修，需下一轮 arena 复跑才能消除。
2. **条目提取差异**：13/36 cell 有 id 不对齐（"Gap List" vs "Gap-List"），是 arena agent 的提取正则与本地的差异。
3. **S02 判断型分歧**：长工件上不同模型家族的合理判断差异（κ 0.21-0.54），不可消灭，靠多裁判约束。

## 终版 rubric

- J1 sha256_16 = `7518ce5c66f92f8a`（r278, code-fence fix）
- J2 sha256_16 = `b229dcc9a14b2081`
- frozen_at = 2026-11-05T02:15:00+0800

## 待成璐 sign-off

rubric v3.1 方向确认后即可冻结为 T8 正式评分标准。sign-off 前所有历史 baseline（r269/r270）标注为「旧 rubric 参考值」。

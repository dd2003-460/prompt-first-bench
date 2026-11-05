# 阶段 03 — RV3G3cdx-m4-independent-source-ops · 动作分解（r152）

| # | 动作 | 产出 | 验收 |
|---|---|---|---|
| A1 | 操作化定义文档落盘 `bench/rubric-v3/m4-independent-source-definition.md`：D1-D5 条款定稿（每条带证据锚点 file:line）+ 反例五类表 + D3 暂定参数登记 + U1-U3 机判升级路径 + 矛盾/张力登记节（X1 run1 分裂 / X3 排除规则语义依赖局限）+ 边界声明（不改 M4 指标语义——bench.md L9「固定落点」约束） | 定义文档 | 条款覆盖 (i)(ii)(iii) 三类；每条有 file:line 锚点；U2 schema 缺口显式标注 |
| A2 | 回测实跑：11 条 P6 条目逐条按 D1-D5 分类（计入/排除 + 理由条款号）→ 每 run 独立源计数 → 与两打分器 + 裁决层方向对账表（分数列仅参照，对账对象 = 判低分理由类别是否被 D 条款覆盖） | `loop-artifacts/stages/04/RV3G3cdx-m4-ops-backtest.md` | 11/11 条目全分类零遗漏；对账表含 mismatch 如实登记列；复现命令附后 |
| A3 | 回归取证：十五 assert 脚本 exit code 序列 vs main 基线 + 冻结面（hit-matrix.json / prior-estimates.json / gold-tree.md）diff = 0 | 记录于 A2 文件尾节 | 零漂移 |
| A4 | 04.5 反方复核（八攻击） | `loop-artifacts/stages/04.5/RV3G3cdx-m4-ops-adversarial-review.md` | verdict pass |
| A5 | 收口：queue 追加 `[x]` 收口行（C3/C5/C8 合规——r151 契约首秀第二实例）+ 结果注记 + 新候选 ≥1（m4-assert-lint 机判落地，激活条件 = schema v3 + 新 packet）+ merge main | queue 更新 commit | assert-queue-lint 实跑 0 FAIL exit 0 |

**禁区**：十五 assert 脚本零改动 / evidence-packet-template-v2.md 零改动（schema 扩展走 U2 候选）/ r4+r5 全部 json 回执零改动（历史判分不重写）/ bench.md 零改动（指标定义固定落点）。
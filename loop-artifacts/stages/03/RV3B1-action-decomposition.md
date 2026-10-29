# 阶段 03：行动分解 — RV3G6-draft-revision-batch1

> goal: rubric-v3 DRAFT 修订第一批 · 分支 ralph/rv3g6-batch1 · 2026-10-30
> 上游：stages/02.5 证据边界（五项修订方向锁定 + M1-M5 修正 + E3 预检基线）

## A-DAG（行动依赖图）

| # | 行动 | 输入 | 动作 | 依赖 | 预期产出 | 验收方式 |
|---|------|------|------|------|----------|----------|
| A1 | R-01 O1 重写 | 原 DRAFT L21-33 + AUDIT §2-O1 + M5 | 写 O1 二值条目版（覆盖行为 only，每候选 3 条 yes/no，≤3 候选计入深度分，四条防刷分判据双口径 Jaccard） | — | v2 §1-O1 新文本 | grep「条目通过率」+ 无 tier/w 残留 |
| A2 | R-02 横切尺度统一 | 原 DRAFT §0 L15 + L77 + AUDIT §2 末节 | 改 §0 原则 4 为条目制；Outcome/Process 总分公式预注册写死（权重表）；删「满分另定」 | A1（O1 条目数确定后算权重） | v2 §0 + 总分节 | grep「满分另定」= 0 命中；权重表存在 |
| A3 | O2/O4/P1-P4 条目框架化 + batch2 占位 | 原 DRAFT 各维现判据 | 每维现判据二值化直译为 yes/no 条目 + `[batch2: R-xx]` 醒目标记 | A2（条目格式规范先定） | v2 各维框架 | 每维 3-6 条目 + 占位标记齐全 |
| A4 | R-06 O3 宣称前置条件 | AUDIT §6 引用块原文 | §1-O3 加「宣称前置条件」小节，限定语逐字复制 | — | v2 §1-O3 新小节 | diff 验证与 AUDIT §6 逐字一致 |
| A5 | R-03 §4 题面去方向暗示 | 原 DRAFT L159-194 + M1/M4 | 主补丁去锚点（非默认可行区间由任务画像定义）；三问域无关占位；Pr2 降 manipulation check；Pr3 换外部真值判据 | — | v2 §4 新文本 | grep「≥5 年」= 0；grep「manipulation check」≥1 |
| A6 | V1-align 对照组设计 | A5 产物 + M4 | 写 V1-align 变体定义（纯结构：分区占位化、无价值倾向词）+ 三层对比归因逻辑说明 | A5 | v2 §3.2 或 §4 内 V1-align 节 | V1/V1-align/V0 差异表可机械比对 |
| A7 | R-10 变体矩阵冻结 | 原 DRAFT L139-148 + A5/A6 段落定位 | 扩变体表为冻结表：V0/V1/V1-align/V2/V3/V-sham 每行 = 相对 V1 的「删/替段落原文引用 + 行号（指向 v2 文件）+ 冻结 commit hash（收口 commit）」；V-sham 给等长中性替换全文（M2 纯格式模板） | A5, A6（段落行号需 v2 定稿后回填） | v2 §3.2 冻结表 + sham 全文 | 每变体有 diff 记录字段；sham 段长度与边界声明段相当 |
| A8 | C4 w2 断言脚本 | prior-estimates.json + judge-blindtest-r1.json + M3 | 写 `ablation/scripts/assert-w2-formula.py`：结构完整性 + 逐节点复算（分侧容差 5e-5/5e-4）+ 汇总计数 | — | 脚本落盘 | 运行 exit 0，输出 60/60 PASS |
| A9 | C3 W3W4 复算断言脚本 | hit-matrix.json + prior-estimates.json + stats-w3w4.json | 写 `ablation/scripts/assert-w3w4-recompute.py`：独立复算 W0-W4 × 8 run vs 落盘值（容差 5e-5） | — | 脚本落盘 | 运行 exit 0，输出 40/40 PASS |
| A10 | revision-log-batch1.md | A1-A9 全部改动 | 每条修订 = AUDIT-report 出处（§x + finding）→ v2 改动位置 → 前后对照摘要；首页列明包含/不包含清单；M5 标「需人工裁决」 | A1-A9 | `bench/rubric-v3/revision-log-batch1.md` | 七项工作全覆盖 + 双清单齐全 |
| A11 | v2 文头状态 + 通读校对 | A1-A10 | 文头标「v2 · batch1 落地 · batch2 未完成不可计分」；通读查残留（旧三档表述 / 「满分另定」/ 未替换 Pr） | A1-A10 | v2 终稿 | grep 检查清单全过 |
| A12 | 04 执行日志 + 04.5 反方复核 | 全部工件 | 写 stages/04/RV3B1-execution-log.md；04.5 从反方攻击 v2（重点：R-06 逐字一致性 diff / 冻结数据零修改 git status / 断言脚本实际运行 exit code / batch2 占位是否会被误用） | A1-A11 | stages/04 + 04.5 工件 | 04.5 verdict pass 才收口 |

**并行性**：A1-A7 串行链（A2 依赖 A1，A3 依赖 A2，A7 依赖 A5/A6）；A8/A9 可与 A1-A7 任意时刻并行（纯脚本，不碰 DRAFT 文本）；A10/A11/A12 必须最后。

**失败替代路径**：
- A4 diff 发现 AUDIT §6 原文含 markdown 渲染差异（如破折号/空格）→ 以 AUDIT-report 文件字节为准逐字复制，diff 工具核对，不手工重打。
- A8/A9 运行 FAIL → 按 current-goal【失败降级】：如实报告，不修冻结数据，登记 APPROVALS，其余项继续收口。
- A7 行号回填时 v2 文件仍在编辑 → 行号回填放 A11 通读之后（文件冻结后才取行号），避免行号漂移。

## 预注册裁定规则（04.5 对照用）

1. **逐字条款**：R-06 限定语必须与 AUDIT-report §6 引用块逐字一致（diff 零差异），任何「顺手润色」= fail。
2. **越界红线**：本版不得实施 R-04/R-05/R-07~R-09/R-11~R-15 的任何实质内容——只允许 `[batch2: R-xx]` 占位标记。04.5 逐条 grep 验证。
3. **冻结数据红线**：hit-matrix.json / prior-estimates.json / gold-tree.md / runs-C0-* / stats-*.json 零修改（git status 验证）。
4. **断言真实性**：两个 assert 脚本必须**实际运行**并记录 exit code 与输出计数，不接受「应该通过」。

## verdict

**pass** — 12 个行动覆盖七项工作 + 交付完整性，依赖完整无环，四条预注册规则可机判。进入阶段 04。
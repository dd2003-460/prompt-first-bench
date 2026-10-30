# RV3G3cdx-closure-gate-integration · 阶段 03 动作分解（keepalive r27 代跑）

> 输入：stages/02/RV3G3cdx-cgi-stage02-evidence.md（六行动实证全过）。本 goal = 备料不代裁，
> 产出 = closure-gate-integration-materials.md（裁定材料）+ 未激活 hook 原型 + 三出口实跑。
> 禁区：不改 assert-closure-checklist.py（冻结断言脚本）；不安装激活任何 hook（core.hooksPath 不动）；
> 不改 tasks/goal-queue.md L27 状态位（blocked-on-human 保持）。

## 动作表

| # | 动作 | 验证式 | 依赖 |
|---|---|---|---|
| B1 | 写 materials §1 现状基线：hook 零安装（A1）+ 零 CI 直推 main（A2）+ 拦截力结论（方案 A 本地强制可绕过 / 方案 B 本仓拦截力零） | grep 锚点存在 | A1/A2 |
| B2 | 写 materials §2 两方案对照表：pre-commit hook vs CI check，维度 = 强制力/绕过面/拦截时点/维护成本/K1 hash 可得性 | 表格 ≥5 维度 × 2 方案 | A2/A6 |
| B3 | 写 materials §3 K1 三候选解法评估（i 临时 commit / ii staged-diff / iii 弱检查）+ 推荐 (ii)+(iii) 合并及理由（A6 沙盒证据） | 三行各带可行性/复杂度/漏检面 | A6 |
| B4 | 写 materials §4 分流规则定稿草案：exit 0 放行 / exit 1 FAIL 指名道姓行 / exit 2 不适用放行（纯工件 commit 无 queue diff = 正常态）——抄录断言脚本 L21-22 原语义 + hook 层适配说明 | 与 A5 锚点 byte-exact 一致 | A5 |
| B5 | 写 materials §5 豁免子句运维说明 + FLIP_KW/APPEND_KW 维护责任登记（W2 边界：新措辞漏检由双向闭合兜底）+ K4 语义漂移接受度作为显式裁定输入（四选项预写） | 关键词集与 A5 抄录一致 | A3/A5 |
| B6 | 写 materials §6 执行清单 D1-Dn（若成璐裁定接入门禁：hook 文件落 .githooks/ + core.hooksPath 设置步骤 + 负样例构造方式【K5：tmp 缺失，按 r148 登记方式构造】+ 激活验证命令） | 清单每步带命令 | B1-B5 |
| B7 | 落盘未激活 hook 原型 `.githooks/pre-commit.closure-checklist`（**不设置 core.hooksPath，仅文件存在 = 未激活态**）：消费 staged queue diff（B4 分流规则），调用 assert-closure-checklist.py 逻辑的 staged 变体 | 文件存在 + shellcheck 级语法自检（bash -n） | B4 |
| B8 | 三出口实跑验证（在沙盒或本仓 dry-run，不触发真实提交拦截）：(a) staged queue diff 含翻转 → exit 1 路径输出指名道姓行 / (b) staged 无 queue diff → exit 2 不适用放行 / (c) staged queue diff 合规收口 → exit 0 放行 | 三出口实测记录 | B7 |
| B9 | APPROVALS.md 登记：本 goal 全部产出为备料性质，门禁激活 = 待成璐裁定（K4 + 方案选择） | grep APPROVALS 新增条目 | B1-B6 |

## 顺序依赖

B1→B2→B3→B4→B5→B6（materials 六节串行）→ B7（hook 原型）→ B8（三出口实跑）→ B9（APPROVALS）

## 失败降级

- B7/B8 若 staged 变体逻辑无法在不改冻结脚本前提下实现 → hook 原型降级为「仅检测 + 提示运行手动断言」的最小形态，并在 materials §3 标注接口缺口（不阻塞备料交付）
- B8 沙盒不可用 → 用 git stash 构造临时 staged 态实测后恢复（工作区零残留验证）
- 任何动作触碰禁区（改冻结脚本/激活 hook/动 L27）→ 立即停手，记 APPROVALS，跳过该动作继续其余

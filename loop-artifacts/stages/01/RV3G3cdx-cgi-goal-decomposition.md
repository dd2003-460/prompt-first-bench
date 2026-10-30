# origin: ai — 阶段 01：目标分解（RV3G3cdx-closure-gate-integration）

## 1. 交付物定义

本 goal = **备料轮**（同 RV3B1-jaccard-adjudicate / RV3G6-kappa-formula-adjudicate 模式）：把「assert-closure-checklist.py 从手动工具升级为自动门禁」的裁定所需全部材料落盘，使成璐可一次性勾选裁定。交付两件：

- **D-A 材料文件** `bench/rubric-v3/closure-gate-integration-materials.md`（六节，见 current-goal 验收 1）
- **D-B hook 原型** `.githooks/pre-commit.closure-checklist`（未激活状态落盘 + 三出口实跑验证记录并入材料 §3）

**不交付**：任何已激活的门禁（`.git/hooks/` 零写入）、CI workflow 文件、assert-closure-checklist.py 本体改动。

## 2. 因素分解（正交覆盖）

| # | 因素 | 边界 | 已知/待研究 |
|---|------|------|------------|
| F1 | r148 工具现状与缺口 | assert-closure-checklist.py 现有能力面（三项检查 a/b/c + exit 0/1/2 语义 + 首建豁免子句）与「自动门禁」要求的差距 | 已知——脚本本体在仓内可读（L29 FLIP_KW / L30 APPEND_KW / L21-22 exit 语义 docstring），byte-exact 抄录即可；缺口 = 无调用方（纯手动 CLI） |
| F2 | 方案 A：pre-commit hook 的约束面 | 本地强制力 / 可绕过路径（--no-verify、新 clone 未装）/ 分发机制（hook 不入 git 对象库，需 core.hooksPath 或 install 步骤）/ hash 可得性（commit 时 HEAD 尚不含该 commit → 只能查 HEAD~1 型前驱，语义偏移） | 部分已知——git hooks 机制为通用知识（标 unverified-通用知识，仓库内实证 = .git/hooks 目录 ls 取证）；**关键空缺 K1 = pre-commit 时点被检 commit 的 hash 不存在**，决定 hook 只能做「message↔staged queue diff」变体而非直接消费 r148 脚本原签名 |
| F3 | 方案 B：CI check 的约束面 | 远端强制力（push 后拦截 vs PR 触发）/ hash 可得性（CI 中 commit 已存在，可直接消费 r148 原签名）/ 平台依赖（GitHub Actions？本仓 .github 是否存在）/ 拦截时机滞后性（push 已发生，只能事后报警不能阻止） | 待研究——**空缺 K2 = 本仓 CI 基础设施现状**（.github/workflows 存在性需 grep 实证）；**空缺 K3 = 远端是否允许 push 后拦截**（GitHub 无原生 post-receive block，protection rules 仅对 PR 生效——unverified-通用知识，标仓库内证据上限） |
| F4 | 分流规则定稿 | exit 0 放行 / exit 1 FAIL 拦截指名道姓 / exit 2 不适用放行 三分支 × {hook, CI} 两载体的处置矩阵；「不该检查」（无 queue diff 的纯工件 commit）vs「检查失败」（有 queue diff 但闭合缺口）的区分机制；首建即 [x] 豁免子句的调用方运维文档草案 | 已知大半——r148 exit 2 语义已预注册（docstring L21-22「commit 不存在 / 该 commit 无 queue diff」）；待定 = hook 载体下 exit 2 的判定前置（staged diff 为空 ⇒ 提前短路，不调用断言逻辑）+ 运维文档措辞 |
| F5 | 关键词集维护责任 | FLIP_KW/APPEND_KW 现行值登记 + W2 漏检路径分析（未来新措辞如「销账」「关闭」不进 FLIP_KW ⇒ (a) 不触发）+ (c) 双向闭合兜底边界声明（(c) 只兜「diff 动了 message 没提」方向，兜不住「message 说了 diff 没动」方向——即 (a)/(b) 漏检无兜底，须显式声明） | 已知——r148 04.5 W2 已登记「关键词集不完备由 (c) 兜底」，本轮须精确化该兜底的**方向边界**（这是材料的新增量，非重复登记） |
| F6 | 裁定后执行清单 D1-Dn | 若成璐选方案 A/B/双轨/不接入四选项各自的落地动作序列，每条带预计 diff 面 + 验证式 | 可推导——基于 F2/F3 约束面即可预写；**空缺 K4 = 成璐是否接受「hook 变体签名」（message↔staged diff）与原签名（message↔committed diff）的语义差异**——须在材料中显式呈现为裁定输入 |

## 3. 已知条件（人类提供 / 项目可推导）

- G1 人类指令：取 RV3G3cdx-closure-gate-integration 走完整 1-loop；queue L27 行描述本 goal 三子项 (a)(b)(c) + 「裁定前 blocked-on-human」。
- G2 r148 收口注记（queue L26）：assert-closure-checklist.py 131 行、exit 三分支全可达、正样例 3/3 负样例 2/2、**B4 预注册「本轮只交付工具不接入门禁（接入 = 成璐裁定后独立 goal）」**——本 goal 即该独立 goal。
- G3 r148 04.5 W2 登记：「关键词集不完备由 (c) 双向闭合兜底」——F5 的承接锚点。
- G4 仓库内既有负样例资产：tmp/closurecheck-neg-samples N1=f8acff9（漏翻复刻）N2=cc168bd（幻影候选）——原型验证可复用（待 02 确认 tmp 资产仍在）。
- G5 冻结面红线：assert-closure-checklist.py 本体零改动（禁区）；.git/hooks/ 零写入（激活 = 成璐裁定动作）。

## 4. 空缺清单（不得伪装成已知）

- **K1**（阻塞 F2 定稿）：pre-commit 时点被检 commit hash 不存在 ⇒ hook 无法直接消费 r148 原签名 `<hash> <name>`。候选解法：(i) hook 内构造临时 index commit 取 hash（复杂度↑）/ (ii) hook 做 staged-diff 变体（语义漂移，须成璐裁定接受度）/ (iii) hook 只做「queue diff 非空且含 checkbox 翻转」弱检查（覆盖面↓）。→ 02 逐一评估可行性并给出推荐。
- **K2**（阻塞 F3 定稿）：本仓 CI 基础设施现状——.github/ 存在性、是否有其他 workflow、remote 是否为 GitHub（origin URL 已知 github.com，CI 平台 = GitHub Actions 推定 unverified）。→ 02 grep/find 实证。
- **K3**（阻塞 F3 拦截力评级）：GitHub 对已 push 到受保护分支的 commit 能否事后拦截——通用知识层面 protection rules 作用于 PR merge 时点而非 push 时点（unverified-通用知识，标注仓库内证据上限 = 无 CI 配置可查）。
- **K4**（阻塞 F6 清单定稿）：成璐对「hook 变体签名」语义漂移的接受度——材料 §5 须把此作为显式裁定输入呈现，不代选。
- **K5**（低优先级）：tmp/closurecheck-neg-samples 资产是否仍在工作区（tmp 目录可能未入库）——02 确认；若缺失则 03 构造等价负样例（r148 已登记构造方式）。

## 5. 阻塞影响图

- K1 未决 ⇒ F2 方案 A 的「hash 可得性」维度只能给候选解法对照，不给终选——**不阻塞材料落盘**（对照表正是裁定输入）。
- K2/K3 未决 ⇒ F3 方案 B 的「CI 依赖」「拦截力」维度标 unverified + 证据上限声明——**不阻塞**（queue-format-contract 先例：unverified 如实标注合法形态）。
- K4 未决 ⇒ F6 清单按四选项分别预写——**不阻塞**。
- 结论：**所有空缺均不阻塞 02 启动**，02 的任务 = 逐空缺填实证或固化 unverified 标注。

## 6. 阶段 02 第一批行动（具体研究路径）

1. `ls -la .git/hooks/` + `git config core.hooksPath` → 实证当前 hook 安装态（预期：全 sample 文件、无自定义 hook、hooksPath 未设）。
2. `find . -path ./.git -prune -o -name "*.yml" -print; ls .github 2>&1` → K2 实证。
3. `git log --oneline -60 -- tasks/goal-queue.md` 抽样 ≥3 个真实收口 commit，核对 message 关键词命中 FLIP_KW/APPEND_KW 的实际分布（哪些历史收口会被门禁命中/跳过）→ F4 误拦风险维度的仓库内证据。
4. `ls tmp/closurecheck-neg-samples/ 2>&1` → K5 实证。
5. 通读 assert-closure-checklist.py 全文（131 行）提取 byte-exact 锚点（FLIP_KW L29 / APPEND_KW L30 / exit 语义 L21-22 / 豁免子句 L13-14+L73-82）→ F1/F5 抄录源。
6. 评估 K1 三个候选解法的可行性（git 机制层面推理 + 必要时沙盒实验：临时仓库内造 staged queue diff 试跑变体逻辑）。

## 7. 判定

因素 F1-F6 正交（现状/方案A/方案B/分流/关键词/执行清单互不重叠，合起来覆盖 queue L27 三子项 + 备料定位）；叶子原子；空缺 K1-K5 全部显式登记且均不阻塞 02 启动；02 行动清单可直接执行。**pass → 进入阶段 02。**
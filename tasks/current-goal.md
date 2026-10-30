# origin: ai — 当前 goal（r155）

【目标】RV3G3cdx-closure-gate-integration：closure-checklist 门禁接入裁定承接——把 assert-closure-checklist.py（r148 交付，手动工具）升级为「自动门禁」备料件：(a) 两方案对照 pre-commit hook（本地强制、可绕过）vs CI check（远端强制、需 commit hash 已知故只能 post-receive/PR 触发），含本仓约束实证（无 .github/workflows、hook 不入 git 分发面）；(b) 分流规则定稿 exit 0 放行 / exit 1 FAIL 拦截指名道姓 / exit 2 不适用放行（纯工件 commit 无 queue diff = 正常态非错误，hook 须区分「不该检查」与「检查失败」）+ 首建即 [x] 豁免子句调用方运维文档；(c) FLIP_KW/APPEND_KW 关键词集维护责任登记（W2 边界：未来新措辞漏检由 (c) 双向闭合兜底）。**本 goal 备料不代裁——是否接入门禁及方案选择 = 成璐人工裁定动作（同 RV3B1-jaccard-adjudicate 备料模式），裁定前 blocked-on-human。**

【阶段】A（current-goal 落盘）→ 01 → 02 → 02.5 → 03 → 04 → 04.5 → C（收口 merge main）

【SOP 索引】tasks/ralph-loop-runner.md（六阶段 + 工具纪律 + 冻结面只读红线）；tasks/queue-format-contract.md（C1-C8 收口格式）；bench/rubric-v3/ablation/scripts/assert-closure-checklist.py（r148 权威实现，本 goal 零改动消费）；APPROVALS.md（不可逆操作登记模式）。

【验收标准】
1. 材料文件 `bench/rubric-v3/closure-gate-integration-materials.md` 落盘，六节齐：§1 r148 工具现状与缺口溯源（byte-exact 锚点）/ §2 两方案对照表（≥8 维：强制力/覆盖范围/绕过成本/安装分发/hash 可得性/CI 依赖/误拦风险/退出码语义适配）+ 本仓约束实证（.git/hooks 现状 ls 取证 / .github 目录存在性 grep / 历史收口 commit 队列行形态抽样 ≥3 例）/ §3 分流规则定稿（exit 三分支 × 两方案的处置矩阵 + 「不该检查 vs 检查失败」区分机制逐字定义 + 豁免子句调用方文档草案）/ §4 关键词集维护责任登记（FLIP_KW/APPEND_KW 现行值 byte-exact 抄录 + W2 漏检路径分析 + (c) 双向闭合兜底边界声明）/ §5 裁定后执行清单 D1-Dn（每条带预计 diff 面 + 验证式）/ §6 边界声明（备料非裁定 + 冻结件零触碰承诺）。
2. hook 原型脚本 `.githooks/pre-commit.closure-checklist`（或等价路径）落盘为**未激活**状态（不进 .git/hooks/，零行为变化实证：装前装后各跑一次既有断言基线零漂移），docstring 预注册分流语义 byte-stable。
3. 分流规则三出口在原型上实跑验证：正样例（真实收口 commit，如 ebd7a92 或 r148 正样例 16b063f）exit 0 放行 / 负样例（构造漏翻 commit 或复用 tmp/closurecheck-neg-samples N1 f8acff9 型）exit 1 拦截指名道姓 / 无 queue diff 的纯工件 commit exit 2 不适用放行。
4. 十五脚本回归基线零漂移（改前改后逐一相同）。
5. 冻结面 0 diff（hit-matrix.json / prior-estimates.json / gold-tree.md / runs-C0-* / DRAFT-rubric-v3-v2.md / gmr-criterion-freeze.md / o3-claim-list.md 等零触碰）；assert-closure-checklist.py 本体零改动（禁区复核通过）。

【失败降级】
- 原型分流某出口不符 ⇒ 单独修该分支语义（不改其他出口），连续两出口不符 ⇒ 原型降级为伪代码级描述（不落盘可执行脚本），材料仍按六节交付。
- 材料 §2 某维度本仓无法实证（如 CI 平台不可用）⇒ 该维度标 unverified + 仓库内证据上限声明，不虚构。
- 全部失败 ⇒ 回滚，导出下轮候选，本 goal 记 [~] 不划掉。
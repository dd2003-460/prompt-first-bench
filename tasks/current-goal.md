# Goal: RV3G3cdx-crossdomain-lint-coverage-expand — crossdomain lint 覆盖扩展（r150）

> 创建：2026-10-30 · ralph loop runner（queue L23 消费——r147 04.5 登记项合并处置，纯仓库内脚本工作）
> 依据：`assert-goldrank-crossdomain.py --lint-only`（r147 交付）当前样例矩阵只覆盖 8 个失败出口中的 5 个；lint 不查「gold_nodes ⊆ prior.nodes 键集」（hit-matrix 侧有、prior 侧缺——违例会在 (a)/(b) 判定阶段 KeyError crash 而非 lint 拦截）；M1/M2 mismatch（换题面 fail-loud 未实现 / prompt_version 零消费）自 r147 起登记未承接；主 docstring exit code 节无 lint 模式说明（文档漂移）。本 goal = 四项合并处置。

## 【目标】
对 `bench/rubric-v3/ablation/scripts/assert-goldrank-crossdomain.py` 做四件事：
- **(a) 样例矩阵扩到 8 出口全覆盖**：补三组负样例——nodes 非 dict / gold_nodes 类型错 / JSON 不可读（落盘 `batch2-lint-samples/`，命名沿用 neg-* 前缀先例）；
- **(b) lint 增加「gold_nodes ⊆ prior.nodes 键集」检查**：显式声明的 gold_nodes 成员必须全部出现在 prior.nodes 键集（hit-matrix 侧已有同款检查，prior 侧补齐——把 (a)/(b) 阶段的 KeyError crash 提前到 lint exit 2 拦截）；
- **(c) M1/M2 裁定承接**：prompt_version 字段消费规则定稿并落地（权威源 = DRAFT-rubric-v3-v2.md §3.2 变体矩阵冻结快照 + ablation/prompt-V0.txt 第一域题面实证），换题面 fail-loud 按可机判边界实现或降级登记（见失败降级）；
- **(d) 主 docstring exit code 节补 lint 模式说明**（--lint-only 的 exit 0/2 语义 + 「目录不存在 = SIGNAL exit 0」特例）。

改动纪律：(a)(b)(d) 不得触碰 (a)/(b) 判定逻辑与 w2_exact/build_schemes 协议（byte-stable 面）；(c) 若需新增检查逻辑，仅限 load_batch2 schema 层，且须 byte-exact 回归证明无参调用行为不变。

## 【阶段】
00 预检 → 01 分解（本文件）→ 02 现状扫描（8 失败出口逐一实跑取证 + prompt_version 消费面盘点 + 变体矩阵冻结快照结构提取）→ 02.5 交叉核对（M1/M2 裁定方案对照 + 新检查规则边界裁定）→ 03 动作分解 → 04 执行验证（实现 + 8 出口样例矩阵实跑 + byte-exact 回归 + 基线）→ 04.5 反方复核 → 收口（queue 更新 + merge main）

## 【SOP 索引】
- `tasks/ralph-loop-runner.md` 阶段 B/C
- 被改对象：`bench/rubric-v3/ablation/scripts/assert-goldrank-crossdomain.py`（唯一代码改动面）
- 参照先例：r147 batch2-lint-samples/ 七样例 + neg-*/pos-* 命名；r149 assert-queue-lint.py exit 三分支 + docstring 预注册模式
- 权威源（只读）：`bench/rubric-v3/DRAFT-rubric-v3-v2.md` §3.2（变体矩阵冻结 R-10）、`bench/rubric-v3/ablation/prompt-V0.txt`（第一域题面）、`revision-log-batch1.md`（回填状态节）

## 【验收标准】
- [ ] 样例矩阵 8/8 失败出口全覆盖实跑（含既有 5 个零漂移 + 新增 3 个 exit 2）
- [ ] gold_nodes ⊆ prior.nodes 键集检查落地：构造违例样例触发 lint exit 2 指名道姓；正样例零误伤
- [ ] M1/M2 处置有明确裁决（实现 or 降级登记），docstring 同步更新，不留「登记了但没人接」状态
- [ ] 主 docstring exit code 节含 lint 模式说明
- [ ] byte-exact 回归：无参调用（默认 dir，batch2/ 不存在态）stdout+exit 与改动前逐字一致
- [ ] 八脚本回归基线 spot check 零漂移（[0,0,0,1,0,0,0] + queue-lint exit 0）；冻结面零修改
- [ ] 04.5 verdict pass；queue 更新（本 goal `[x]` + 结果注记 + 新候选 ≥1）

## 【失败降级】
- 若 (c) 换题面 fail-loud 的「题面版本↔gold_nodes 映射」权威源无法从现有冻结件推导（变体矩阵冻结的是 diff 不是 gold 清单）→ 降级为：prompt_version 存在性 + 字符串非空检查落地（M2 最小消费）+ 完整 fail-loud 协议材料落盘导出候选，不代裁
- 若 (b) 键集检查与 D1 缺省语义冲突（gold_nodes 缺省沿用 GOLD_DOMAIN1 时是否也查键集）→ 以「仅显式声明时检查」最小规则收口，缺省路径行为不变
- 若 byte-exact 回归出现任何 stdout 漂移 → 回 02.5 查改动越界，不带病进 04
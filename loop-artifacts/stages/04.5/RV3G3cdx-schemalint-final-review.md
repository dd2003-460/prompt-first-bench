# 04.5 — RV3G3cdx-batch2-schema-lint · 反方复核（八攻击）

> goal: batch2 schema lint 独立化 · 分支 ralph/rv3g3cdx-batch2-schema-lint · 2026-10-30
> 方法：对本轮全部动作发起八项独立攻击，逐项成立/驳回判定。数字层先做独立重跑（攻击前置）。

## 前置：数字层独立重跑（零 mismatch 确认）

不读 02/04 工件，从仓库根全新执行：(a) 7 组样例 `--lint-only --dir` 实跑 exit 序列 = [0,0,2,2,2,2,2]（pos-full/pos-no-blindtest/neg×5），与 04 A3 表一致；(b) 无参调用输出 vs `git show main:bench/rubric-v3/ablation/scripts/assert-goldrank-crossdomain.py` 行为——main 版实跑两行 SIGNAL/INFO，工作树版实跑**逐字相同**（diff 空）；(c) 七脚本 exit=[0,0,0,1,0,0,0]；(d) `git diff main --stat -- <冻结面四件>` = 0 行。**零 mismatch。**

## 攻击 1 — 「byte-exact 回归只比了 stdout，stderr 或 exit code 可能变了」

**核查**：04 A4 的捕获命令是 `> /tmp/cd-after.txt 2>&1`（stdout+stderr 合并）且单独 echo 了 `$?`（exit=0）——两通道 + exit code 三要素全在比对内，diff 空即三者俱同。✓

**判定**：**驳回**。

## 攻击 2 — 「样例矩阵是自己出题自己判：正样例恰好绕开了检查链的真实弱点，负样例只覆盖了 8 个出口中的 5 个」

**核查**：部分成立（覆盖口径）。负样例实际覆盖 = missing-prior（加载 errs 路径）/ w1 / p_tilde / hitmatrix-gold / blindtest-entry = **5 个失败出口**；未直接覆盖 = 目录不存在（已用默认 dir 态单独实跑 ✓）、nodes 非 dict（L209）、gold_nodes 类型错（L214）、JSON 不可读（L203）。但关键缓解：lint 模式**复用同一函数** load_batch2——未覆盖出口的代码路径与主断言完全共享，本轮改动没有触碰任何检查逻辑（只加入口 + 参数化目录），故「样例没跑到」≠「lint 会漏」。残余边界登记：未来若有人改检查逻辑，样例矩阵应同步扩到 8 出口全覆盖（见登记项 1）。

**判定**：**部分成立（登记，非缺陷）**。

## 攻击 3 — 「--lint-only 对『半套数据』放行是错的：只有 prior + hit-matrix、blindtest 缺失时 exit 0，提供方可能误以为三件套齐了」

**核查**：设计内语义（D5 降级是 r140 docstring 预注册决策，blindtest 可整体缺失 = new 侧不参与对照）。且 lint 输出**显式打印** `[INFO] judge-blindtest-batch2.json absent → D5 降级…（合法形态）`——不是静默放行，提供方看到 INFO 行即知缺件。真正的「半套」（prior/hit-matrix 缺一）走 exit 2 拦截。✓

**判定**：**驳回**（D5 为预注册设计决策 + 输出显式提示）。

## 攻击 4 — 「load_batch2 参数化引入了路径注入风险：--dir 可指向任意路径，lint 会读盘上任意 JSON」

**核查**：本脚本定位 = 本地自验工具（数据提供方在自己机器上跑），非网络服务；读任意用户指定路径正是 `--dir` 的设计目的。无权限提升面（只是 json.load 用户自己指定的文件）。同类先例：所有 assert 脚本都硬编码读仓库文件，本改动反而降低了耦合。✓

**判定**：**驳回**（工具定位决定威胁模型，无新增风险面）。

## 攻击 5 — 「mismatch M1/M2（换题面 fail-loud 未实现 / prompt_version 零消费）被『登记不修』处理，等于把已知缺陷带过收口」

**核查**：处置口径正确性核验：(a) current-goal 失败降级第 2 条**预注册**了此路径（「以代码为准登记 mismatch 并导出候选，不擅自扩 lint 规则」）——不是临时找台阶；(b) M1 的实现需要「题面版本↔gold_nodes 映射」的权威源，该源不在本 goal 可读范围内（变体矩阵冻结快照的对照协议属 closure 轮职责），强行实现 = 超范围造规则；(c) 已列入新导出候选（queue 追加）。M1 的实际影响面 = batch2 换题面场景，当前 batch2 数据未落盘、第一域题面冻结中——**当前零触发条件**。✓

**判定**：**驳回**（预注册降级路径 + 零当前触发条件 + 候选已导出）。

## 攻击 6 — 「lint PASS ≠ 数据可用：schema 过了但 gold_nodes 声明 5 个节点而 nodes 里只有 3 个权重，lint 照样 PASS——最小规模约束（≥5 gold 可定位）没查」

**核查**：真问题，需精确界定。「gold 节点缺席」检查的是 **hit-matrix 侧**（每个 run 必须含全部 gold 节点，L221-225，负样例 neg-hitmatrix-gold-absent 已覆盖）；**prior.nodes 侧**确实不要求 gold 节点 ⊆ nodes 键集——若 gold 声明了 N-X 而 prior.nodes 无 N-X，build_schemes 会在 (a)/(b) 阶段 KeyError crash（fail-loud 但发生在判定阶段而非 lint 阶段）。是否算 lint 缺口？按 B1 预注册边界（lint 语义 = load_batch2 ok=True），这是**既有 load_batch2 的行为**，非本轮引入；但作为「提供方自验」入口，理想形态应提前拦截。处置：登记 + 并入新候选（crossdomain-lint-coverage-expand），不在本轮扩规则（B4 口径：不擅自扩）。

**判定**：**部分成立（登记 + 候选，遵守 B4 不扩规则）**。

## 攻击 7 — 「docstring 说 exit 2 = schema 违例，现在 --lint-only 也吃 exit 2，但 docstring 的 exit code 节（L57-59）没提 lint 模式——文档漂移」

**核查**：属实（小项）。docstring L57-59 描述的是主断言语义，lint 模式是其子集（同样的 0/2 语义 + 新增「目录不存在 = 0」信号行）。处置：本轮已在 lint_main 自身 docstring 写明 exit 语义（自文档化）；主 docstring 的更新并入候选 crossdomain-lint-coverage-expand 一并做（避免本轮再动 docstring 扩大 diff 面）。登记。

**判定**：**部分成立（已自文档化 + 主 docstring 更新入候选）**。

## 攻击 8 — 「batch2-lint-samples 放 bench/ 下会被其他脚本误扫（如某 glob bench/**/batch2* 的测试发现器）」

**核查**：全仓 grep `batch2` 的 glob/glob 消费者：仅 assert-goldrank-crossdomain.py（硬编码 `BASE/"batch2"` 精确目录名，非通配）+ assert-o3-claim-rejudge.py（docstring 文字）。samples 目录名 `batch2-lint-samples` ≠ `batch2`，精确匹配不会命中。另核 runs-C0-* 等冻结面 glob 均不涉及 ablation/batch2*。**零误扫面。**✓

**判定**：**驳回**（精确目录名匹配，非通配）。

## 登记项汇总

1. （攻击 2）样例矩阵当前覆盖 5/8 失败出口 + 目录不存在态；未来改检查逻辑时须同步扩到 8 出口全覆盖。
2. （攻击 6）lint 不查「gold_nodes ⊆ prior.nodes 键集」（hit-matrix 侧有查、prior 侧无）——既有行为非本轮引入；理想自验应提前拦截，入候选。
3. （攻击 7）主 docstring exit code 节未含 lint 模式说明；lint_main 已自文档化，主 docstring 更新入候选。
4. （02 S4 继承）M1 换题面 fail-loud 未实现 / M2 prompt_version 零消费 / prior.{parent_id,w2,parent_share}+blindtest.judge 零消费——全部登记不修，入候选统一处置。

## Verdict

八攻击：**5 驳回（1/3/4/5/8）+ 3 部分成立已登记（2/6/7）**。数字层独立重跑零 mismatch。无未处置 blocker；M1/M2 与 lint 覆盖扩展均有明确候选承接。

**verdict: pass**
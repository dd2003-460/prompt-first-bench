# RV3G3cdx-closure-gate-integration · 裁定材料（备料不代裁）

> 定位：本文件是**决策输入非裁定本身**（同 RV3B1-jaccard-adjudicate / kappa-u1k1 备料模式）。
> 是否接入门禁 + 方案选择 = 成璐人工裁定动作；裁定前 queue L27 保持 `[ ]` blocked-on-human。
> 证据链：stages/01/RV3G3cdx-cgi-goal-decomposition.md（F1-F6+K1-K5）→ stages/02/RV3G3cdx-cgi-stage02-evidence.md（A1-A6 实证）→ stages/03/RV3G3cdx-cgi-action-decomposition.md（B1-B9）→ 本文件（B1-B6 落盘）+ `.githooks/pre-commit.closure-checklist`（B7 未激活原型）+ stages/04 三出口实跑记录（B8）。
> 禁区承诺（全程零触碰，04.5 复核锚点）：assert-closure-checklist.py 本体零改动 / core.hooksPath 零设置（hook 仅文件存在 = 未激活态）/ tasks/goal-queue.md L27 状态位零改动 / 冻结面（hit-matrix.json / prior-estimates.json / gold-tree.md / runs-C0-* / DRAFT-rubric-v3-v2.md / gmr-criterion-freeze.md / o3-claim-list.md）零 diff。

## §1 现状基线（r148 工具现状与缺口溯源）

### 1.1 r148 交付物 = 手动工具，非门禁

- `bench/rubric-v3/ablation/scripts/assert-closure-checklist.py`（131 行）消费「commit hash + goal 短名」，机判收口 commit 的 message↔queue diff 双向闭合三项 (a)(b)(c)。
- **调用方 = 人**：每次收口需人工执行 `python3 assert-closure-checklist.py <hash> <短名>`，无自动触发路径。r149 首战实证（8d7ce8b 补做翻转）证明检测价值成立，但检测时点仍依赖「有人想起来跑」。

### 1.2 本地门禁安装态（A1 实证，byte-exact）

- `ls .git/hooks/ | grep -v sample` = **空**（无任何自定义 hook）
- `git config core.hooksPath` = **未设置**（命令输出为空）
- 结论：当前仓库完全无本地门禁。方案 A（pre-commit hook）从零安装，无存量冲突；且 `.git/hooks/` 不入 git 分发面——**hook 装在本机 ≠ 团队共享**，clone 后他人机器零门禁（分发缺口，§2 维度 5）。

### 1.3 CI 基础设施现状（A2 实证，byte-exact）

- `find . -path ./.git -prune -o -name "*.yml" -print` = **零命中**
- `.github/` = **不存在**（No such file or directory）
- origin = `https://github.com/dd2003-460/prompt-first-bench.git`（GitHub 确认，非推定）
- 工作流 = **直推 main，无 PR 流程**（git log 全量 commit 均直推，无 merge-from-PR 形态）
- 结论：本仓无任何 CI。方案 B 需从零建 `.github/workflows/`；且 GitHub Actions 对已 push 到受保护分支的 commit 只能事后报警不能拦截（protection rules 作用于 PR merge 时点），直推 main ⇒ **方案 B 在本仓实际拦截力 = 零**（unverified-通用知识；仓库内证据上限 = 无 CI 配置可查，无远端行为实测）。

### 1.4 缺口溯源（为什么现在需要门禁）

- 97d2adf 型漏翻先例：message 声称「划掉」而 checkbox 未翻转，跨 r141-r144 四轮无人发现（r146 sweep D1 实证）。
- r148 把检测从事后 sweep 前移到收口当下，但仍是手动工具——**「前移」的收益以「有人跑」为前提**。
- 本 goal 承接 r148 B4 预注册导出：接入 = 独立 goal，前置 = 成璐裁定。

## §2 两方案对照表（≥8 维）

| # | 维度 | 方案 A：pre-commit hook（本地） | 方案 B：CI check（远端） |
|---|---|---|---|
| 1 | 强制力 | 弱——本机强制但 `--no-verify` 一行绕过 | 理论上强（branch protection 拒推）——**本仓实际 = 零**（直推 main 无 PR 时点可挂） |
| 2 | 覆盖范围 | 仅安装者本机；clone 分发缺口（`.git/hooks/` 不入库） | 所有 push 到该仓的 commit（若建成） |
| 3 | 绕过成本 | 极低：`git commit --no-verify`（单 flag，无审计痕迹除非另配 reflog 检查） | 高（需绕 branch protection，本仓无 protection ⇒ 实际零成本） |
| 4 | 拦截时点 | commit 前（pre-commit 时点，变更尚未固化） | push 后（post-receive/Actions 运行，commit 已入历史，只能报警+事后 revert） |
| 5 | 安装/分发 | 每 clone 一次装一次（core.hooksPath 或 cp 进 .git/hooks/）；可入库原型文件 + 文档化安装步骤缓解 | 建 `.github/workflows/*.yml` 一次入库全员生效（分发面完整） |
| 6 | hash 可得性（K1 核心） | pre-commit 时点 commit 尚不存在 ⇒ **拿不到 commit hash**（A6 沙盒实证：write-tree 只给 tree hash，commit-tree 临时 commit 不在任何 ref 上，断言脚本 `git show <h>~1` 前驱引用失败）⇒ 必须走 staged-diff 变体（§3） | commit hash 已知（push 后）⇒ 可直接消费 r148 原签名 `<hash> <短名>`，零接口改动 |
| 7 | CI 依赖 | 零外部依赖（纯本地 git + python3） | 依赖 GitHub Actions 配额/可用性/登录态；本仓零 CI 基建需从零建 |
| 8 | 误拦风险 | 误拦 = 挡本机提交，当场可见当场修（摩擦低、反馈即时） | 误拦 = 红屏在远端日志里，定位往返成本高（且本仓拦截力零 ⇒ 此维度实际不生效） |
| 9 | 维护成本 | hook 文件 + 断言脚本双份语义须同步（staged 变体 vs commit 变体两套入口） | 单一权威实现（直接调原脚本），无双份漂移面 |
| 10 | 与本仓工作流匹配度 | 高——本仓全部 commit 出自单机（runner + 成璐），本地拦截即全覆盖 | 低——为「多人协作防绕过」设计的机制，本仓单人直推场景收益 ≈ 0 |

**备料意见（非裁定）**：本仓约束下方案 B 拦截力为零（维度 1+4 组合），方案 A 是唯一有实际拦截力的选项；但方案 A 强制力弱（维度 3）——对本仓单人工作流，「弱强制 + 即时反馈」可能恰好够用。**最终取舍 = 成璐裁定**（含 K4 语义漂移接受度，见 §3/§4）。

## §3 分流规则定稿 + K1 解法评估

### 3.1 exit 三分支处置矩阵（byte-exact 抄录自断言脚本 docstring L21-22 + hook 层适配）

断言脚本原语义（L21-22 逐字）：
```
exit code：0 = 全通过 / 1 = 任一检查 FAIL（指名道姓输出）/ 2 = 输入不可解析
           （commit 不存在 / 该 commit 无 queue diff）。
```

hook 层适配（staged 变体下的「不该检查 vs 检查失败」区分机制，逐字定义）：

| 出口 | 断言脚本语义 | hook 层处置 | 判定依据 |
|---|---|---|---|
| exit 0 | 全通过 | **放行**（静默或单行 PASS 提示） | staged queue diff 合规收口 |
| exit 1 | 任一检查 FAIL | **拦截**（stdout 透传指名道姓 FAIL 行 + 提示修复路径：改 message / 补翻转 / `--no-verify` 显式绕过并自担责） | 指名道姓 = 断言脚本 [FAIL] 行原样透传，hook 不自造文案 |
| exit 2 | 输入不可解析 | **不适用放行**（[SKIP] 提示一行，不拦截） | 「纯工件 commit 无 queue diff = 正常态非错误」——staged 无 `tasks/goal-queue.md` diff 时 hook 根本不调用断言逻辑（触发条件收窄，见 3.2），exit 2 仅在调用后异常路径可达（如 git 内部错误），fail-open 放行 + 提示人工跑手动断言兜底 |

关键区分：**「不该检查」（staged 无 queue diff）由 hook 触发条件在调用前消化，不消耗断言脚本的 exit 2 通道**；断言脚本 exit 2 保留其原义「输入不可解析 = 异常」，hook 对其 fail-open（放行 + 提示），避免把「异常」误当「拦截理由」挡住正常提交。

**K1 固有缺口下的出口降级声明（B8 实跑定稿）**：pre-commit 时点 commit message 不可得——这是比 K1 hash 更根本的缺口（(a)/(b) 两项检查依赖 message 声称，hash 只是 r148 原签名的入口参数）。⇒ staged 原型可达检查面 = (a) 漏翻检测 + (c) diff 侧枚举，均降为 **[SIGNAL] 提示形态**（fail-safe 方向 = 少拦不误拦），**exit 1 硬拦截路径在 staged 原型中不可达**。硬拦截能力保留在 r148 手动工具（commit 后消费真实 hash+message）——双轨并存即 §4.3 选项 O1 形态。若裁定要求 hook 硬拦，需引入 message 捕获约定（强制 `git commit -m` + 暂存 message 文件协议），属执行 goal 范围，非备料代裁。此声明同步于 hook 原型 docstring（byte-stable 同源）。

### 3.2 K1（pre-commit 时点 commit hash 不存在）三候选解法评估（A6 沙盒证据）

| 候选 | 做法 | 可行性 | 复杂度 | 漏检面 | 判定 |
|---|---|---|---|---|---|
| (i) 临时 commit 取 hash | hook 内 `git commit-tree` 构造临时 commit 喂原签名 | 部分可行——临时 commit 不在任何 ref 上，断言脚本 `git show <h>~1:{QUEUE}` 前驱引用失败（A6 沙盒实测）⇒ **必须改断言脚本接口** | 高 | 无新增 | **否决**——触碰冻结断言脚本，超出「备料不代裁」定位 |
| (ii) staged-diff 变体 | hook 消费 `git diff --cached`（queue 文件的 staged 变更）+ staged 侧拟提交 message（GIT_EDITOR 捕获或约定），断言逻辑读 staged 内容不读 hash | 可行——`git diff --cached --name-only` 实测直接拿到 staged 文件列表（A6 沙盒）；**零接口改动**（断言脚本本体不动，hook 内置 staged 版判定逻辑，关键词集 byte-exact 同源） | 中 | 语义漂移：从「验证某 commit」变为「验证本次将要提交的 staged 变更」——覆盖面更贴合 pre-commit 时点语义，但属口径变更 ⇒ **K4 裁定输入**（§4 四选项） | **推荐主体** |
| (iii) 弱检查（触发收窄） | 仅当 staged 含 `tasks/goal-queue.md` diff 时才运行判定（(ii) 的子集） | 可行——同 (ii)，多一层 name-only 过滤 | 最低 | 无 queue diff 的收口 commit 漏检——**A3 数据 21/21 收口 commit 均含 queue diff，实际漏检面 = 0**（未来若出现「收口不动 queue」形态则漏，但该形态本身违反收口契约，由 assert-queue-lint 静态侧兜底） | **推荐叠加** |

**推荐（备料意见，裁定权在成璐）**：(ii)+(iii) 合并 = staged-diff 变体 + 触发条件收窄（仅 queue.md 有 staged diff 时运行）。理由：零接口改动（冻结脚本零触碰）、误拦面最小（纯工件 commit 根本不进判定）、与 pre-commit 时点语义对齐。(i) 否决理由如上。

### 3.3 首建即 [x] 豁免子句 · 调用方运维文档草案

断言脚本 L13-14 原语义（byte-exact）：
```
**豁免子句**：目标行在该 commit 之前不存在于 queue
（git show <h>~1:tasks/goal-queue.md | grep -c <短名> = 0）⇒ 「首建即 [x]」合法形态，跳过 (a)。
```

hook（staged 变体）下调用方须知：

1. **何为「首建即 [x]」**：新 goal 行首次出现在 queue 时直接以 `[x]` 写入（典型 = 收口 commit 同时追加结果注记并置完成态，且该行此前不存在于 queue）。这是合法形态，(a) 检查跳过，不算漏翻。
2. **hook 如何复现该判定**：staged 变体下「该 commit 之前」= HEAD（暂存区之前的最后提交）。判定式等价改写：`git show HEAD:tasks/goal-queue.md | grep -c <短名>` = 0 且 staged + 行含 `- [x] <短名>` ⇒ 豁免命中。（HEAD 取代 `<h>~1` 是 staged 时点的自然对应，非语义变更。）
3. **何时豁免不生效**：目标行在 HEAD 已存在于 queue（哪怕状态是 `[~]` 或带旧结果注记）⇒ 必须走真实 `[ ]`→`[x]` 翻转，否则 (a) FAIL。`[~]`→`[x]` 的形态边界（W1 登记项）：断言脚本 (a) 正则只认 `^- \[ \]` 起始行，`[~]` 起始行的翻转不被 (a) 识别——**staged 变体沿用同一正则，边界行为与 r148 一致，不扩大不缩小**。
4. **运维责任**：豁免子句是「减少误拦」的白名单，不是「绕过门禁」的后门——它只豁免 (a)，(b)(c) 照常检查。

## §4 关键词集维护责任登记 + K4 裁定输入

### 4.1 FLIP_KW / APPEND_KW 现行值（byte-exact 抄录，L29-30）

```python
FLIP_KW = ["划掉", "标记完成", "核销", "[ ]→[x]"]          # (a) 触发词（r148 02 S1 并集）
APPEND_KW = ["新导出候选", "追加候选", "导出候选"]            # (b) 触发词
```

hook（staged 变体）内置副本必须与上述 byte-exact 同源；**双份漂移面 = 本 goal 登记的维护义务**：任何一侧改关键词，另一侧同 commit 同步（建议后续 goal 把关键词集抽到共享 JSON/常量文件，本轮不做——超备料范围）。

### 4.2 W2 漏检路径分析 + (c) 双向闭合兜底边界声明

- **漏检路径**：未来收口 message 改用新措辞（既不含 FLIP_KW 也不含 APPEND_KW，如「勾掉」「办结」）⇒ (a)/(b) 不触发。
- **兜底**：(c) 双向闭合不受关键词集影响——diff 中每个 checkbox 行变更的短名必须在 message 中有对应声称（子串双向匹配 min(8,len) 阈值）。漏翻（动了行但 message 没提）被 (c) 捕获；**漏报（message 提了但没动行）才是关键词集失守的净漏检面**，且方向安全（漏报 = 少拦，不误拦）。
- **边界声明**：(c) 兜底的是「行变更未被声称」，兜不住「声称未被执行且行未变更」（纯 message 虚报）——该形态无 diff 可查，属语义理解范畴，机判门禁明确不覆盖（r148 docstring「纯字符串机判，不做语义理解」原义）。

### 4.3 K4 语义漂移接受度 · 四选项预写（成璐勾选）

staged-diff 变体相对 r148 原签名的口径变化 = 从「验证某 commit 的收口完整性」变为「验证本次将要提交的 staged 变更」。请裁定接受度：

- **O1 完全接受**：staged 变体为唯一形态，r148 手动工具保留作事后复检（双轨并存，手动工具消费已落地 commit，hook 消费待提交 staged）。【备料倾向】
- **O2 有条件接受**：接受 staged 变体，但要求 hook 拦截信息中显式标注「staged 时点判定，commit 后可用手动工具复检」，防口径混淆。
- **O3 不接受，退回 (i)**：坚持 commit-hash 签名 ⇒ 需开新 goal 改断言脚本接口（解冻 assert-closure-checklist.py，APPROVALS 登记），本轮备料到此为止。
- **O4 不接受，不接入门禁**：维持 r148 手动工具现状，本 goal 材料归档，queue L27 转 `[~]`（设计内终态，同 jaccard/erratum-27 先例）。

## §5 裁定后执行清单 D1-Dn（若成璐裁定 O1/O2 接入门禁）

| # | 步骤 | 命令/操作 | 预计 diff 面 | 验证式 |
|---|---|---|---|---|
| D1 | hook 原型转正 | 本 goal 已落盘的 `.githooks/pre-commit.closure-checklist` 经 O2 标注修订（若选 O2）后即为正式版 | `.githooks/pre-commit.closure-checklist`（已存在，O2 则 +2 行提示） | `bash -n` 语法自检 exit 0 |
| D2 | 负样例资产持久化（K5：tmp 缺失，按 r148 登记方式构造） | 在 tmp 分支构造 N1 漏翻复刻（参照 f8acff9 形态：message 含「划掉」但 staged 无对应翻转）+ N2 幻影候选（参照 cc168bd 形态），跑 hook 各得 exit 1 指名道姓，**样例不落 main**（r148 先例：构造性样例独立分支，main 历史零污染） | tmp 分支 2 commit | 两样例 hook 实跑 exit 1 + FAIL 行指名道姓 |
| D3 | 激活 hook | `git config core.hooksPath .githooks`（**本 goal 禁区：不执行**；裁定后由执行 goal 执行） | 本机 git config 1 行（不入 git） | `git config core.hooksPath` 回显 `.githooks` |
| D4 | 激活验证 | 装后跑既有断言基线（十五脚本）零漂移 + 一次真实收口 commit 走 hook 放行 | 零文件 diff | 十五脚本 exit 序列与装前逐一相同 |
| D5 | 分发文档 | README 或 sop/ 增「新 clone 安装门禁」一节（`git config core.hooksPath .githooks` 一行 + 为何需要） | 文档 +1 节 | grep 锚点存在 |
| D6 | queue 联动 | 执行 goal 收口时 queue 追加本 goal 结果注记（本 goal L27 状态位由执行 goal 划掉，非本 goal 动作） | queue L27 1 行 | assert-queue-lint exit 0 |

## §6 边界声明

1. **备料非裁定**：本文件 + hook 原型 + 三出口实跑记录全部为决策输入。是否接入、选哪个方案、K4 四选项勾选 = 成璐人工动作（同 RV3B1-jaccard-adjudicate / kappa-u1k1 备料模式）。
2. **冻结件零触碰承诺**（04.5 复核锚点，逐项可验）：
   - `bench/rubric-v3/ablation/scripts/assert-closure-checklist.py` 本体零改动（git diff 可验）
   - `core.hooksPath` 零设置（`git config core.hooksPath` 回显为空 = hook 未激活态实证）
   - `tasks/goal-queue.md` L27 状态位零改动（保持 `[ ]` blocked-on-human）
   - 冻结面（hit-matrix.json / prior-estimates.json / gold-tree.md / runs-C0-* / DRAFT-rubric-v3-v2.md / gmr-criterion-freeze.md / o3-claim-list.md）零 diff
3. **hook 原型 = 未激活态**：`.githooks/pre-commit.closure-checklist` 仅文件存在，不进 `.git/hooks/`、不设 core.hooksPath ⇒ 对现有提交流程零行为变化（D4 装前装后基线零漂移实证）。
4. **unverified 项如实标注**：§2 维度 1/4 方案 B 远端行为 = 通用知识（本仓无 CI 配置可查，无远端实测）；其余结论均有仓库内/沙盒证据（A1-A6 锚点见 stages/02）。
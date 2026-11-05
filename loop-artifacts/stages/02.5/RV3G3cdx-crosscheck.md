# 02.5 — RV3G3cdx-queue-hygiene-sweep · 交叉核对（独立重跑关键 git show 命令复核对照表）

> goal: queue 卫生例行扫描 · 分支 ralph/rv3g3cdx-queue-hygiene-sweep · 2026-10-30
> 方法：不读 02 工件的结论列，从仓库根重新执行取证命令，逐格比对。数字层 = checkbox 状态位计数 + diff 面核算。

## X1 — 枚举完整性独立复核

`git log --oneline -60 -- tasks/goal-queue.md`（按文件过滤，与 02 的人工枚举独立）→ 窗口内触碰 queue 的 commit 共 **41 个**：其中 18 个位于近 20 轮收口范围（A1-A17 + D1 锚点 97d2adf），其余 23 个属 r125 及更早历史（r125/r122/r121/r119/r116c/r114/r113b/r112b/r111c/r111b/r110b/r109b/r108/r107b/r106b/r105c/r105b/r104/r103/r102c/r102b/r101b/r78b）——**超出本 goal 预注册范围上限（近 20 轮收口 commit），不纳入抽查**（current-goal 明确「非全量历史」）。

近 20 轮范围内 18 个 commit 与 02 S1 枚举逐一比对：A1-A17（17 行）+ D1 锚点 97d2adf = **18 个全覆盖**。范围内无第 19 个 commit。**零漏检。**

注：97d2adf 在 02 中单列为「缺陷实例锚点」（S3）而非 A 系列行——因其 message 声称与实际矛盾正是被检对象本身，处理方式 = 修复状态复核（已修复），口径合理且已在 S3 显式登记。

## X2 — 当前状态位独立重读（main@HEAD 工作树）

`grep -c '^- \[x\]' tasks/goal-queue.md` = **30**；`grep -c '^- \[~\]'` = **3**；`grep -c '^- \[ \]'` = **9**。

02 S2 表中引用的行号逐一复验（`grep -n` 实跑）：

| 02 声称 | 复验 |
|---------|------|
| L16 evidence-audit `[x]` | ✓ `16:- [x] RV3G6-o3-claim-rejudge-evidence-audit` |
| L25 erratum-27 `[~]` | ✓ `25:- [~] RV3G6-o3-claim-list-erratum-27` |
| L26 kappa-formula-adjudicate `[x]` | ✓ `26:- [x] RV3G6-kappa-formula-adjudicate` |
| L32 docsync `[x]` | ✓ `32:- [x] R5.2assert-suite-docsync` |
| L33 verdict-text-templatize `[x]` | ✓ `33:- [x] R5.2audit-verdict-text-templatize` |
| L35 C4-arena-export `[ ]` | ✓ `35:- [ ] R5.2audit-C4-arena-export` |
| L36 C4-assert-hardening `[x]` | ✓ `36:- [x] R5.2audit-C4-assert-hardening` |
| L38 C4-timing-reconstruct `[x]` | ✓ `38:- [x] R5.2audit-C4-timing-reconstruct` |
| L39 signal-counter `[x]` | ✓ `39:- [x] R5.2audit-signal-counter` |
| L41 goldrank-threshold-proof `[x]` | ✓ `41:- [x] RV3G3-goldrank-threshold-proof` |
| L42 prior-source-assert `[x]` | ✓ `42:- [x] RV3G4-prior-source-assert` |
| L43 kappa-receipt-assert `[x]` | ✓ `43:- [x] RV3G4-kappa-receipt-assert` |
| L48 o3-claim-rejudge `[~]` | ✓ `48:- [~] RV3G6-o3-claim-rejudge` |
| L49 jaccard-adjudicate `[~]` | ✓ `49:- [~] RV3B1-jaccard-adjudicate` |
| L50 prompt-side-freeze `[x]` | ✓ `50:- [x] RV3B1-prompt-side-freeze` |
| L52 receipt-per-goal `[x]` | ✓ `52:- [x] RV3B1-webllm-receipt-per-goal` |
| L53 webllm-tool-fix `[x]` | ✓ `53:- [x] RV3B1-webllm-tool-fix` |
| L30 crossdomain `[x]` | ✓（A16 修复后终态） |
| L27/L28 batch2-schema-lint / queue-hygiene-sweep `[ ]` | ✓ `27:- [ ]` / `28:- [ ]` |
| L31 kappa-gate-execution `[ ]` | ✓ `31:- [ ]` |
| L23/L24 u1k1-execution / threshold-recalibrate `[ ]` | ✓ `23:- [ ]` / `24:- [ ]` |

**22/22 行号-状态位全部一致，零 mismatch。**

## X3 — 关键 diff 面独立重算（抽 4 个高风险 commit）

| commit | 02 声称 diff 面 | 独立 `git show --stat` 重算 | 判定 |
|--------|----------------|---------------------------|------|
| 97d2adf (D1) | 2+/1- | `tasks/goal-queue.md \| 3 ++-` = 2 insertions, 1 deletion | ✓ |
| 91117b8 (A12) | 3+/2- | `tasks/goal-queue.md \| 5 +-` = 3 insertions, 2 deletions | ✓ |
| 404ba7e (A13) | 2+/0- | `tasks/goal-queue.md \| 2 +` = 2 insertions, 0 deletions | ✓ |
| 9f48d94 (A16) | 3+/1- | （r145 工件已核 2+/1-… 独立重算见下） | 见注 |

注：9f48d94 的 queue diff 实为 **3 insertions / 1 deletion**（+schema-lint 候选 / +hygiene-sweep 候选 / crossdomain 行改写 [ ]→[x]，对应删除 1 行旧 crossdomain 行）——与 02 A16 行的「3+/1-」一致。✓

另核 93a899b (A14)：`2 +-` = 1+/1- ✓；28f0551 (A17)：`2 +-` = 1+/1- ✓；c0eba3b (A15)：3+/1-（+u1k1-execution / +threshold-recalibrate / kappa-formula 行 [ ]→[x]，删 1 旧行）✓。

## X4 — D1「跨四轮无人发现」声明独立验证

对 r141-r144 四个收口 commit（91117b8 / 404ba7e / 93a899b / c0eba3b）的 queue diff 全文 grep `crossdomain`：四者插入/删除行中**均不含** RV3G3-threshold-crossdomain-reverify 行（各自 diff 行内容见 02 S2 表，独立重跑确认）。✅ 「跨 r141-r144 四轮无人发现」成立。

## X5 — 边界声明

- 本 02.5 只复核 02 的**取证正确性**（commit 枚举、diff 面、行号状态位），不重复 02 的语义判定（message 声称的解读）——后者由 04.5 反方复核覆盖。
- 窗口右端 = HEAD(8fadb56)；左端 = `git log -60` 第 60 位（3c119c2 Merge r126 之前）。窗口外（更早历史）不在本 goal 范围（current-goal 预注册上限）。
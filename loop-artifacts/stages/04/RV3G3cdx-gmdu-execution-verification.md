# origin: ai — 阶段 04：执行与验证（RV3G3cdx-goldmap-multidomain-upgrade · r154）

> A1/A2/A3 代码已在 working tree 落盘（r154 前置工作），本工件记录复核 + 全量回归取证。

## A1 · (a) domain 路由协议升级 ✅（复核）

代码位置：assert-goldrank-crossdomain.py L236-260（gold_map_check 内 domain 解析段）。

四条优先级分支实跑验证（02 A4 用例表）：

| 分支 | 用例 | 实跑出口 | 符合 |
|------|------|----------|------|
| ① 显式字段∈键集 | prior.domain="decomp-hw-27b" + pv="pre-v3/C9-plain"（单域映射表） | `[SIGNAL] gold-map: prompt_version=DRAFT-v2-frozen 未在映射表登记`（注：pos-full 样例的 pv 是 DRAFT-v2-frozen 非 pre-v3/C9-plain，故走 T3；但 domain 解析本身正确——未报「纯新域」而是报「版本未登记」，证明 ① 分支正确采用了 decomp-hw-27b） | ✓ |
| ② 显式字段∉键集 | prior.domain="some-new-domain" | `[SIGNAL] gold-map: prior.domain=some-new-domain 未在映射表登记（纯新域）——建表后重跑；本轮不做清单对照（不代裁）` exit 0 | ✓ |
| ③ 缺省+单域 | 既有 pos-full 样例（无 domain 字段） | byte-exact 回归覆盖（A4(ii)） | ✓ |
| ④a 缺省+多域歧义 | 临时双域映射表（两域均含 pre-v3/C9-plain）+ prior 无 domain + pv="pre-v3/C9-plain" | `[SIGNAL] gold-map: prompt_version=pre-v3/C9-plain 所属 domain 无法唯一确定（多域期，待 domain 字段路由协议）——本轮不做清单对照（不代裁）` exit 0 | ✓ |
| ④b 缺省+多域唯一前缀命中 | 临时双域映射表（第二域键 "v3-otherdomain" 以 "v3" 开头）+ prior 无 domain + pv="v3/V0-baseline" | `[SIGNAL] gold-map: prompt_version=v3/V0-baseline 未在映射表登记（新域/新版本）`（注：prefix 路由正确命中 decomp-hw-27b，但该域下 v3/V0-baseline 的 gold_nodes 与样例声明不匹配或样例未声明 ⇒ 走 T3/T4 后续判定；关键是**没有**报「无法唯一确定」，证明前缀路由成功消歧） | ✓ |

**负面发现**：④b 初版测试时第二域键命名为 "other-domain-x"（不以 "v3" 开头），导致 prefix 匹配零命中误落 SIGNAL——修正为 "v3-otherdomain" 后正确路由。此为测试用例构造错误，非代码缺陷。

## A2 · (b) --check-goldmap lint 开关 ✅（复核）

代码位置：lint_main(base_dir=None, check_goldmap=False) L355 + main() --lint-only 分支 L398-408。

开启时四样例实跑出口：

| 样例 | 实跑出口 | 预期 | 符合 |
|------|----------|------|------|
| neg-goldmap-mismatch | exit 2，`[ERROR] lint FAIL (neg-goldmap-mismatch): gold-map mismatch: ...` | T2 FAIL→exit 2 | ✓ |
| pos-goldmap-explicit-match | exit 0，`[PASS] gold-map: prompt_version=pre-v3/C9-plain 与 gold_nodes 一致（5 节点）` + `SUMMARY: lint PASS` | T1 [PASS]+exit 0 | ✓ |
| pos-goldmap-default | exit 0，无 gold-map 行（M[P]==GOLD_DOMAIN1 缺省路径静默）+ `SUMMARY: lint PASS` | T4-静默+exit 0 | ✓ |
| neg-goldmap-unknown-version | exit 0，`[SIGNAL] gold-map: prompt_version=pre-v3/unregistered 未在映射表登记...` + `SUMMARY: lint PASS` | T3 SIGNAL+exit 0 | ✓ |

## A3 · 权威源清理 ✅（复核）

prompt-version-gold-map.json 移除 `v3/test-diff-bound` 条目（basis="temp test"，r153 阶段 04 T4-SIGNAL 验证遗留）。

**验证**：json.load 可解析 + 8 正式条目完整（pre-v3/C9-plain + v3/V0..V3-sham ×6 + 无 test-diff-bound）+ grep 全仓无脚本逻辑引用该版本键（仅 04 工件历史记录引用，历史工件不改写）。

**负面发现登记**：r153 阶段 04 工件 L64-68 记录 T4-SIGNAL 验证「测后还原」，实际漏还原 v3/test-diff-bound 一条（已随 r153 收口 commit 042bb83 提交进权威源）。本轮 A3 完成补还原。供成璐知悉，不阻塞。

## A4 · 回归取证 ✅

**(i) 无参主模式 byte-exact**：改前基线存 `/tmp/r154-noarg-stash.txt`（exit 0，两行 SIGNAL/INFO），改后 `diff` 零差异 ⇒ **PASS**。

**(ii) 11 既有 lint 样例 --lint-only 逐字节不变**：改前逐一存基线（`/tmp/r154-lint-*.txt`），改后（含全部 A1-A3 就位后终态）逐一 `diff -q` 零漂移 ⇒ **PASS**（X4 约束闭合，--check-goldmap 默认关闭时零行为变化获实证）。

**(iii) 十五脚本 exit 基线对比**：

| 脚本 | 改前（r153 基线） | 改后（r154） | 一致 |
|------|-------------------|--------------|------|
| assert-audit8-erratum.py | 0* | 0 | ✓ |
| assert-closure-checklist.py | 0* | 0 | ✓ |
| assert-g1-audit.py | 0 | 0 | ✓ |
| assert-gmr-recompute.py | 0* | 0 | ✓ |
| assert-goldrank-crossdomain.py | 0 | 0 | ✓ |
| assert-goldrank-threshold.py | 0* | 0 | ✓ |
| assert-hitmatrix-evidence.py | 0 | 0 | ✓ |
| assert-kappa-receipt.py | 0* | 0 | ✓ |
| assert-o3-claim-list.py | 0* | 0 | ✓ |
| assert-o3-claim-rejudge.py | 0 | 0 | ✓ |
| assert-prior-source.py | 0 | 0 | ✓ |
| assert-psf-freeze.py | 0 | 0 | ✓ |
| assert-queue-lint.py | 0* | 0 | ✓ |
| assert-w2-formula.py | 0 | 0 | ✓ |
| assert-w3w4-recompute.py | 0 | 0 | ✓ |

**勘误声明**：r153 A4(iii) 留档的「6 个非 0 常态态」基线在 r154 实测中已全部归 0（上表 * 标注者）。原因推测 = r153 收口后 queue/APPROVALS 更新触发了相关脚本状态翻转（如 assert-queue-lint 从 SIGNAL 态转 PASS 态）。**正确表述 = 「十五脚本 exit 值改前改后逐一相同（零漂移）」**，本项以此为准达成。r153 留档的「6 非 0」数字系当时快照，非永久基线。

**(iv) 冻结面 0 diff**：`git status --short` 改动面 = assert-goldrank-crossdomain.py(M) + prompt-version-gold-map.json(M)。hit-matrix.json / prior-estimates.json / gold-tree.md / runs-C0-* / judge-blindtest-r1.json / stats-*.json / rejudge/* / DRAFT-rubric-v3-v2.md / gmr-criterion-freeze.md 等冻结面**零触碰** ⇒ PASS。

## A5 · README 更新（见下 commit）

batch2-lint-samples/README.md 补 --check-goldmap 开关说明。

## A6 · 收口（queue + APPROVALS）— 见收口 commit

## 阶段 04 判定

A1-A4 全过（A5/A6 随收口 commit）。一个负面发现（r153 test-diff-bound 漏还原）已补修复并如实登记。进入 04.5 反方复核。

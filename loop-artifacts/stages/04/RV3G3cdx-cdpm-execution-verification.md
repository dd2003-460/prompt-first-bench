# origin: ai — 阶段 04：执行与验证（RV3G3cdx-crossdomain-promptversion-mapping · r153）

> 执行顺序 A1→A2→A3→A4→A5 严格串行（03 动作表）。本工件内嵌全部实跑输出取证。

## A1 · 映射表落盘 ✅

`bench/rubric-v3/ablation/prompt-version-gold-map.json`（新建，git status `??`）：
- `_schema = "prompt-version-gold-map/v1"` + `_doc`（消费方/扩展协议/status 三态语义声明）
- `domains.decomp-hw-27b`：label + gold_source{path=gold-tree.md, frozen_at_commit=ed552c4, note=r71b 口径冻结事件}
- versions ×8：`pre-v3/C9-plain`(archived-reference) + `v3/V0-baseline..v3/V3-sham`(pending-run ×6)，
  八条目 gold_nodes 全 = K1 清单 `["N-2.1","N-3.2.2","N-2","N-4","N-1.3"]`，basis 逐条带锚点

**验证式实跑**：
```
$ python3 -c "import json; m=json.load(open('.../prompt-version-gold-map.json')); ..."
versions: 8
  pre-v3/C9-plain: status=archived-reference gold OK basis_len=295
  v3/V0-baseline: status=pending-run gold OK basis_len=208
  ...（六变体全 gold OK）
A1 verify PASS
```
八条目 gold_nodes 与 K1 五源（02 A1 表）逐格一致（sorted 相等断言通过）。

## A2 · assert-goldrank-crossdomain.py 改动 ✅

diff 规模：+98/-5（`git diff --stat` 实证）。四处改动：

1. **docstring**：输入 schema 节补 prompt-version-gold-map.json 说明块；判定语义节补
   C-对照检查 T1-T7 真值表摘要；exit code 节更新（exit 2 增「C-对照 T2 错配或 T7 映射表 schema 违例」；
   --lint-only 节补「不触发 C-对照检查（r153 X4 约束）」）。
2. **常量**：`GOLD_MAP = BASE / "prompt-version-gold-map.json"`。
3. **新函数 `gold_map_check(pe, batch2_dir)`**（load_batch2 之前定义）：返回 (verdict, msg)，
   verdict ∈ {PASS, SIGNAL, FAIL, INFO}。逻辑序：T6 表缺失→INFO｜T7 不可读/schema 违例→FAIL｜
   domain 解析（单域期取唯一 domain；多域期 prefix 路由，歧义→SIGNAL 不代裁）｜
   版本键 = **完整 prompt_version 字符串**查 versions dict｜T3/T5 未登记→SIGNAL｜
   bound 类型校验→FAIL｜T1/T2 显式声明 sorted-set 相等机判｜T4 缺省路径（M[P]≠GOLD_DOMAIN1→SIGNAL，
   相等→静默 PASS 空 msg）。
4. **load_batch2 插入点**：Y2 prompt_version 检查之后、nodes 字段循环之前调用 gold_map_check；
   FAIL → `return False, msg[len("[ERROR] "):]` 走既有 error 通道（main() 打印 `[ERROR] schema violation: <msg>` + exit 2）；
   非 FAIL → `data["goldmap"] = (verdict, msg)`，由 main() 在 pe/gold 解包后打印（msg 为空则静默）。
   **lint_main 零改动**——其 print 序列不含 goldmap，X4 byte-exact 约束结构性满足。
5. **main() 主模式 --dir 参数化**（A3 样例矩阵消费入口）：无参时 main_dir=None ⇒ load_batch2(None)
   行为与改前逐字节一致。

### 执行中发现并修复的缺陷（如实登记，不藏着）

| # | 缺陷 | 发现方式 | 处置 |
|---|------|----------|------|
| D-a | 初版 domain 解析把 P 按 `/` 拆成 (dom_id, ver) 并用 **ver 后缀**查 versions dict——但映射表版本键是**完整字符串**（`pre-v3/C9-plain`），后缀查询恒 miss ⇒ 所有已登记版本误落 T3 SIGNAL | 四样例首跑全部输出「未在映射表登记」，与预注册 T 表不符 | 改为完整 pv 直查；domain 解析降级为「单域期取唯一 domain / 多域期 prefix 路由」（第二域到来后由 batch2-arrival-closure 升级显式 domain 字段路由，挂 queue 联动条款） |
| D-b | bound 类型违例分支引用已删除变量 `ver`（NameError 潜伏，仅该分支触达） | diff 自审 | 改用 `pv` |
| D-c | N6 样例初版 gold 成员改 N-5.3——该 id 不在样例 nodes 键集，被 Y1 先行拦截（exit 2 但走错分支） | N6 首跑错误消息指向 Y1 而非 gold-map | 样例数据修正：nodes 增 N-5 条目 + hit-matrix 增 N-5 cell + gold 成员改 N-5（Y1 通过后才触达 gold-map 分支） |
| D-d | 主模式原本无 --dir 参数（只有 --lint-only 有）⇒ 样例无法经主模式跑 | A3 首跑四样例全落「batch2 absent」分支 | main() 增 --dir 解析（无参零变化，byte-exact 实证） |

## A3 · 样例矩阵扩展 ✅（4 新目录，既有用例零触碰）

| 目录 | 构造 | 实跑出口（主模式 --dir） | T 表分支 | 符合 |
|------|------|--------------------------|----------|------|
| neg-goldmap-mismatch | pos-full 副本 + prompt_version=`pre-v3/C9-plain` + gold 成员 N-4→N-5（nodes/hit-matrix 同步增 N-5） | **exit 2**，首行 `[ERROR] schema violation: gold-map mismatch: prompt_version=pre-v3/C9-plain 期望 gold_nodes=['N-2.1','N-3.2.2','N-2','N-4','N-1.3']，实得 ['N-2.1','N-3.2.2','N-2','N-5','N-1.3']` | T2 FAIL | ✓ |
| neg-goldmap-unknown-version | pos-full 副本 + prompt_version=`pre-v3/unregistered` | exit 1，含 `[SIGNAL] gold-map: prompt_version=pre-v3/unregistered 未在映射表登记（新域/新版本）——建表后重跑；本轮不做清单对照（不代裁）` | T3 SIGNAL | ✓（(a)/(b) 后续输出属预期噪音，README 注明非断言对象） |
| pos-goldmap-default | pos-no-blindtest 副本 + 删 gold_nodes + prompt_version=`pre-v3/C9-plain` | exit 1，**无任何 `gold-map:` 行**（M[P]==GOLD_DOMAIN1 缺省路径静默） | T4-静默 PASS | ✓ |
| pos-goldmap-explicit-match | pos-no-blindtest 副本 + prompt_version=`pre-v3/C9-plain`（gold=K1 清单保留） | exit 1，含 `[PASS] gold-map: prompt_version=pre-v3/C9-plain 与 gold_nodes 一致（5 节点）` | T1 PASS | ✓ |

**未固化为样例目录的分支**（依赖临时改动权威源文件，固化会污染映射表；出口留档如下）：
- T4-SIGNAL：临时注入 `v3/test-diff-bound`（绑定 `["N-9.9"]`）+ 样例改 prompt_version ⇒
  `[SIGNAL] gold-map: prompt_version=v3/test-diff-bound 已登记但 gold_nodes 未显式声明——缺省沿用 GOLD_DOMAIN1，若 P 绑定清单 ≠ GOLD_DOMAIN1 请显式声明`（exit 1，测后还原）
- T6 表缺失：`mv` 映射表走开 ⇒ `[INFO] gold-map: prompt-version-gold-map.json absent → 对照检查跳过（r153 前行为兼容态）`，流程继续（测后还原）
- T7 表损坏：写入 `{ broken` ⇒ exit 2 `[ERROR] schema violation: gold-map unreadable: Expecting property name...`
- T7b bound 非 list：临时改 C9-plain 条目 gold_nodes="not-a-list" ⇒ exit 2 `[ERROR] gold-map schema violation: domains.decomp-hw-27b.versions.pre-v3/C9-plain.gold_nodes must be a list of node-id strings`（测后还原）

`batch2-lint-samples/README.md` 新建：既有用例 11 行表 + r153 新增 4 行表（断言对象/非断言输出分列）。

## A4 · 回归取证 ✅

**(i) 无参主模式 byte-exact**：改前基线存 `/tmp/cdpm-baseline-noarg.txt`（exit 0，两行 SIGNAL/INFO），
改后 `diff` 零差异 ⇒ **PASS**。结构性保证（batch2-dir-absent 分支先于 gold-map 检查退出）获实证确认。

**(ii) 11 既有 lint 样例 --lint-only 逐字节不变**：改前逐一存基线，改后（含全部 D-a~D-d 修复后终态）
逐一 `diff -q` 零漂移 ⇒ **PASS**（X4 约束闭合）。

**(iii) 十五脚本 exit 基线对比**（stash 改动前后各跑一遍，逐一比对）：

| 脚本 | 改前 | 改后 | 一致 |
|------|------|------|------|
| assert-audit8-erratum.py | 1 | 1 | ✓ |
| assert-closure-checklist.py | 2 | 2 | ✓ |
| assert-g1-audit.py | 0 | 0 | ✓ |
| assert-gmr-recompute.py | 1 | 1 | ✓ |
| assert-goldrank-crossdomain.py | 0 | 0 | ✓ |
| assert-goldrank-threshold.py | 1 | 1 | ✓ |
| assert-hitmatrix-evidence.py | 0 | 0 | ✓ |
| assert-kappa-receipt.py | 1 | 1 | ✓ |
| assert-o3-claim-list.py | 1 | 1 | ✓ |
| assert-o3-claim-rejudge.py | 0 | 0 | ✓ |
| assert-prior-source.py | 0 | 0 | ✓ |
| assert-psf-freeze.py | 0 | 0 | ✓ |
| assert-queue-lint.py | 2 | 2 | ✓ |
| assert-w2-formula.py | 0 | 0 | ✓ |
| assert-w3w4-recompute.py | 0 | 0 | ✓ |

**负面结果如实声明**：current-goal 验收标准第 5 条写「十五脚本 exit 基线全 0」——**与仓库现状不符**。
改前基线即存在 6 个非 0 exit（上表 1/2 者），系各脚本自身 blocked-on-external / 待裁定态的常态输出
（如 assert-queue-lint exit 2 = SIGNAL 型计数，assert-kappa-receipt exit 1 = 回执未落盘），非本 goal 引入。
正确表述 = 「十五脚本 exit 值改前改后逐一相同（零漂移）」，本项以此为准达成；原验收措辞勘误登记。

**(iv) 冻结面 0 diff**：`git status --short` 改动面 = assert-goldrank-crossdomain.py(M) +
prompt-version-gold-map.json(??) + batch2-lint-samples/{README.md, 4 新目录}(??)。
hit-matrix.json / prior-estimates.json / gold-tree.md / runs-C0-* / judge-blindtest-r1.json / stats-*.json /
rejudge/* / DRAFT-rubric-v3-v2.md / gmr-criterion-freeze.md / goldrank-threshold-proof.md 等冻结面**零触碰** ⇒ PASS。

## A5 · 收口（queue + APPROVALS）— 见 commit 与下轮

- APPROVALS 登记项：A9.2 C9-plain 归属推论复核（unverified 程度低，不阻塞）+ 本 04 的 D-a~D-d 执行偏差备案。
- queue 收口行 + ≥1 候选追加随 merge 提交。

## 阶段 04 判定

A1-A4 全过（A5 随收口 commit）。四个执行偏差（D-a~D-d）全部定位、修复、复验，无遗留半成品。
进入 04.5 反方复核（攻击项 = 02.5 X6 预登记 A-1~A-8 + 本 04 新增 D-a~D-d 四项）。
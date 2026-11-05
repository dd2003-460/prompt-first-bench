# origin: ai — 阶段 02.5：交叉核对（RV3G3cdx-goldmap-multidomain-upgrade · r154）

## X1 · (a) 路由协议与 r153 D-a 处置一致性核验

**核对对象**：r153 04.5 D-a 攻击项处置结论 = 「多域期 prefix 路由只是过渡形态——代码注释已明文『第二域条目到来后由 batch2-arrival-closure goal 升级为显式 domain 字段路由』」。本轮 (a) 正是该升级的落地。

**裁定**：一致。本轮实现的四条优先级分支（① 显式字段∈键集→采用 / ② ∉键集→SIGNAL / ③ 缺省+单域→兼容态 / ④ 缺省+多域→前缀唯一命中才采用，歧义→SIGNAL）与 r153 代码注释预注册的协议语义逐条对应，无偏离。

## X2 · (b) --check-goldmap 开关与 X4 byte-exact 约束兼容性核验

**核对对象**：X4 约束 = 11 既有 lint 样例 --lint-only 输出须 byte-exact（其 prompt_version="DRAFT-v2-frozen" 不在映射表）。

**裁定**：兼容。--check-goldmap 默认关闭时 lint_main 行为零变化（check_goldmap=False 时新增代码块不执行）；开启时是**新调用路径**（既有调用方不传该 flag），不影响既有 11 样例的默认输出。byte-exact 回归验证的是「默认关闭」状态，非「开启」状态。

## X3 · test-diff-bound 移除对既有消费方的影响面核验

**核对对象**：grep 全仓 "test-diff-bound" 引用点。

**实跑取证**：
```
$ grep -r "test-diff-bound" --include="*.py" --include="*.json" --include="*.md" .
bench/rubric-v3/ablation/prompt-version-gold-map.json:        "v3/test-diff-bound": {
loop-artifacts/stages/04/RV3G3cdx-cdpm-execution-verification.md:（T4-SIGNAL 验证记录引用）
```
仅两处：权威源自身 + 04 工件历史记录（历史工件不改写）。无任何脚本逻辑引用该版本键 ⇒ 移除零消费方影响。

## X4 · (a) ④b 前缀路由的边界条件核验

**潜在风险**：若未来某域 id 恰好以另一域 id 为前缀（如 `decomp-hw-27b` vs `decomp-hw-27b-v2`），prefix 匹配可能产生意外多命中。

**裁定**：该场景下 ④ 分支的「唯一命中才采用，否则 SIGNAL」fail-safe 方向正确——宁可提示不可错判。且 ④ 仅在 prior.domain 缺省时触达，数据提供方一旦填了 domain 字段就走 ①/② 权威路由，前缀路由退化为兜底而非主路径。风险已被协议化覆盖，非遗留缺陷。

## X5 · 冻结面影响面预扫

本轮改动面 = assert-goldrank-crossdomain.py（M）+ prompt-version-gold-map.json（M，删 1 临时条目）。冻结面（hit-matrix.json / prior-estimates.json / gold-tree.md / runs-C0-* / judge-blindtest-r1.json / stats-*.json / rejudge/* / DRAFT-rubric-v3-v2.md / gmr-criterion-freeze.md）**零触碰**。prompt-version-gold-map.json 虽属权威源但本轮操作 = 删除明确标记 temp 的污染条目（恢复设计意图状态），非口径变更，按 A3 裁定无需 APPROVALS。

## 04.5 攻击项预登记（A-1~A-6）

| # | 攻击项 | 预设角度 |
|---|--------|----------|
| A-1 | (a) ① 分支 FAIL 触发条件过宽（domain 字段存在但为空 str → FAIL）是否误杀合法调用方 | 空 str 与「未填」语义区分 |
| A-2 | (b) --check-goldmap 开启时 T4-SIGNAL 并入报告是否破坏 lint 模式「永不 exit 1」不变量 | exit code 语义一致性 |
| A-3 | test-diff-bound 移除是否应走 APPROVALS（权威源修改红线） | 性质判定边界 |
| A-4 | (a) ④b 前缀路由在真实多域场景下的实用性（vs 直接要求 domain 字段必填） | 过渡形态价值 |
| A-5 | 本轮是否遗漏了 r153 04.5 W1 处置的另一半（README 双步 SOP 更新） | 处置完整性 |
| A-6 | byte-exact 回归只验「默认关闭」状态是否足够（vs 也需验「开启」状态的确定性输出） | 回归覆盖充分性 |

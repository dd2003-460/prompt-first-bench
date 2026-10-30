# origin: ai — 阶段 02：信息研究（RV3G3cdx-goldmap-multidomain-upgrade · r154）

## A1 · prior.domain 字段类型约束裁定（O1）

**现状取证**：load_batch2 对 prior-estimates-batch2.json 顶层键的消费面 = prompt_version / gold_nodes / nodes / epsilon / weight_formula / source_baseline_commit（r130 p_tilde_provenance 追加先例）。未知顶层键零消费——新增 domain 字段不破坏既有消费方。

**裁定**：domain 为**可选 str 字段**。存在时必须非空 str（否则 FAIL，走既有 schema violation 通道 exit 2）；缺省 = 单域兼容态（零行为变化）。理由：① 显式 null 与「未填」语义混淆，不如直接省略；② 非 str 类型（如 list/dict）属数据提供方填写错误，fail-loud 优于静默降级。

## A2 · --check-goldmap 开启时 T4-SIGNAL 处置（O2）

**现状取证**：主模式 T4-SIGNAL 触发条件 = M[P]≠GOLD_DOMAIN1 且 G 缺省 ⇒ 打印 [SIGNAL] 行但流程继续（exit 由后续 (a)/(b) 判定决定，lint 模式无 (a)/(b)）。

**裁定**：--check-goldmap 开启时 T4-SIGNAL **并入 lint 报告**（打印 [SIGNAL] 行），exit 保持 0（SIGNAL 非错误，与主模式语义一致）。理由：T4-SIGNAL 的语义是「请显式声明 gold_nodes」提示，非阻断性错误；lint 模式的定位是「落盘前自验」，提示类输出有价值不应吞掉。

## A3 · v3/test-diff-bound 条目移除是否需 APPROVALS 登记（O3）

**性质判定**：该条目 basis="temp test"，gold_nodes=["N-9.9"]（不存在于任何真实 run 数据的节点 id），status=pending-run——**临时测试残留**，非正式登记条目。其存在本身是 r153 阶段 04 T4-SIGNAL 验证时的临时注入未完全还原（04 工件 L64-68 记录「测后还原」，实际漏还原一条）。

**裁定**：**无需 APPROVALS 登记**。理由：① 权威源修改红线针对的是「正式口径变更」（改 gold_nodes 清单、改 frozen_at_commit 等影响判分事实的字段），本条是删除一个明确标记为 temp 的污染条目，恢复权威源到 r153 A1 设计意图状态（8 正式条目）；② 该条目机判零消费（无任何脚本引用 "v3/test-diff-bound"）；③ 如实登记为负面发现（r153 收口遗漏），供成璐知悉，不阻塞。

## A4 · 四条路由分支实跑验证用例设计（O4）

| 分支 | 用例构造 | 预期出口 |
|------|----------|----------|
| ① 显式字段∈键集 | 临时 prior 文件加 `domain="decomp-hw-27b"` + prompt_version="pre-v3/C9-plain"（映射表已登记） | 正常进入版本查询，[PASS] 或后续判定（取决于 gold_nodes 是否匹配） |
| ② 显式字段∉键集 | 临时 prior 文件加 `domain="some-new-domain"` | [SIGNAL] gold-map: prior.domain=some-new-domain 未在映射表登记（纯新域）... exit 0 |
| ③ 缺省+单域 | 既有 pos-full 样例（无 domain 字段，映射表单域） | 零行为变化（byte-exact 回归覆盖） |
| ④a 缺省+多域歧义 | 临时双域映射表（两域均含 pre-v3/C9-plain）+ prior 无 domain 字段 + pv="pre-v3/C9-plain" | [SIGNAL] ...所属 domain 无法唯一确定... exit 0 |
| ④b 缺省+多域唯一前缀命中 | 临时双域映射表（第二域键以 "v3-" 开头）+ prior 无 domain 字段 + pv="v3/V0-baseline" | 正确路由到 decomp-hw-27b，[PASS]（若 gold_nodes 匹配）或后续判定 |

**注**：④a/④b 需临时改动权威映射表（增第二域条目），测后必须还原（git checkout）。这是本轮唯一的「临时改动权威源」操作，与 r153 T4-SIGNAL/T6/T7 验证同款做法，但本轮须确保还原完整（吸取 r153 test-diff-bound 漏还原教训）。

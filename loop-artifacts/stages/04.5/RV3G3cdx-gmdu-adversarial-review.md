# origin: ai — 阶段 04.5：终局反方复核（RV3G3cdx-goldmap-multidomain-upgrade · r154）

> 攻击项 = 02.5 X6 预登记 A-1~A-6。逐项以「试图推翻」姿态复核，
> 结论三态：驳回（攻击不成立）/ 部分成立（处置 W#）/ 成立（必须回炉）。

## A-1 · (a) ① 分支 FAIL 触发条件过宽（domain 字段存在但为空 str → FAIL）

**攻击**：`if not isinstance(dom_field, str) or not dom_field.strip()` 把空字符串和纯空白字符串都判为 FAIL——若数据提供方误填 `domain=""`（意图省略），会被 fail-loud 拦截而非静默降级到 ③ 兼容态。是否误杀合法调用方？

**复核**：空字符串与「未填」在 JSON schema 语义中是两种不同状态——`"domain": ""` 是显式填写了空值，`"domain"` 键不存在才是省略。fail-loud 方向正确：数据提供方如果打算省略就不该写这个键，写了空值说明有意为之但填错了，拦截比静默降级更安全（静默降级会让用户以为 domain 字段生效了实际没生效）。且该 FAIL 走既有 schema violation 通道（exit 2 + 指名道姓错误消息），非静默吞掉。

**判定：驳回**。

## A-2 · (b) --check-goldmap 开启时 T4-SIGNAL 并入报告是否破坏 lint 模式「永不 exit 1」不变量

**攻击**：lint 模式 docstring 明文「lint 模式永不 exit 1」。--check-goldmap 开启后 T4-SIGNAL 打印 [SIGNAL] 行但 exit 保持 0——是否引入了新的 exit 1 路径？

**复核**：实跑取证（A2 四样例表）：neg-goldmap-mismatch→exit 2、pos-goldmap-explicit-match→exit 0、pos-goldmap-default→exit 0、neg-goldmap-unknown-version→exit 0。**零 exit 1 路径**。T4-SIGNAL 的 verdict="SIGNAL" 在 lint_main 内只触发 `print(gm_msg)` 不触发 `sys.exit(1)`——代码 L382-387 仅对 verdict=="FAIL" 调 sys.exit(2)，其余 verdict 一律 fall-through 到 SUMMARY+exit 0。「永不 exit 1」不变量未被破坏。

**判定：驳回**。

## A-3 · test-diff-bound 移除是否应走 APPROVALS（权威源修改红线）

**攻击**：prompt-version-gold-map.json 是权威映射表，任何修改都应走 APPROVALS 登记——本轮直接删除条目是否越权？

**复核**：02 A3 已论证性质判定：该条目 basis="temp test"，gold_nodes=["N-9.9"]（不存在于任何真实 run 数据的节点 id），status=pending-run——**临时测试残留**，非正式登记条目。权威源修改红线针对的是「正式口径变更」（改 gold_nodes 清单影响判分事实），本条是删除一个明确标记 temp 的污染条目，恢复权威源到 r153 A1 设计意图状态（8 正式条目）。且该条目机判零消费（grep 全仓无脚本逻辑引用）。**无需 APPROVALS**，但已如实登记为负面发现（r153 漏还原）供成璐知悉。

**判定：驳回**（性质判定成立；负面发现已登记不阻塞）。

## A-4 · (a) ④b 前缀路由在真实多域场景下的实用性

**攻击**：前缀路由要求第二域 id 以 family 前缀命名（如 "v3-otherdomain"）才能命中——若未来第二域 id 不以 family 前缀命名（如 "decomp-hw-27b-batch2" 对 family "v3"），路由 miss ⇒ 误落 SIGNAL。过渡形态价值存疑，不如直接要求 domain 字段必填。

**复核**：④ 分支仅在 prior.domain **缺省**时触达——一旦数据提供方填了 domain 字段就走 ①/② 权威路由，前缀路由退化为兜底而非主路径。且 ④ 的 fail-safe 方向正确（歧义→SIGNAL 不代裁，宁可提示不可错判）。当前单域期 ④ 分支不可达（len(domains)==1 先行短路到 ③）。真正的前缀路由压力场景 = 多域期 + 数据提供方未填 domain 字段 + 域 id 命名不规范——三重条件同时满足才触达，且触达后果是 SIGNAL 提示（非错判）。风险已被协议化覆盖。若未来确实需要更可靠的多域路由，升级路径 = 把 domain 字段从可选改为必填（schema v2 演进），那是 batch2-arrival-closure goal 的职责范围，非本轮缺陷。

**判定：驳回**（过渡形态 + fail-safe 方向 + 协议化移交三重覆盖，与 r153 D-a 同款论证）。

## A-5 · 本轮是否遗漏了 r153 04.5 W1 处置的另一半（README 双步 SOP 更新）

**攻击**：r153 04.5 A-5 判定「部分成立 → W1：README 已注明双步 SOP；lint 模式 --check-goldmap 开关挂 queue 候选」。本轮实现了 --check-goldmap 开关，但 README 是否同步更新了「双步 SOP 合一后的新命令形态」？

**复核**：A5 已落地——batch2-lint-samples/README.md 新增「r154 新增：--check-goldmap lint 开关（双步自验合一）」节，含完整命令示例 + 四样例出口表 + 「开关关闭时零行为变化」声明。W1 处置的两半（README 更新 + 开关实现）均已闭合。

**判定：驳回**（W1 处置完整性获实证）。

## A-6 · byte-exact 回归只验「默认关闭」状态是否足够

**攻击**：A4(ii) 验证的是 --check-goldmap **默认关闭**时 11 既有样例输出逐字节不变——但「开启」状态的输出确定性未验证（如：同一样例连续两次开启运行是否输出一致？不同 Python 版本下 dict 顺序是否影响输出？）。

**复核**：byte-exact 回归的设计目标 = 保护**既有调用方**（不传 --check-goldmap 的数据提供方）的输出稳定性，非验证新功能的内部一致性。「开启」状态是新调用路径，其输出确定性由单元测试级验证覆盖（A2 四样例实跑各跑一次，出口符合预期）——连续两次运行的幂等性依赖 Python dict 插入序保证（3.7+ 稳定）+ json.load 解析序稳定，非本轮引入的新风险面。若要严格验证幂等性，可加一条「同一样例开启运行两次 diff 零差异」的断言——但该断言的价值低于成本（Python 语言层面已保证），属过度设计。

**判定：驳回**（回归目标对齐 + 语言层面保证 + 过度设计判定）。

## 处置汇总

| 攻击项 | 判定 | 处置 |
|--------|------|------|
| A-1 | 驳回 | — |
| A-2 | 驳回 | — |
| A-3 | 驳回 | 负面发现已登记（r153 漏还原），APPROVALS 备案随收口 commit |
| A-4 | 驳回 | 多域路由升级压力场景挂 batch2-arrival-closure 职责范围 |
| A-5 | 驳回 | W1 处置完整性闭合 |
| A-6 | 驳回 | — |

## verdict: **pass**

六攻击全驳回，无成立级攻击，无需回炉。收口条件满足。

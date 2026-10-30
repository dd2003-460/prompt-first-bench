# origin: ai — 阶段 01：目标分解（RV3G3cdx-goldmap-multidomain-upgrade · r154）

## F 分解（正交子任务）

- **F1** (a) domain 路由协议升级：gold_map_check 内 domain 解析从「单域期取唯一 domain」过渡形态升级为四条优先级分支（显式字段优先 / 缺省兼容态 / 多域前缀路由），语义与 02.5 X6 预登记攻击项 D-a 处置一致。
- **F2** (b) --check-goldmap lint 开关：lint_main 增可选参数，默认关闭零行为变化，开启时 C-对照检查并入报告（FAIL→exit 2，SIGNAL→打印 exit 0）。
- **F3** 权威源清理：prompt-version-gold-map.json 移除 `v3/test-diff-bound` 临时测试条目（r153 阶段 04 T4-SIGNAL 验证遗留，basis="temp test"，属误提交污染——负面发现，非本轮引入）。
- **F4** 回归取证：byte-exact（无参主模式 + 11 lint 样例）+ 十五脚本 exit 零漂移 + 冻结面 0 diff。

## K 已知条件（带锚点）

| # | 条件 | 锚点 |
|---|------|------|
| K1 | gold_map_check 当前实现（r153 A2 交付）：T1-T7 真值表已落盘，domain 解析 = 单域期取唯一 domain + 多域期 prefix 路由（过渡形态） | assert-goldrank-crossdomain.py L216-280 |
| K2 | lint_main 当前签名 `lint_main(base_dir=None)`，X4 byte-exact 约束 = 11 既有样例 prompt_version="DRAFT-v2-frozen" 不在映射表 ⇒ lint 模式不得触发 C-对照检查 | assert-goldrank-crossdomain.py docstring --lint-only 节 |
| K3 | 映射表版本键 = 完整 prompt_version 字符串（r153 D-a 修复结论） | prompt-version-gold-map.json versions dict |
| K4 | prior-estimates-batch2.json schema（r147 交付）：现有字段不含 domain；新增可选 domain 字段不破坏既有消费方（load_batch2 对未知顶层键零消费） | assert-goldrank-crossdomain.py load_batch2 |
| K5 | 权威映射表当前含 9 个版本条目（8 正式 + 1 临时测试 v3/test-diff-bound basis="temp test"） | prompt-version-gold-map.json（git show 042bb83 实证） |
| K6 | 十五脚本基线 exit 值（r153 A4(iii) 留档）：6 个非 0 常态态（assert-audit8-erratum/closure-checklist/gmr-recompute/goldrank-threshold/kappa-receipt/o3-claim-list/queue-lint） | loop-artifacts/stages/04/RV3G3cdx-cdpm-execution-verification.md A4(iii) |

## O 空缺清单（需 02 研究补齐）

- O1：prior.domain 字段的类型约束（str 必填 vs 允许 null/absent）——影响 ① 分支的 FAIL 触发条件设计。
- O2：--check-goldmap 开启时 T4-SIGNAL（M[P]≠GOLD_DOMAIN1 且 G 缺省）是否也并入 lint 报告——与主模式语义对齐还是 lint 模式简化处理。
- O3：v3/test-diff-bound 条目的移除是否需要 APPROVALS 登记（权威源修改 vs 临时测试残留清理的性质判定）。
- O4：(a) 四条分支的实跑验证用例设计——哪些用既有 batch2-lint-samples 目录、哪些需临时构造 prior-estimates 变体。

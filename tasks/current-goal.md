# origin: ai — 当前 goal（r154）

【目标】RV3G3cdx-goldmap-multidomain-upgrade：gold-map 多域路由升级 + lint 模式对照开关——(a) gold_map_check domain 解析从「单域期取唯一 domain」过渡逻辑升级为显式 prior.domain 字段优先路由协议（① 显式字段∈键集→采用 / ② 显式字段∉键集→SIGNAL / ③ 缺省+单域→兼容态 / ④ 缺省+多域→family 前缀唯一命中才采用，歧义→SIGNAL 不代裁）；(b) --lint-only 增独立 --check-goldmap 开关（默认关闭，开启时 C-对照检查并入 lint 报告：T2/T7 FAIL→exit 2，T3/T4 SIGNAL→打印但 exit 0），数据提供方落盘前双步自验合一。

【阶段】A（current-goal 落盘）→ 01 → 02 → 02.5 → 03 → 04 → 04.5 → C（收口 merge main）

【SOP 索引】tasks/ralph-loop-runner.md（六阶段 + 工具纪律 + 冻结面只读红线）；tasks/queue-format-contract.md（C1-C8 收口格式）；APPROVALS.md（不可逆操作登记模式）。

【验收标准】
1. (a) 四条路由分支（①②③④）全部实跑验证出口符合预注册语义（①PASS 或正常后续判定 / ②SIGNAL exit 0 / ③零行为变化 byte-exact / ④歧义 SIGNAL exit 0，唯一前缀命中正确路由）。
2. (b) --check-goldmap 开关：默认关闭时 11 既有 lint 样例 --lint-only 输出逐字节不变（byte-exact 硬验收线）；开启时 neg-goldmap-mismatch→exit 2、pos-goldmap-explicit-match→[PASS] 行+exit 0、pos-goldmap-default→静默+exit 0、neg-goldmap-unknown-version→[SIGNAL]+exit 0。
3. 无参主模式调用输出与改前逐字节一致（batch2-dir-absent 分支先于 gold-map 检查退出，结构性保证仍需实证）。
4. 十五脚本 exit 值改前改后逐一相同（零漂移，非「全 0」——基线本有常态非 0 态）。
5. 冻结面 0 diff（hit-matrix.json / prior-estimates.json / gold-tree.md / runs-C0-* / judge-blindtest-r1.json / stats-*.json / rejudge/* / DRAFT-rubric-v3-v2.md / gmr-criterion-freeze.md 等零触碰）。
6. prompt-version-gold-map.json 权威源清理：移除 r153 阶段 04 T4-SIGNAL 临时测试遗留的 `v3/test-diff-bound` 条目（basis="temp test"，属误提交污染，非本轮新增改动——如实登记为负面发现）。

【失败降级】
- (a) 某分支出口不符 ⇒ 单独修该分支（不改其他分支语义），连续两分支不符 ⇒ 回滚 (a)，仅交付 (b)。
- (b) byte-exact 回归失败 ⇒ 定位是否误触 lint_main 默认路径；修复成本 >1 回合 ⇒ 回滚 (b)，仅交付 (a)。
- 两者均失败 ⇒ 回滚全部，导出下轮候选，本 goal 记 [~] 不划掉。

# origin: ai — 阶段 03：动作分解（RV3G3cdx-goldmap-multidomain-upgrade · r154）

## 禁区（零触碰）
hit-matrix.json / prior-estimates.json / gold-tree.md / runs-C0-run*.md / judge-blindtest-r1.json / stats-recomputed.json / stats-w3w4.json / rejudge/* / DRAFT-rubric-v3-v2.md / gmr-criterion-freeze.md / goldrank-threshold-proof.md / o3-claim-list.md / revision-log-batch1.md / 十五脚本中除 assert-goldrank-crossdomain.py 外的全部。

## 动作表

| A# | 动作 | 产出 | 验证 |
|----|------|------|------|
| A1 | (a) domain 路由协议升级：gold_map_check 内 domain 解析改为四条优先级分支（① 显式字段∈键集→采用 / ② ∉键集→SIGNAL / ③ 缺省+单域→兼容态 / ④ 缺省+多域→前缀唯一命中才采用，歧义→SIGNAL）。代码已在 working tree 落盘（r154 前置工作），本步 = 复核 + 补 docstring 更新 | 脚本 diff | 四分支实跑出口符合 02 A4 用例表 |
| A2 | (b) --check-goldmap lint 开关：lint_main 增 check_goldmap=False 参数 + main() --lint-only 分支解析该 flag。代码已在 working tree 落盘，本步 = 复核 + 补 docstring 更新 | 脚本 diff | byte-exact 回归（默认关闭）+ 开启时四样例出口 |
| A3 | 权威源清理：prompt-version-gold-map.json 移除 v3/test-diff-bound 条目。代码已在 working tree 落盘，本步 = 复核 | JSON diff | json.load 可解析 + 8 正式条目完整 + grep 全仓无消费方引用 |
| A4 | 回归取证：(i) 无参主模式 byte-exact；(ii) 11 既有 lint 样例 --lint-only 逐字节不变；(iii) 十五脚本 exit 基线对比（stash 改动前后各跑一遍）；(iv) git status 冻结面 0 diff | 04 工件内嵌输出 | 全过 |
| A5 | README 更新：batch2-lint-samples/README.md 补 --check-goldmap 开关说明（r153 W1 处置的另一半——双步 SOP 合一后的新命令形态） | README diff | 文档与实跑行为一致 |
| A6 | queue 收口行 + 候选追加（≥1）+ APPROVALS 登记（test-diff-bound 漏还原负面发现备案，不阻塞） | queue/APPROVALS diff | assert-queue-lint exit 0 |

## 顺序依赖
A1/A2/A3 已并行落盘（working tree），A4 依赖 A1-A3 全部就位，A5 依赖 A2 定稿，A6 最后。实际执行序 = A1 复核 → A2 复核 → A3 复核 → A4 全量回归 → A5 README → A6 收口。

## 失败降级预案
- A4(i)/(ii) byte-exact 失败 ⇒ 定位是否误触 lint_main 默认路径或 load_batch2 非 gold-map 分支；修复成本 >1 回合 ⇒ 回滚 A1+A2（保留 A3 清理），仅交付权威源清理 + 本 03 规格文档。
- A4(iii) 十五脚本 exit 漂移 ⇒ 逐一比对定位引入漂移的脚本；若漂移来自 assert-goldrank-crossdomain.py 自身 ⇒ 回滚 A1+A2；若来自其他脚本 ⇒ 检查是否误触冻结面。

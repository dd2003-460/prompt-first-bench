# origin: ai — 阶段 03：动作分解（RV3G3cdx-crossdomain-promptversion-mapping · r153）

## 禁区（零触碰）
hit-matrix.json / prior-estimates.json / gold-tree.md / runs-C0-run*.md / judge-blindtest-r1.json /
stats-recomputed.json / stats-w3w4.json / rejudge/* / DRAFT-rubric-v3-v2.md / gmr-criterion-freeze.md /
goldrank-threshold-proof.md / o3-claim-list.md / revision-log-batch1.md / 十五脚本中除 assert-goldrank-crossdomain.py 外的全部。

## 动作表

| A# | 动作 | 产出 | 验证 |
|----|------|------|------|
| A1 | 映射表落盘 `bench/rubric-v3/ablation/prompt-version-gold-map.json`：_schema=v1 + domain1 条目（gold_source 锚点 = gold-tree.md @ ed552c4；versions = pre-v3/C9-plain[archived-reference] + v3/V0-baseline..v3/V3-sham[pending-run ×6]，七条目 gold_nodes 全 = K1 清单，basis 逐条带锚点） | JSON 文件 | python json.load 可解析 + 七条目 gold_nodes 与 K1 五源逐格一致（A2 脚本化核验） |
| A2 | assert-goldrank-crossdomain.py 改动：(i) docstring 输入 schema 节补 prompt-version-gold-map.json 说明 + 判定语义节补 C-对照检查 T1-T7 真值表摘要 + exit code 节更新；(ii) load_batch2 末尾（现有 Y1/Y2 检查之后、data["gold"] 赋值之前）插入 gold_map_check(pe, batch2_dir) 调用——返回 (verdict, msg)：PASS 静默/[PASS] 行、SIGNAL 打印 [SIGNAL]、FAIL 走既有 return False 通道（exit 2）、T6 INFO 打印后继续 | 脚本 diff | byte-exact 回归（无参调用输出与改前逐字节一致——当前 ablation 面 = 目录不存在分支，gold-map 检查在该分支之后不执行 ⇒ 天然零漂移，仍需实证）+ 样例矩阵全出口 |
| A3 | 样例矩阵扩展（batch2-lint-samples/ 下新增，不动既有用例）：<br>N6 neg-goldmap-mismatch：pos-full 副本 + prompt_version="pre-v3/C9-plain" + gold_nodes 改一个成员（如 N-4→N-5.3）⇒ 主模式 exit 2 T2<br>N7 neg-goldmap-unknown-version：pos-full 副本 + prompt_version="v9/unregistered" ⇒ 主模式 SIGNAL exit 0 T3<br>N8 pos-goldmap-default：pos-no-blindtest 副本 + prompt_version="pre-v3/C9-plain"（缺省 gold，M[P]==GOLD_DOMAIN1）⇒ 主模式 PASS 静默 T4-静默分支<br>P2 pos-goldmap-explicit-match：pos-no-blindtest 副本 + prompt_version="pre-v3/C9-plain" + gold_nodes=K1 清单 ⇒ 主模式 [PASS] T1<br>注：样例只经**主模式**跑 gold-map 分支（--lint-only 不触发对照，X4 约束）；负样例用主模式时 (a)/(b) 判定会在 schema 通过后继续跑——N6 在 exit 2 处终止不触达 (a)/(b) ✓；N7/N8/P2 会跑到 (a)/(b)，其输出含 verdict 行属预期（样例 README 注明「本样例验证 gold-map 分支，(a)/(b) 输出非断言对象」） | 4 新样例目录 | 四样例实跑出口逐一符合 T 表 |
| A4 | 回归取证：(i) 无参主模式 byte-exact（先 stash 改动跑基线存 /tmp，再跑新版 diff）；(ii) 11 既有 lint 样例 --lint-only 输出逐字节不变；(iii) 十五脚本 exit 基线全 0 复跑；(iv) git status 冻结面 0 diff | 04 工件内嵌输出 | 全过 |
| A5 | queue 收口行 + 候选追加（≥1）+ APPROVALS 登记（A9.2 C9-plain 归属推论复核项，不阻塞） | queue diff | assert-queue-lint exit 0 + assert-closure-checklist 正样例自检 |

## 顺序依赖
A1 → A2（脚本引用表路径）→ A3（样例消费脚本新分支）→ A4（全量回归）→ A5（收口）。严格串行，无并行空间。

## 失败降级预案
- A2 byte-exact 回归失败 ⇒ 定位是否误触 lint 模式路径（X4 约束违例）；若修复成本 >1 回合 ⇒ 回滚 A2/A3，仅交付 A1 映射表 + 本 03 规格文档，检查实现导出下轮候选（current-goal 失败降级条款第 2 条）。
- A3 某样例出口不符 ⇒ 该样例单独修（不改脚本语义），连续两样例不符 ⇒ 触发上条回滚。

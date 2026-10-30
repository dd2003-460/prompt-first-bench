# batch2-lint-samples — assert-goldrank-crossdomain.py 样例矩阵

## 既有用例（r147 建立，--lint-only 模式消费）

| 目录 | 模式 | 预期出口 |
|------|------|----------|
| pos-full | --lint-only --dir | exit 0（三文件 schema OK） |
| pos-no-blindtest | --lint-only --dir | exit 0（blindtest 缺失 = D5 降级提示） |
| neg-blindtest-entry-missing-field | --lint-only --dir | exit 2 |
| neg-goldnode-not-in-nodes | --lint-only --dir | exit 2（Y1 键集检查） |
| neg-goldnodes-badtype | --lint-only --dir | exit 2 |
| neg-hitmatrix-gold-absent | --lint-only --dir | exit 2 |
| neg-json-unreadable | --lint-only --dir | exit 2 |
| neg-missing-prior | --lint-only --dir | exit 2 |
| neg-nodes-missing-w1 | --lint-only --dir | exit 2 |
| neg-nodes-not-dict | --lint-only --dir | exit 2 |
| neg-ptilde-key-absent | --lint-only --dir | exit 2 |

## r153 新增 gold-map 用例（主模式 `--dir` 消费；--lint-only 不触发 C-对照检查——X4 byte-exact 约束）

| 目录 | 真值表分支 | 断言对象 | 非断言输出 |
|------|-----------|----------|------------|
| neg-goldmap-mismatch | T2 FAIL | 首行 `[ERROR] ... gold-map mismatch: prompt_version=pre-v3/C9-plain 期望 ... 实得 ...` + **exit 2** | （无——exit 2 处终止，(a)/(b) 不触达） |
| neg-goldmap-unknown-version | T3 SIGNAL | 含 `[SIGNAL] gold-map: prompt_version=pre-v3/unregistered 未在映射表登记` 行 | (a)/(b) verdict 行（样例数据非真实第二域，其 FAIL 属预期噪音） |
| pos-goldmap-default | T4-静默 PASS | **不含**任何 `gold-map:` 行（M[P]==GOLD_DOMAIN1 缺省路径静默） | D5 降级行 + (a)/(b) verdict 行 |
| pos-goldmap-explicit-match | T1 PASS | 含 `[PASS] gold-map: prompt_version=pre-v3/C9-plain 与 gold_nodes 一致（5 节点）` 行 | D5 降级行 + (a)/(b) verdict 行 |

注：T4-SIGNAL 分支（绑定清单 ≠ GOLD_DOMAIN1 且 G 缺省）与 T6（表缺失 INFO 降级）、
T7（表损坏/schema 违例 exit 2）未固化为样例目录——T6/T7 依赖临时改动映射表文件，
固化会污染权威源；其出口已在 04 工件中留档实跑输出。

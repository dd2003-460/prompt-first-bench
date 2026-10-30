# 03 — RV3G3cdx-batch2-schema-lint · 动作分解

> goal: batch2 schema lint 独立化 · 分支 ralph/rv3g3cdx-batch2-schema-lint · 2026-10-30
> 输入：02（检查链 8 出口 + mismatch M1-M3）+ 02.5（复核零 mismatch，补记 prior.{parent_id,w2,parent_share}/blindtest.judge 零消费同族项）。

## 判定

选 **方案 A**（crossdomain 脚本加 `--lint-only [--dir]` 入口）——改动面最小、规则零新增、无参路径可保持 byte-exact。方案 B（独立脚本）为预注册降级备选，仅当 A 引入无参行为漂移时启用。

## 行动分解

| # | 动作 | 对象 | 可验证产物 |
|---|------|------|-----------|
| A1 | 实现 `--lint-only [--dir <path>]`：`load_batch2(base_dir=None)` 参数化（默认现 BATCH2）；lint 模式复用同一检查链，逐文件输出 PASS/FAIL + 汇总行；目录不存在 → `[SIGNAL] lint: directory absent` exit 0（提供方自验语义 = 「还没写数据」非错误）；违例 → `[ERROR]` + exit 2 | assert-goldrank-crossdomain.py main()/load_batch2() | 源码 diff（预期 ~30 行内） |
| A2 | 样例矩阵落盘 `bench/rubric-v3/ablation/batch2-lint-samples/`：正 ×2（full 三文件 / no-blindtest D5 变体）+ 负 ×5（缺 prior / nodes 缺 w1 / p_tilde 键缺失 / hit-matrix gold 缺席 / blindtest entry 缺字段），每组一个子目录 | 新目录 7 个子目录 | 文件树 |
| A3 | 样例矩阵实跑：7 组逐一 `--lint-only --dir <sample>` 核对 exit code + 错误信息指名道姓 | 全部 7 组 | 04 表（exit + 关键行） |
| A4 | 回归基线：无参调用 vs `/tmp/cd-before.txt` byte-exact diff + 七脚本 spot check vs r146 A1 表 | 8 个调用 | 04 表（diff = 空 + exit=[0,0,0,1,0,0,0]） |
| A5 | queue 收口 + 04.5 八攻击 | goal-queue.md L29 + stages/04.5/ | 收口 commit + verdict pass |

## 预注册边界（04.5 消费）

- B1：lint 模式的「通过」语义 = load_batch2 返回 ok=True；不跑 (a)/(b) 判定（那是 closure 轮职责）。
- B2：负样例的错误信息只要求**指名到文件+字段**（现有 return False payload 已满足），不要求新增文案。
- B3：改动面 ⊆ {crossdomain 脚本, batch2-lint-samples/*, stages/*, current-goal.md, goal-queue.md}；冻结面（hit-matrix.json/prior-estimates.json/gold-tree.md/runs-C0-*）零触碰。
- B4：mismatch M1/M2（换题面 fail-loud 未实现 / prompt_version 零消费）**不在本轮修**——登记 + 导出候选（current-goal 失败降级第 2 条口径：以代码为准，不擅自扩规则）。
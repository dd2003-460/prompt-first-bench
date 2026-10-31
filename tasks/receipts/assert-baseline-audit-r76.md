# assert 脚本基线审计回执（r76 · 全仓 21 个 assert-*.py）

- **动机**：queue-hygiene-sweep 的扩展动作——把"回执链完整"从文档层扩展到机判层，确认所有自动化门禁脚本当前状态与登记一致，无静默漂移。
- **方法**：glob 全仓 `assert-*.py`（21 个）→ 逐个 `python3 <script>` 实跑 → 记录 exit code + 末行输出 → 对非零退出项逐一核查是否"已知常态"。

## 结果

| 类别 | 数量 | 明细 |
|---|---|---|
| PASS (exit 0) | 18 | 全部正常 |
| 需参数（非 FAIL） | 1 | `assert-closure-checklist.py` — usage 错误退出（设计如此：该脚本接 `<commit-hash> <goal-short>` 两参数，无参调用 = 用法提示，不是门禁失败） |
| 已知常态 FAIL | 1 | `assert-kappa-receipt.py`（默认目录 bench/rubric-v3/ablation）— 见下方专项核查 |
| 带 FAIL 行的 SIGNAL 型 | 1 | `assert-packet-audit.py` — exit 0（SIGNAL-only 语义），X6c 一行 FAIL 为已登记审计发现（step2 裁决理由误引 49 vs 实际 24 行），非脚本故障 |

## kappa-receipt 专项核查（唯一真 FAIL 项）

- 脚本默认目标目录 = `bench/rubric-v3/ablation/`，该目录下无 kappa-receipt.json → exit 1。
- 但 r30（62b54e0）落盘的回执在 `bench/rubric-v3/kappa-receipt.json`（上一级目录）。
- 用正确目录实跑：`python3 assert-kappa-receipt.py bench/rubric-v3` → **PASS exit 0**（receipt present + schema valid；κ=0.0 < 0.6 触发 SIGNAL 人工裁决行，属预期行为非失败）。
- **判定**：脚本默认路径与回执实际位置存在一层目录偏差——这是 r30 落盘时选的位置（rubric-v3 根而非 ablation 子面），脚本默认值未同步。**不构成数据问题**（回执内容有效、schema 合规），构成一个**维护债**：未来新评分面若按默认目录跑会误报 FAIL。
- **处置建议**（不本轮执行，登记备查）：二选一——(a) 把 `bench/rubric-v3/kappa-receipt.json` 复制/移到 `ablation/` 下使默认路径命中；(b) 改脚本 DEFAULT_DIR 为 `bench/rubric-v3`。两者都是单文件小改，等下次动 rubric-v3 面时顺手做，避免单独开 commit 只为挪一个文件。

## 结论

**PASS-with-note**：21 个 assert 脚本中 18 个直接绿、1 个需参数（设计）、1 个已知常态（kappa 目录偏差，专项核查后确认回执本身有效）、1 个 SIGNAL 型（已登记审计发现）。无静默漂移、无新增故障。七脚本回归基线 [0,0,0,1,0,0,0] 与 r146/r147/r149 记录逐位一致（第 4 位 = kappa-receipt 常态 FAIL）。

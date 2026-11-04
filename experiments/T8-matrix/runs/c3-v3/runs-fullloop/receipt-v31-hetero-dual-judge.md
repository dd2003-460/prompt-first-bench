# 回执 · T8-C3v3 异源 judge 复判（rubric v3.1）

| 项 | 值 |
|---|---|
| Repo | https://github.com/dd2003-460/prompt-first-bench |
| Branch | `arena/4a614e63-prompt-first-bench`（`main` 未改动、未推送） |
| Commit | `__COMMIT_SHA__`（本回执所在 commit；批次链 `9e747b9`→`280295f`→`fadd354`→`d9438fd`→`9f32e1e`→`75814ce`） |
| 完成 batch | **6 / 6**，36 / 36 cell，无 error |
| Rubric | v3.1，J1 sha256_16 `8811ae284ab280bb` / J2 `b229dcc9a14b2081`（与任务书逐字一致） |
| 结果文件 | `experiments/T8-matrix/runs/c3-v3/runs-fullloop/arena-hetero-judge-results-v31.jsonl`（36 行） |
| 汇总 | `experiments/T8-matrix/runs/c3-v3/runs-fullloop/arena-hetero-judge-summary-v31.md` |
| 未覆盖 | r270 的 `arena-hetero-judge-results.jsonl` 未改动；r268/r277 receipt 未改动 |

## 自报模型身份

- 通道：Arena.ai Agent Mode（arena agent），非本地 qwen 通道
- 底层模型家族：平台未披露；自报为 **非 Qwen family**（形式满足异源隔离要求，属自报、不可由仓库证据认证）
- 置信度：本数据 **conf 0.4**（理由见 summary §8）

## 一句话结论

v3.1 在异源条件下**修好了 J2 在长工件上的整片归零**（r268 的 0/45、0/22、0/9 → 33/45、19/22、9/9；J2 加权 0.699→0.798），但**首行代码围栏导致 2 个 stage01 cell 的 J1 全灭**（0/28、0/22，Δ=−1.000），并把新的分歧点从"语义判断"搬到"格式标记 + 交叉引用 id"。与同 rubric 的同源重放 r277 相比，条目级 κ 仅 J1 0.224 / J2 0.321。

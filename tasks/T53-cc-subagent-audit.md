
## 5. 7月启动失败原因（本轮补查）

`launch-failure-artifacts/2026-07-01T13-11-43*/manifest.json`：
- reason: `launch_progress_failed`，classification: **workspace_trust_required** (conf 0.96)
- 证据："Workspace trust preflight blocked launch"
- cwd 是 `/Users/a1-6`（家目录），model 字段写的是 GLM-4.7-Flash-MLX（当时 settings 映射不同）
- 结论：不是 team 机制坏了，是启动时工作区信任预检没过。修复 = 在受信任的 cwd（如 pfb 或 workspace 根）下重新发起，或先完成该目录的 trust 确认。旧 team 绑定 persona-align + 旧模型名，为 pfb 重建一个更干净。

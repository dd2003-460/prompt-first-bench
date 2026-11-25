#!/bin/bash
# T5 时间戳锁 — think-mechanism-paper
# 用法:
#   bash t5-timestamp-lock.sh prep   # 本地孤儿分支 + SHA256SUMS + 验证（可逆，随时跑）
#   bash t5-timestamp-lock.sh push   # 推远程（对外动作，仅 D 说"投"后）
# 先例: idea53-preprint-ts-v4 @ e8754392a（v1/v2 孤儿索引未清导致 WIP 泄漏的教训已内置）
set -euo pipefail
cd "$(dirname "$0")/../.."   # pfb 仓根
TAG="thinkmech-preprint-ts-v1"
SUBDIR="submission-thinkmech"
BRANCH="${TAG}-branch"

BUNDLE=(
  tasks/think-mechanism-paper/draft/paper.tex
  tasks/think-mechanism-paper/draft/paper.pdf
  tasks/think-mechanism-paper/draft/number-trace.md
  tasks/think-mechanism-paper/draft/revision-log.md
  tasks/think-mechanism-paper/pilot/runs.json
  tasks/think-mechanism-paper/pilot/results.md
  tasks/think-mechanism-paper/pilot/audit-rubric.md
  tasks/think-mechanism-paper/pilot/scores.json
)

prep() {
  # 1. 文件齐全
  for f in "${BUNDLE[@]}"; do
    [[ -f "$f" ]] || { echo "MISSING: $f"; exit 1; }
  done
  # 2. 孤儿分支（先删旧的，防 v1/v2 索引残留）
  git branch -D "$BRANCH" 2>/dev/null || true
  git checkout --orphan "$BRANCH"
  # 只清索引不动工作区（git rm 会删掉 bundle 源文件，cp 就失败了——idea53 v1/v2 教训）
  git reset -q
  mkdir -p "$SUBDIR"
  for f in "${BUNDLE[@]}"; do
    cp "$f" "$SUBDIR/"
  done
  ( cd "$SUBDIR" && sha256sum paper.tex paper.pdf number-trace.md revision-log.md runs.json results.md audit-rubric.md scores.json > SHA256SUMS.txt )
  git add "$SUBDIR"
  git -c user.name="zero" -c user.email="zero@local" commit -qm "T5 timestamp lock: think-mechanism-paper submission bundle (8 files + SHA256SUMS)"
  # 3. 完整树验证（只许 8 文件 + SHA256SUMS，零 WIP 泄漏）
  FILES=$(git ls-tree -r --name-only HEAD)
  COUNT=$(echo "$FILES" | wc -l | tr -d ' ')
  echo "tree files: $COUNT"
  echo "$FILES"
  [[ "$COUNT" == "9" ]] || { echo "TREE LEAK: expect 9 files (8 + SHA256SUMS), got $COUNT"; git checkout -q main 2>/dev/null || git checkout -q -; exit 1; }
  # 4. git archive 解包 + sha256sum -c（哈希自洽）
  TMP=$(mktemp -d)
  git archive HEAD | tar -x -C "$TMP"
  ( cd "$TMP/$SUBDIR" && sha256sum -c SHA256SUMS.txt )
  rm -rf "$TMP"
  # 回到工作分支
  CUR=$(git branch --show-current)
  git checkout -q main 2>/dev/null || git checkout -q -
  echo "PREP OK: branch $BRANCH @ $(git rev-parse --short $BRANCH), 9 files, hashes self-consistent"
}

push() {
  prep
  git push origin "$BRANCH"
  # 远程 200 验证
  CODE=$(curl -s -o /dev/null -w "%{http_code}" "https://github.com/dd2003-460/prompt-first-bench/tree/$BRANCH/$SUBDIR/SHA256SUMS.txt")
  echo "remote HTTP $CODE"
  [[ "$CODE" == "200" ]] || { echo "REMOTE VERIFY FAILED"; exit 1; }
  echo "T5 LOCKED: $BRANCH @ $(git rev-parse $BRANCH) pushed + remote 200"
}

case "${1:-}" in
  prep) prep ;;
  push) push ;;
  *) echo "usage: $0 {prep|push}"; exit 2 ;;
esac

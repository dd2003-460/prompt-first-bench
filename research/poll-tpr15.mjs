#!/usr/bin/env node
// Poll T-PR-15 arena session: detect completion (commit_sha receipt) or interruption (Stopped, no progress).
// Usage: node poll-tpr15.mjs <max_polls> <interval_ms>
const MAX = parseInt(process.argv[2] || '40', 10);   // ~2h at 3min
const INTERVAL = parseInt(process.argv[3] || '180000', 10);
const SESSION = '01a1ca66-5358-7039-bcfa-b2fbf65a5a27';

let lastRan = -1;
let stablePolls = 0;

for (let i = 1; i <= MAX; i++) {
  try {
    const task = await taskSpace(3769);
    const page = task.page("p1");
    await page.waitForTimeout(1500);
    const info = await page.evaluate(() => {
      const body = document.body.innerText;
      const ranCount = (body.match(/Ran commands/g)||[]).length;
      const hasCommitSha = /commit[_ ]?sha|@[0-9a-f]{7,40}/i.test(body.slice(-4000));
      const genBtns = [...document.querySelectorAll('button')].map(b=>({al:b.getAttribute('aria-label'),dis:b.disabled})).filter(c=>/generat|send/i.test(c.al||''));
      const running = genBtns.some(b=>b.al==='Stop generating' && !b.dis);
      const tail = body.slice(-600);
      return { url: location.href, ranCount, hasCommitSha, running, tail };
    });
    const ts = new Date().toISOString();
    console.log(`[${ts}] poll ${i}/${MAX} ran=${info.ranCount} running=${info.running} commit=${info.hasCommitSha}`);

    if (info.hasCommitSha) {
      console.log('RESULT: COMPLETE — commit sha detected');
      console.log('TAIL:', info.tail);
      process.exit(0);
    }
    // interruption: not running AND ranCount unchanged for 2 consecutive polls
    if (!info.running) {
      if (info.ranCount === lastRan) stablePolls++; else stablePolls = 0;
      if (stablePolls >= 2) {
        console.log('RESULT: INTERRUPTED — Stopped with no progress for 2 polls');
        console.log('TAIL:', info.tail);
        process.exit(2);
      }
    } else {
      stablePolls = 0;
    }
    lastRan = info.ranCount;
    await new Promise(r=>setTimeout(r, INTERVAL));
  } catch (e) {
    console.log(`[${new Date().toISOString()}] poll ${i} error: ${e.message}`);
    await new Promise(r=>setTimeout(r, INTERVAL));
  }
}
console.log('RESULT: TIMEOUT — max polls reached, still running');
process.exit(3);
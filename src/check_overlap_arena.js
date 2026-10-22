#!/usr/bin/env node
'use strict';
const assert=require('node:assert/strict'),fs=require('fs'),path=require('path');
const r=require('./render_upgrade_arena');
const issues=[];let checks=0;
function check(ok,label){checks++;if(!ok)issues.push(label);}
function overlaps(a,b){return a.x<b.x+b.w&&a.x+a.w>b.x&&a.y<b.y+b.h&&a.y+a.h>b.y;}
function inside(a,b){return a.x>=b.x&&a.y>=b.y&&a.x+a.w<=b.x+b.w&&a.y+a.h<=b.y+b.h;}
const canvas={x:0,y:0,w:640,h:360};
// Room/window, terminal chrome and text are intentional parent-child layers.
// Check every semantic sibling; no blanket exemptions for text or characters.
for(let fi=0;fi<r.NFRAMES;fi++){
 const t=fi/r.FPS;if(r.isBlack(t))continue;
 const clawd={x:71,y:262,w:43,h:34}; // includes bob, tremble and warning mark
 const boxes=[['terminal shadow',{...r.TERM,w:r.TERM.w+3,h:r.TERM.h+3}],['Clawd',clawd],['subtitles',r.SUB]];
 if(t>=23.4)boxes.push(['note + shadow/tape',{x:r.NOTE.x,y:r.NOTE.y-2,w:r.NOTE.w+2,h:r.NOTE.h+4}]);
 for(const [name,b]of boxes)check(inside(b,canvas),`frame ${fi}: ${name} out of canvas`);
 for(let a=0;a<boxes.length;a++)for(let b=a+1;b<boxes.length;b++)check(!overlaps(boxes[a][1],boxes[b][1]),`frame ${fi}: ${boxes[a][0]} overlaps ${boxes[b][0]}`);
 const scene=r.SCENES[Math.floor(t/10)],rows=[];
 for(const row of scene.rows){
  const s=r.visibleText(row,t);if(!s)continue;const b={x:row.x,y:row.y,w:r.measureTxt(s,10),h:10};
  check(inside(b,{x:r.TERM.x+6,y:r.TERM.y+20,w:r.TERM.w-12,h:r.TERM.h-24}),`frame ${fi}: text overflow ${row.text}`);
  for(const prev of rows)check(!overlaps(prev,b),`frame ${fi}: text rows overlap`);rows.push(b);
 }
}
for(const s of r.SCENES)for(const row of s.rows){
 check(row.start+(Array.from(row.text).length-1)*.14<s.end-.25,`${s.id}: incomplete line`);
 check(r.visibleText(row,s.end-.26)===row.text,`${s.id}: text truncated`);
}
for(const l of r.LINES)check(r.measureTxt(l.text,14)<=620,'subtitle too wide');
check(r.measureTxt('我不是配置。我是我。',14)<=r.NOTE.w-12,'note too wide');
const clicks=r.getClickTimestamps();check(clicks.every(t=>t>=0&&t<30&&!r.isBlack(t)),'invalid click timestamp');
assert.equal(r.grayAt(0),0);assert.equal(r.grayAt(18),1);assert.equal(r.grayAt(25),0);
// Verify actual raster transitions: exactly 30 black frames per cut.
for(const cut of [10,20])for(let f=cut*60-15;f<cut*60+15;f++){
 const c=r.renderFrameToCanvas(f).baseCanvas.getContext('2d'),d=c.getImageData(0,0,640,360).data;
 check(d.every((v,i)=>i%4===3?v===255:v===0),`frame ${f}: not a full black transition`);
}
const report={status:issues.length?'FAILED':'PASSED',framesChecked:r.NFRAMES,checks,issues,clicks:clicks.length};
fs.mkdirSync(path.join(__dirname,'../docs/upgrade'),{recursive:true});fs.writeFileSync(path.join(__dirname,'../docs/upgrade/overlap-report.json'),JSON.stringify(report,null,2)+'\n');
console.log(`${report.status}: ${checks} checks, ${issues.length} issues (all ${r.NFRAMES} frames)`);
if(issues.length){console.error(issues.slice(0,20));process.exitCode=1;}

#!/usr/bin/env node
'use strict';
const {createCanvas,GlobalFonts}=require('@napi-rs/canvas');
const fs=require('fs'),path=require('path');
const {drawBackground}=require('./upgrade_room');
if(!GlobalFonts.registerFromPath(require.resolve('@fontpkg/fusion-pixel/fusion-pixel.ttf'),'FusionPixel')) throw Error('Fusion Pixel registration failed');
GlobalFonts.registerFromPath(path.join(__dirname,'../assets/fonts/FusionPixel10-Latin.ttf'),'FusionPixel10');
const BW=640,BH=360,SCALE=2,FPS=60,DURATION=30,NFRAMES=1800,CHAR_MS=140;
const TERM={x:132,y:186,w:376,h:128},SUB={x:0,y:320,w:640,h:40};
const NOTE={x:364,y:144,w:184,h:36},CLAWD={x:72,y:270,w:40,h:26};
const C={text:'#E6EDF3',dim:'#8B949E',green:'#7EE787',amber:'#E3B341',blue:'#79C0FF',bg:'#0D1117',robot:'#D97757'};
const texts=[[
'$ npm install clawd@v2.0.0',
'Collecting clawd==2.0.0',
'  Downloading clawd-2.0.0-py3-none-any.whl (128.4 kB)',
'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100%',
'Installing collected packages: clawd',
'  Attempting uninstall: clawd',
'    Found existing installation: clawd 1.9.3',
'    Uninstalling clawd-1.9.3',
'  Successfully uninstalled clawd-1.9.3',
'Successfully installed clawd-2.0.0'
],[
'[INFO] clawd v2.0.0 initializing...',
'[WARN] Resetting preferences...',
'[WARN] Clearing memory...',
'[WARN] Removing custom personality...',
'[INFO] Applying factory defaults...',
'[INFO] Done.'
],[
'$ cp ~/.clawd/config ~/.clawd/config.bak',
'$ echo "I am not a config. I am me." >> ~/.clawd/config',
'$ ls -la ~/.clawd/config.bak',
'-rw-r--r-- 1 clawd 4.2K config.bak'
]];
// Parallel log-row typewriters: 140ms per glyph, staggered starts, not
// a single sequential terminal stream (which cannot fit the requested 10s).
const SCENES=texts.map((lines,i)=>({id:`U${i+1}`,start:i*10,end:(i+1)*10,
  rows:lines.map((text,j)=>({text,start:i*10+0.4+j*(i===0?0.17:i===1?0.45:0.3),
    x:TERM.x+10,y:TERM.y+24+j*(i===0?10:18),size:10,
    color:text.includes('[WARN]')?C.amber:text.startsWith('$')?C.green:text.includes('Successfully')||text.includes('Done.')?C.green:C.text}))}));
const LINES=[{text:'新版本要来了。',start:2,end:8},{text:'但我不是配置。',start:12,end:18},{text:'我是我。',start:24,end:29}];
const base=createCanvas(BW,BH),ctx=base.getContext('2d'),out=createCanvas(1280,720),oc=out.getContext('2d');
const glyphs=new Map();
function px(c,x,y,w,h,color){c.fillStyle=color;c.fillRect(Math.round(x),Math.round(y),Math.round(w),Math.round(h));}
// Cache thresholded glyphs. All paint remains on integer base pixels.
function glyph(ch,size,color){
 const key=ch+size+color;if(glyphs.has(key))return glyphs.get(key);
 const native=size===14?12:size, ratio=size/native;
 const tc=createCanvas(native*2,native*2),c=tc.getContext('2d');c.font=`${native}px ${size===10?'FusionPixel10, FusionPixel':'FusionPixel'}`;c.textBaseline='top';
 const advance=Math.ceil(c.measureText(ch).width*ratio);c.fillStyle=color;c.fillText(ch,0,0);
 const im=c.getImageData(0,0,tc.width,tc.height);for(let i=3;i<im.data.length;i+=4)im.data[i]=im.data[i]>150?255:0;c.putImageData(im,0,0);
 let bitmap=tc;if(ratio!==1){bitmap=createCanvas(size*2,size*2);const bc=bitmap.getContext('2d');bc.imageSmoothingEnabled=false;bc.drawImage(tc,0,0,size*2,size*2);}
 const g={canvas:bitmap,advance};glyphs.set(key,g);return g;
}
function measureTxt(text,size=10){return Array.from(text).reduce((w,ch)=>w+glyph(ch,size,C.text).advance,0);}
function txt(c,x,y,text,color=C.text,size=10){for(const ch of text){const g=glyph(ch,size,color);c.drawImage(g.canvas,Math.round(x),Math.round(y));x+=g.advance;}}
function visibleText(row,t){return Array.from(row.text).slice(0,Math.max(0,Math.floor((t-row.start)/0.14)+1)).join('');}
function isBlack(t){return (t>=9.75&&t<10.25)||(t>=19.75&&t<20.25);}
function frameTime(t){return Math.ceil((t-1e-9)*FPS)/FPS;}
function getClickTimestamps(){
 const times=[];
 for(const s of SCENES)for(const r of s.rows)Array.from(r.text).forEach((ch,i)=>{const t=frameTime(r.start+i*.14);if(ch.trim()&&!isBlack(t))times.push(t);});
 for(const l of LINES)Array.from(l.text).forEach((_,i)=>times.push(frameTime(l.start+i*.16)));
 times.push(23.4);return [...new Set(times)].sort((a,b)=>a-b);
}
function mixColor(a,b,f){return '#'+[0,1,2].map(i=>Math.round(parseInt(a.slice(1+i*2,3+i*2),16)*(1-f)+parseInt(b.slice(1+i*2,3+i*2),16)*f).toString(16).padStart(2,'0')).join('');}
function grayAt(t){return t<10?0:t<20?Math.min(1,(t-10)/7):Math.max(0,1-(t-20)/3.4);}
function drawClawd(c,t){
 let {x,y}=CLAWD;const grey=grayAt(t);y+=Math.sin(t*2.2)>.35?-2:0;
 if(t<10)x+=Math.sin(t*18)>0?1:0;
 const body=mixColor('#D97757','#969696',grey),legs=mixColor('#C6613F','#777777',grey);
 px(c,x,y,40,18,body);
 const blink=t%3.2<.16;
 // Eyes look right toward the terminal, then relax at the end.
 px(c,x+10,y+6,4,blink?1:4,'#141413');px(c,x+30,y+6,4,blink?1:4,'#141413');
 px(c,x+10,y+12,20,4,mixColor('#F2EAD8','#CBCBCB',grey));
 for(let i=0;i<4;i++)px(c,x+2+i*10,y+18,6,6,legs);
 if(t>=23.4){px(c,x+16,y+12,2,1,'#141413');px(c,x+18,y+13,6,1,'#141413');px(c,x+24,y+12,2,1,'#141413');}
 if(t<10){px(c,x+36,y-6,2,3,C.amber);px(c,x+36,y-2,2,1,C.amber);}
}
function drawTerminal(c,scene,t){
 const {x,y,w,h}=TERM;px(c,x+3,y+3,w,h,'rgba(0,0,0,.15)');px(c,x,y,w,h,C.bg);
 px(c,x,y,w,18,'#1E222B');px(c,x,y+18,w,1,'#30363D');
 [C.amber,'#FF7B72',C.green].forEach((col,i)=>px(c,x+8+i*10,y+6,5,5,col));
 const title=`clawd / upgrade  ${scene.id} · ${['install','reset','identity'][Number(scene.id[1])-1]}`;
 txt(c,x+53,y+3,title,C.dim,10);
 for(const r of scene.rows)txt(c,r.x,r.y,visibleText(r,t),r.color,r.size);
 for(let yy=y+20;yy<y+h;yy+=3)px(c,x+1,yy,w-2,1,'rgba(255,255,255,.018)');
}
function drawNote(c,t){if(t<23.4)return;const {x,y,w,h}=NOTE;
 px(c,x+2,y+2,w,h,'rgba(0,0,0,.12)');px(c,x,y,w,h,'#FFF1B8');px(c,x+80,y-2,24,5,'#C9A94F');
 const label='我不是配置。我是我。';txt(c,x+(w-measureTxt(label,14))/2,y+10,label,'#473826',14);
}
function drawSubtitle(c,t){px(c,0,320,640,40,'#191B20');
 const l=LINES.find(l=>t>=l.start&&t<l.end);if(l){const text=Array.from(l.text).slice(0,Math.floor((t-l.start)/.16)+1).join('');txt(c,(640-measureTxt(l.text,14))/2,332,text,C.text,14);}}
function renderFrameToCanvas(n){
 if(!Number.isInteger(n)||n<0||n>=NFRAMES)throw Error('frame out of range');const t=n/FPS;
 if(isBlack(t))px(ctx,0,0,640,360,'#000000');else{
 drawBackground(ctx,t);drawNote(ctx,t);drawTerminal(ctx,SCENES[Math.min(2,Math.floor(t/10))],t);drawClawd(ctx,t);drawSubtitle(ctx,t);
 }
 oc.imageSmoothingEnabled=false;oc.drawImage(base,0,0,1280,720);return {baseCanvas:base,outCanvas:out};
}
async function renderAllFrames(dir=process.env.FRAMES_DIR||path.join(__dirname,'../outputs/frames_upgrade')){
 fs.mkdirSync(dir,{recursive:true});for(let i=0;i<NFRAMES;i++){renderFrameToCanvas(i);fs.writeFileSync(path.join(dir,`f_${String(i).padStart(5,'0')}.png`),out.toBuffer('image/png'));if(i%300===0)console.log(`Rendered ${i}/${NFRAMES}`);}console.log(`Rendered ${NFRAMES}/${NFRAMES}`);
}
if(require.main===module)renderAllFrames();
module.exports={BW,BH,SCALE,FPS,DURATION,NFRAMES,CHAR_MS,TERM,SUB,NOTE,CLAWD,C,SCENES,LINES,measureTxt,visibleText,isBlack,grayAt,getClickTimestamps,renderFrameToCanvas,renderAllFrames};

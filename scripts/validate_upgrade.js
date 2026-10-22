#!/usr/bin/env node
'use strict';
const fs=require('fs'),path=require('path'),{execFileSync,spawnSync}=require('child_process'),assert=require('assert/strict');
const {readWavPcm16}=require('./build_audio_arena');
const root=path.join(__dirname,'..');
const ffmpeg=process.env.FFMPEG_BIN||execFileSync(path.join(root,'.venv/bin/python'),['-c','import imageio_ffmpeg; print(imageio_ffmpeg.get_ffmpeg_exe())'],{encoding:'utf8'}).trim();
const file=path.join(root,'outputs/upgrade_arena_v1.0.mp4');
const decode=spawnSync(ffmpeg,['-hide_banner','-i',file,'-map','0:v:0','-f','null','-'],{encoding:'utf8'});
assert.equal(decode.status,0,decode.stderr);
assert.match(decode.stderr,/Video: h264/);assert.match(decode.stderr,/1280x720/);assert.match(decode.stderr,/60 fps/);assert.match(decode.stderr,/Duration: 00:00:30\.00/);
const frameCounts=[...decode.stderr.matchAll(/frame=\s*(\d+)/g)].map(m=>Number(m[1]));assert.equal(frameCounts.at(-1),1800);
const {samples,sampleRate}=readWavPcm16(path.join(root,'audio/upgrade_arena_mix.wav'));
let peak=0,clipped=0;for(const x of samples){peak=Math.max(peak,Math.abs(x));if(Math.abs(x)>=32767/32768)clipped++;}assert.equal(samples.length/sampleRate,30);assert.equal(clipped,0);
// Also inspect the delivered AAC, whose encode can create intersample overshoot.
const decoded=spawnSync(ffmpeg,['-v','error','-i',file,'-map','0:a:0','-ac','1','-f','f32le','pipe:1'],{maxBuffer:16*1024*1024});assert.equal(decoded.status,0);
let aacPeak=0;for(let i=0;i<decoded.stdout.length;i+=4)aacPeak=Math.max(aacPeak,Math.abs(decoded.stdout.readFloatLE(i)));assert(aacPeak<1,'AAC clipping');
const report={status:'PASSED',video:{codec:'h264',width:1280,height:720,fps:60,frames:1800,durationSeconds:30},audio:{sampleRate,durationSeconds:30,peakLinear:peak,peakDbFS:20*Math.log10(peak),clippedSamples:clipped,aacDecodedPeak:aacPeak},transitionBlackFrames:30};
fs.writeFileSync(path.join(root,'docs/upgrade/media-report.json'),JSON.stringify(report,null,2)+'\n');console.log(report);

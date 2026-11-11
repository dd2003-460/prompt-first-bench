import { readFileSync } from 'node:fs';
const script = readFileSync('./poll-tpr15.mjs','utf8');
eval(script);

// Channel counters from the user-provided tracking service. Never invent post dates.
export const WEB_TRACKING_ENDPOINT='http://103.90.224.177:6001/verify-channel';
const calendar=new Intl.DateTimeFormat('sv-SE',{timeZone:'Asia/Ho_Chi_Minh',year:'numeric',month:'2-digit',day:'2-digit'});
export const trackingDay=at=>calendar.format(new Date(at));
const metrics=['followers','likes','videos'];
const validCount=value=>Number.isSafeInteger(value)&&value>=0;
const counts=value=>metrics.every(k=>validCount(value?.[k]));
export function parseWebTracking(raw,expectedHandle){
 const channel=raw?.channel;
 if(raw?.valid!==true||raw?.type!=='channel'||String(raw?.platform).toLowerCase()!=='tiktok'||!channel||channel.privateAccount===true)
  throw Error('Web tracking chưa trả số liệu kênh công khai hợp lệ.');
 if(typeof channel.uniqueId!=='string'||channel.uniqueId.toLowerCase()!==expectedHandle.toLowerCase())
  throw Error('Web tracking trả về kênh khác với kênh đã gán.');
 if(raw.profileUrl){
  const url=new URL(raw.profileUrl);
  if(url.protocol!=='https:'||!['www.tiktok.com','tiktok.com'].includes(url.hostname)||url.username||url.password||url.port||url.pathname.replace(/\/$/,'').toLowerCase()!=='/@'+expectedHandle.toLowerCase())
   throw Error('Địa chỉ kênh trả về không khớp.');
 }
 const result={followers:channel.followers,likes:channel.hearts,videos:channel.videos};
 if(!counts(result))throw Error('Web tracking trả số liệu thiếu hoặc không hợp lệ.');
 return result;
}
const copy=value=>Object.fromEntries(metrics.map(k=>[k,value[k]]));
const growth=(end,start)=>Object.fromEntries(metrics.map(k=>[k,end[k]-start[k]]));
export function recordWebTracking(previous,point,followerReference=null){
 if(!counts(point)||typeof point.at!=='string'||!Number.isFinite(Date.parse(point.at)))throw Error('Mốc quét không hợp lệ.');
 if(previous&&previous.version!==1)throw Error('Phiên bản sổ quét chưa được hỗ trợ.');
 const at=new Date(point.at).toISOString(),day=trackingDay(at),current=copy(point),oldDays=previous?.days||[];
 if(!Array.isArray(oldDays)||oldDays.some(d=>!counts(d.opening)||!counts(d.current)||typeof d.day!=='string'))throw Error('Sổ quét cần được kiểm tra trước khi cập nhật.');
 const last=oldDays[oldDays.length-1];
 if(last&&Date.parse(last.lastAt)>Date.parse(at))return previous;
 const days=oldDays.map(d=>({...d,opening:copy(d.opening),current:copy(d.current),first:copy(d.first)}));
 let entry=days.find(d=>d.day===day);
 if(entry){
  entry.current=current;entry.lastAt=at;entry.scans=(entry.scans||1)+1;
 }else{
  const opening=last?copy(last.current):{...current,followers:validCount(followerReference?.count)?followerReference.count:current.followers};
  entry={day,firstAt:at,lastAt:at,opening,first:current,current,scans:1,
   referenceSource:last?'previous_scan':validCount(followerReference?.count)?followerReference.source:'first_scan'};
  days.push(entry);days.sort((a,b)=>a.day.localeCompare(b.day));
 }
 return {version:1,source:'web_tracking',startedAt:previous?.startedAt||at,days};
}
export function webTrackingView(tracking,from,to){
 const days=Array.isArray(tracking?.days)?tracking.days.filter(d=>counts(d.opening)&&counts(d.current)):[];
 const last=days[days.length-1],selected=days.filter(d=>d.day>=from&&d.day<=to);
 return {ready:!!last,source:'web_tracking',startedAt:tracking?.startedAt||null,asOf:last?.lastAt||null,
  current:last?copy(last.current):null,
  days:selected.map(d=>({day:d.day,firstAt:d.firstAt,lastAt:d.lastAt,opening:copy(d.opening),current:copy(d.current),growth:growth(d.current,d.opening),scans:d.scans,referenceSource:d.referenceSource})),
  growth:selected.length?selected.reduce((sum,d)=>{for(const k of metrics)sum[k]+=d.current[k]-d.opening[k];return sum;},{followers:0,likes:0,videos:0}):null};
}
export function webTrackingFollowers(channel,from,to,apiView){
 const tracking=channel?.webTracking,days=Array.isArray(tracking?.days)?tracking.days:[],last=days[days.length-1],history=[];
 for(const d of days){
  if(!counts(d.first)||!counts(d.current))continue;
  if(d.day>to)continue;
  history.push({at:d.firstAt,count:d.first.followers,source:'web_tracking'});
  if(d.lastAt!==d.firstAt)history.push({at:d.lastAt,count:d.current.followers,source:'web_tracking'});
 }
 return {...apiView,status:last?'web_tracking':'awaiting_web_scan',current:last?.current.followers??null,
  asOf:last?.lastAt||null,firstRecordedAt:tracking?.startedAt||null,history};
}

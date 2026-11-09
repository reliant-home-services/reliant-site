(function(){
var mb=document.querySelector('.menu-btn'),nav=document.getElementById('nav');
if(mb)mb.addEventListener('click',function(){var o=nav.classList.toggle('open');mb.setAttribute('aria-expanded',o)});
// quote forms
document.querySelectorAll('form[data-lead]').forEach(function(f){
 var t0=Date.now(),msg=f.querySelector('.msg'),btn=f.querySelector('button[type=submit]');
 f.addEventListener('submit',function(e){
  e.preventDefault();
  var d=Object.fromEntries(new FormData(f).entries());d.elapsed=Date.now()-t0;d.page=location.pathname;
  btn.disabled=true;var old=btn.textContent;btn.textContent='Sending…';msg.className='msg';
  fetch('/api/lead',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(d)})
   .then(function(r){return r.json().catch(function(){return{}}).then(function(j){return{ok:r.ok&&j.ok,j:j}})})
   .then(function(x){
     if(x.ok){f.reset();msg.className='msg ok';msg.textContent='Thank you. Your request has been sent and we will call you shortly.'}
     else{msg.className='msg err';msg.textContent=(x.j&&x.j.error)||'Sorry, that did not send. Please call (770) 508-0971 and we will help right away.'}
   })
   .catch(function(){msg.className='msg err';msg.textContent='Sorry, that did not send. Please call (770) 508-0971 and we will help right away.'})
   .finally(function(){btn.disabled=false;btn.textContent=old});
 });
});
// gallery filter + lightbox
var fb=document.querySelectorAll('.filters button');
fb.forEach(function(b){b.addEventListener('click',function(){
 fb.forEach(function(x){x.setAttribute('aria-pressed',x===b)});
 var c=b.dataset.f;document.querySelectorAll('.gallery figure').forEach(function(g){g.style.display=(c==='all'||g.dataset.c===c)?'':'none'});
})});
var lb=document.getElementById('lb');
if(lb){document.querySelectorAll('.gallery img').forEach(function(i){i.addEventListener('click',function(){lb.querySelector('img').src=i.dataset.full||i.src;lb.querySelector('img').alt=i.alt;lb.classList.add('on')})});
 lb.addEventListener('click',function(){lb.classList.remove('on')});document.addEventListener('keydown',function(e){if(e.key==='Escape')lb.classList.remove('on')})}
})();

/* Google reviews widget: fills any <div data-greviews> from /api/reviews */
(function(){
var boxes=document.querySelectorAll('[data-greviews]');if(!boxes.length)return;
function esc(s){return String(s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function stars(n){var s='';for(var i=1;i<=5;i++)s+=i<=Math.round(n)?'\u2605':'\u2606';return s}
function ago(t){if(!t)return'';var d=new Date(t);if(isNaN(d))return'';return d.toLocaleDateString('en-US',{month:'long',year:'numeric'})}
fetch('/api/reviews').then(function(r){return r.json()}).then(function(d){
 if(!d||!d.reviews||!d.reviews.length){boxes.forEach(function(b){(b.closest('section')||b).hidden=true});return}
 boxes.forEach(function(b){
  var max=parseInt(b.getAttribute('data-max')||'6',10);
  var head='<div class="gr-head"><span class="gr-stars" aria-hidden="true">'+stars(d.rating)+'</span> <b>'+(d.rating?Number(d.rating).toFixed(1):'')+'</b> <span>from '+d.count+' Google reviews</span></div>';
  var cards=d.reviews.slice(0,max).map(function(r){
   return '<div class="feat gr-card"><div class="gr-stars" aria-label="'+r.rating+' out of 5 stars">'+stars(r.rating)+'</div><p>&ldquo;'+esc(r.text)+'&rdquo;</p><p><b>'+esc(r.name)+'</b>'+(ago(r.time)?' &middot; '+ago(r.time):'')+'</p></div>'}).join('');
  var link=d.url?'<p class="center" style="margin-top:20px"><a class="btn" href="'+esc(d.url)+'" rel="noopener" target="_blank">Read all our Google reviews</a></p>':'';
  b.innerHTML=head+'<div class="grid g3" style="margin-top:20px">'+cards+'</div>'+link;
 });
}).catch(function(){boxes.forEach(function(b){(b.closest('section')||b).hidden=true})});
})();

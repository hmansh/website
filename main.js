setInterval(() => {
	let def_with = document.getElementById('yearr').clientWidth;
	let d = new Date();
	d.setMonth(0);
	d.setDate(1);
	d.setHours(0);
	d.setMinutes(0);
	d.setSeconds(0);
	let now = new Date();
	let elapsedY = now - d;
	let spy = 31536000;
	let yperc = elapsedY / 1000 / spy;
	yperc = Math.round(yperc * 10000000) / 100000;
	ypp.innerHTML = yperc + "%";
	ybar.style.width = def_with * yperc / 100 + "px";
}, 500);

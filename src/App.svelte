<script>
	import { baseAddr } from './stores.js';
	import io from 'socket.io-client';
	export let name;


	const socket = io($baseAddr)
	socket.on('connect', data => {
  	console.log('joooj');
	});

/*
document.addEventListener('mousemove', e => {
	const elem = document.getElementById('cursorStick')
	elem.style.transform = 'translateY('+ (e.clientY - 40) + 'px)';
	elem.style.transform += 'translateX('+ (e.clientX - 20) + 'px)';
},false);
*/

</script>

<main>
	<div class="logo"></div>
	<button class="lode-btn">HRÁT</button>

</main>

<style>
	main {
		height: 400px;
		max-width: 600px;
		margin: 5% auto;
	}
	div {
		height: 200px;
		width: 100%;
		background: var(--backdrop);
		background-image: url('/imgs/ship.svg');
		background-repeat: no-repeat;
		background-position: center;
	}
	button {
		width: 130px;
		height: 150px;
		margin: 25px auto;
		padding-top: 80px;
		border-radius: 2px;
		box-sizing: border-box;
		color: white;
		background-color: var(--backdrop);
		background-image: url('/imgs/play.svg');
		background-repeat: no-repeat;
		background-position: center 40px;
		background-size: 35%;
		transition: background-color 1s;
		font-size: 1.1em;
	}
	button:hover {
		 background-color: var(--blue1);
	}
</style>

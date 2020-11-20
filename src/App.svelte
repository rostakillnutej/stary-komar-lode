<script>
	import { state } from './stores/global.js';
	import Hello from './HelloPage.svelte';
	import GameTable from './DraftPage.svelte';
	/* Example připojení na sockety
	import { onMount } from 'svelte';
		onMount( _ => {
	    const socket = io($baseAddr)
	  	socket.on('connect', data => {
	    	//console.log('joooj');
	  	});
		});
	*/


/*
document.addEventListener('mousemove', e => {
	const elem = document.getElementById('cursorStick')
	elem.style.transform = 'translateY('+ (e.clientY - 40) + 'px)';
	elem.style.transform += 'translateX('+ (e.clientX - 20) + 'px)';
},false);
*/

function handleStart() {
	state.update(_ => 'planning');
}

</script>

<main>

{#if $state == 'menu'}
	<Hello on:start={() => handleStart()} />
{:else if $state == 'planning'}
	<GameTable />
{:else if $state == 'game'}
	<div></div>
{/if}

</main>

<style>
</style>

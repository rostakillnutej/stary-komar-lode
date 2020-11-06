<script>
	import Hello from './components/Hello.svelte';
	import GameTable from './DraftPage.svelte';
	let playing = false;
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
	playing = true;
}

</script>

<main>

{#if !playing}
	<Hello on:start={() => handleStart()} />
{:else}
	<GameTable />
{/if}

</main>

<style>
</style>

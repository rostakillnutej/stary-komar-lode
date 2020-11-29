<script>
	import { state,baseAddr } from './stores/global.js';
	import axios from 'axios'
	import { onMount } from 'svelte';
	import Hello from './HelloPage.svelte';
	import GameTable from './DraftPage.svelte';


	onMount( _ => {
		axios({
		  method: 'get',
		  url: $baseAddr + '/user',
			withCredentials: true
		})
		.then(res => {
			console.log('user OK')
		  state.update(_ => 'menu');
		})
		.catch(res => {
		  console.log('user not OK')
		});
	});


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

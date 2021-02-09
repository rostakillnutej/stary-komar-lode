<script>
	import { state,baseAddr } from './stores/global.js';
	import axios from 'axios'
	import { onMount } from 'svelte';
	import Hello from './HelloPage.svelte';
	import DraftPage from './DraftPage.svelte';
	import GamePage from './GamePage.svelte';
	import FinishPage from './FinishPage.svelte';


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
	<DraftPage />
{:else if $state == 'game'}
	<GamePage />
{:else if $state == 'gameEnd'}
	<FinishPage />
{/if}

</main>

<style>
</style>

<script>
	import { createEventDispatcher } from 'svelte';
	const dispatch = createEventDispatcher();
</script>

<main>
	<div class="logo"></div>

	<button class="lode-btn" on:click={() => dispatch('start')}>PLÁNOVAT</button>

	<div class="desc">
		Pravidla jsou jednoduchá, po zmáčknutí tlačítky plánovat se teleportujete ne stránku s rozložením lodí do pole. Lodě si následně rozložíte do tabulky tak, aby nebyly vedle sebe. Následně si zvolíte obtížnost protivníka a kliknete na Hrát. Cílem hry je zničit všechny protivníkovy loě. Dosáhnete toho tak že, se navzájem přestřelujete dokud jeden z vás nevyhraje.
	</div>
</main>

<style>
	main {
		height: 400px;
		max-width: 600px;
		margin: 5% auto;
	}
	.logo {
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

	.desc {
		color: white;
	}


</style>

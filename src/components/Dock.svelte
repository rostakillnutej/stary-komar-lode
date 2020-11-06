<script>
  import ShipElem from './ShipElem.svelte'
  import Ship from '../objects/Ship.js'
  import { dock,shipSelected } from '../stores.js';

  function selectShip(e){
    const exist = document.querySelector('#sticked')
    if(exist)exist.remove()
    shipSelected.update(_ => $dock[e.detail])
    const cln = e.explicitOriginalTarget.cloneNode(true);
    cln.setAttribute('id', 'sticked');
    document.body.appendChild(cln);
    /* Tady nevím jestli se potom ty listenery mažou*/
    document.addEventListener('mousemove', e => {
    	cln.style.transform = 'translateY('+ (e.clientY + 10) + 'px)';
    	cln.style.transform += 'translateX('+ (e.clientX - 20) + 'px)';
    },false);

  }

</script>

<main>
	<div class="ship-storage">
    {#each $dock as item, i}
      <ShipElem index={i} props={item} on:select={selectShip}/>
  	{/each}
  </div>
</main>

<style>

</style>

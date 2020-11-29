<script>
  import { createEventDispatcher } from 'svelte';
  const dispatch = createEventDispatcher();
  import ShipElem from './ShipElem.svelte'
  import { table,dock,shipSelected,isHover,hoverPos } from '../stores/planning.js';
  import * as lode from '../lodeLib.js'

  function selectShip(e){
    shipSelected.update(_ => $dock[e.detail.index])
    //Vytvoření tabulky která se pohybuje s myší
    const cln = e.detail.e.target.cloneNode(true);
    cln.setAttribute('id', 'sticked');
    document.body.appendChild(cln);
    /* Tady nevím jestli se potom ty listenery mažou*/
    document.addEventListener('mousemove', e => {
    	cln.style.transform = 'translateY('+ (e.clientY + 10) + 'px)';
    	cln.style.transform += 'translateX('+ (e.clientX - 20) + 'px)';
    },false);
  }

  function deselectShip(e){
    //Maže loď ze schránky, kurzoru a její nastínění
    if(!$shipSelected) return;
    document.querySelector('#sticked').remove()
    const newTable = lode.removeShip($table,$shipSelected,$hoverPos[0],$hoverPos[1],'h')
    if(newTable){
      table.update(_ => newTable)
      isHover.update(_ => false)
    }
    shipSelected.update(_ => false)
  }

</script>

<button class="ship-storage" on:click={e => deselectShip(e)}>
  {#each $dock as item, i}
    <ShipElem index={i} props={item} on:select={selectShip}/>
	{/each}
</button>

<style>
.ship-storage {
  height: 100%;
  min-height: 60vh;
  box-sizing: border-box;
  padding: 15px;
  background-color: rgba(0,110,125,0.3);
  border-right: solid 5px #0094A8;
  text-align: left;
}
</style>

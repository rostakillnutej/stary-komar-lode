<script>
  import { dock,shipSelected } from '../stores.js';
  import ShipsTable from '../objects/ShipsTable.js'
  export let tableSize;

  let st = new ShipsTable(tableSize);
	let grid = st.grid

  function putShip(elem){
    const x = parseInt(elem.getAttribute('x'));
    const y = parseInt(elem.getAttribute('y'));
    if(x + $shipSelected.width > tableSize || y + $shipSelected.height > tableSize)return
    if(!st.placeShip($shipSelected,x,y))return
    grid = st.grid
    shipSelected.update(_ => false)
    const exist = document.querySelector('#sticked')
    if(exist)exist.remove()
  }

  function getShip(id){
    //const x = parseInt(elem.getAttribute('x'));
    //const y = parseInt(elem.getAttribute('y'));


    shipSelected.update(_ => st.ships[id])
    const cln = e.explicitOriginalTarget.cloneNode(true);
    cln.setAttribute('id', 'sticked');
    document.body.appendChild(cln);

    /* Tady nevím jestli se potom ty listenery mažou*/
/*
    document.addEventListener('mousemove', e => {
    	cln.style.transform = 'translateY('+ (e.clientY + 10) + 'px)';
    	cln.style.transform += 'translateX('+ (e.clientX - 20) + 'px)';
    },false);
*/


/*
    const ship = $dock[$shipSelected - 1]
    if(x + ship.width > tableSize || y + ship.height > tableSize)return
    st.placeShip(ship,x,y)
    grid = st.grid
    shipSelected.update(_ => false)
    const exist = document.querySelector('#sticked')
    if(exist)exist.remove()
*/

  }


  function handleClick(e){
    const elem = e.target;
    if(elem.tagName != 'TD') return;

    //Ship add event handling
    if($shipSelected){
      putShip(elem)
      return;
    }
    //Selecting already placed ship on ShipTable
    const id = parseInt(elem.getAttribute('cell'));
    if(id){
      getShip(id);
    }

  }

  function handleOver(e){
    //console.log(e)
  }

</script>

<table on:click={(e) => handleClick(e)}
  on:mousemove={(e) => handleOver(e)}>
{#each grid as cols, y}
  <tr>
    {#each cols as cell, x}
      <td {y}{x}{cell} class:visible="{cell}"></td>
    {/each}
  </tr>
{/each}
</table>


<style>
  table {

  }
  table:hover {
  	cursor: crosshair;
  }
  td {
    background-color: black;
    height: 40px;
    width: 40px;
  }

  td.visible {
    background-color: red;
  }
</style>

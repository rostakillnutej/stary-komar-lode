<script>
  import { socket,shipSelected,dock } from '../stores/planning.js';
  import { createEventDispatcher } from 'svelte';
  const dispatch = createEventDispatcher();
	export let props;
  export let index;

  function handleClick(e){
    if($shipSelected)return;
    e.stopPropagation();
    dispatch('select',{e,index});
  }

  function handleRotate(){
    $socket.emit('rotateShip',index);
  }

</script>

<div class="ship">

  <button class="rotate"
  on:click={handleRotate}></button>

  <div class="name">{props.name}</div>
  <div>
    <table on:click={(e) => handleClick(e)}
      cellspacing="0"
      cellpadding="0"
      class="ship-grid">
    {#each props.grid as cols}
      <tr>
        {#each cols as line}
          <td class:visible="{line}"></td>
        {/each}
      </tr>
    {/each}
    </table>
  </div>
</div>

<style>
.ship {
  position: relative;
  margin: 10px 0;
}
.name {
  margin-bottom: 5px;
  color: white;
  pointer-events: none;
}
.rotate {
  right: 0;
  top: 15px;
  position: absolute;
  width: 15px;
  height: 15px;
  background-color: white;
  background-image: url('/imgs/rotate.svg');
  background-position: center;
  background-repeat: no-repeat;
  background-size: 80%;

}
</style>

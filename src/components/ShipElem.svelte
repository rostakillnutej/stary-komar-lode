<script>
  import { createEventDispatcher } from 'svelte';
  const dispatch = createEventDispatcher();
	export let props;
  export let index;


</script>

<div>
  <div>{props.name}</div>
  <div>
    <table on:click={(e) => dispatch('select',index)} cellspacing="0" cellpadding="0">
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
table:not(#sticked) {
  transition: transform 0.6s;
}
table:hover {
  transform: scale(1.2);
}
tr {
  pointer-events: none;
}
td.visible {
  width: 20px;
  height: 20px;
  background-color: blue;
}

</style>

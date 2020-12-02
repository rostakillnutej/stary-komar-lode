<script>
  import { socket,myTable } from '../stores/game.js';
    import * as lode from '../lodeLib.js';


</script>

<main>
<table cellspacing="0"
  cellpadding="0">
{#if $myTable}
  {#each $myTable as cols, y}
    <tr>
      {#each cols as cell, x}
        <td {y}{x}{cell} class:visible="{cell}" class={lode.getBorderClass($myTable,y,x,cell)}></td>
      {/each}
    </tr>
  {/each}
{/if}
</table>
</main>

<style>
table {
  float: left;
  background: rgb(0,95,225,0.6);
  border: solid 4px #005FE1;
}

td {
  position: relative;
  border: solid 1px white;
  //background-color: black;
  height: 30px;
  width: 30px;
}

td:nth-child(n+10){
  border-right: 0;
}
td:nth-child(10n+1){
  border-left: 0;
}
tr:first-child td{
  border-top: 0;
}
tr:last-child td{
  border-bottom: 0;
}

td.visible {
  background: #FD1648;
}

td[cell="h"] {
  background: rgba(255, 0, 0, 0.5);
}

td.visible:not([cell="h"])::after {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  height: 26px;
  width: 26px;
  //box-sizing: border-box;
  border: solid black 2px;
}
/* Vypnutí borderu mezi částemi lodě */
td.visible.nb-t::after{
  padding-bottom: 2px;
  border-top: 0;
}

td.visible.nb-b::after{
  padding-top: 2px;
  border-bottom: 0;
}

td.visible.nb-r::after{
  padding-left: 2px;
  border-right: 0;
}

td.visible.nb-l::after{
  padding-right: 2px;
  border-left: 0;
}

</style>

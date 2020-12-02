import { readable,writable } from 'svelte/store';

export const socket = writable();

export const myTable = writable([]);
export const enemyTable = writable([]);

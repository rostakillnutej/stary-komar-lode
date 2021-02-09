import { readable,writable } from 'svelte/store';

export const baseAddr = readable('http://localhost:8000');
export const state = writable('loading');
//export const state = writable('gameEnd');
export const winner = writable('');

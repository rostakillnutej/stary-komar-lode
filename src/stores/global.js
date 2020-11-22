import { readable,writable } from 'svelte/store';
export const baseAddr = readable('http://localhost:8000');
export const baseAddrIo = readable('wss://localhost:8000');
export const state = writable('menu');

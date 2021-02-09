import { readable,writable,get } from 'svelte/store';

export const shipSelected = writable(false);

export const dock = writable([]);

export const table = writable();
export const tableSize = writable(0);

export const isHover = writable(false);
export const hoverPos = writable([]);

export const socket = writable();

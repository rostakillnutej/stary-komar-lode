import { readable,writable } from 'svelte/store';
export const baseAddr = readable('http://localhost:8000');

export const shipSelected = writable(false);

import Ship from './objects/Ship.js'
/*
  Přiklad používání lodí
  Vytvářet se budo automaticky
  proto je to writable
  Toto je jenom na testování
*/
let s1 = new Ship('Fregata')
s1.preCreate(5,3);
s1.fill(1,0,3,0,1);
s1.fill(0,1,4,1,1);
s1.fill(1,2,3,2,1);
let s2 = new Ship('Křižník')
s2.preCreate(3,1);
s2.fill(0,0,2,0,1);
let s3 = new Ship('Výsadková loď')
s3.preCreate(2,3);
s3.fill(0,0,1,2,1);
s3.grid[0][1] = 0;
s3.grid[2][1] = 0;
s3.rotate();

export const dock = writable([s1,s2,s3]);

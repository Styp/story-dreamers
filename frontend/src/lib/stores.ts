import { writable } from 'svelte/store';
import type {ServerPage} from "./api";

export const text = writable<string>('');

export const currentPage = writable<ServerPage>(null)

export const totalPages = writable<number>(0)

export const currentPageNumber = writable<number>(1)
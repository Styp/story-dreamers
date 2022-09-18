import { writable, derived } from 'svelte/store';
import type {ProcessedTextItem, BookletPage} from "./api";
import {get_image} from "./api";
import asyncDerived from "./asyncDerived";

export const text = writable<string>('');

export const totalPages = writable<number>(0)

export const currentPageNumber = writable<number>(0)

export const pages = writable<ProcessedTextItem[]>([])

export const loading = writable<boolean>(false)

export const currentPage = asyncDerived<any,BookletPage>([pages, currentPageNumber], async ([pages, currentPageNumber]) =>{
    if (pages.length) {
        const image = await get_image(pages[currentPageNumber]?.prompt)
        return {
            snippet: pages[currentPageNumber].snippet,
            image: image?.image,
            hasNext: pages.length > currentPageNumber + 1,
            hasPrevious: currentPageNumber > 0
        }
    }
    else{
        return null
    }
})

export const preloadImages = asyncDerived([pages], async ([pages]) => {
    console.log('preload')
    for(const [index, page] of pages.entries()){
        await get_image(pages[index].prompt)
    }
})

export const promptCache = writable<{[key: string]: {image: string}}>({})

export function reset_story(){
    text.set('')
    pages.set([])
    currentPageNumber.set(0)
}